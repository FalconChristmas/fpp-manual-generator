#!/usr/bin/env python3
"""
Minimal Chrome DevTools Protocol screenshot driver (pure stdlib).

Captures full-page PNG screenshots of the running FPP web UI for the v10 manual.
No node/puppeteer/pip required -- implements just enough of the WebSocket
protocol to talk CDP to a headless Chromium started with --remote-debugging-port.

Usage:
    python3 shoot.py <base_url> <shotlist_file> <out_dir>

shotlist_file: lines of "outfile.png<TAB>path_or_url[<TAB>settle_ms]"
Lines starting with # are ignored.
"""
import base64
import hashlib
import json
import os
import signal
import socket
import struct
import subprocess
import sys
import time
import urllib.request


CHROME = "chromium"
DEBUG_PORT = 9333
WIDTH = 1440


class WS:
    """Very small WebSocket client (text frames only, client->server masked)."""

    def __init__(self, url):
        # url like ws://127.0.0.1:9333/devtools/page/XXXX
        assert url.startswith("ws://")
        hostport, _, path = url[5:].partition("/")
        host, _, port = hostport.partition(":")
        self.sock = socket.create_connection((host, int(port or 80)))
        key = base64.b64encode(os.urandom(16)).decode()
        req = (
            f"GET /{path} HTTP/1.1\r\n"
            f"Host: {hostport}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n\r\n"
        )
        self.sock.sendall(req.encode())
        # read handshake response headers
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.sock.recv(4096)
        self._buf = buf.split(b"\r\n\r\n", 1)[1]

    def _recv_exact(self, n):
        while len(self._buf) < n:
            self._buf += self.sock.recv(65536)
        out, self._buf = self._buf[:n], self._buf[n:]
        return out

    def send(self, data):
        payload = data.encode()
        header = struct.pack("!B", 0x81)  # FIN + text
        mask = os.urandom(4)
        n = len(payload)
        if n < 126:
            header += struct.pack("!B", 0x80 | n)
        elif n < 65536:
            header += struct.pack("!BH", 0x80 | 126, n)
        else:
            header += struct.pack("!BQ", 0x80 | 127, n)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.sock.sendall(header + mask + masked)

    def recv(self):
        b0, b1 = self._recv_exact(2)
        length = b1 & 0x7F
        if length == 126:
            length = struct.unpack("!H", self._recv_exact(2))[0]
        elif length == 127:
            length = struct.unpack("!Q", self._recv_exact(8))[0]
        return self._recv_exact(length).decode("utf-8", "replace")

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


class CDP:
    def __init__(self, ws_url):
        self.ws = WS(ws_url)
        self._id = 0

    def call(self, method, **params):
        self._id += 1
        mid = self._id
        self.ws.send(json.dumps({"id": mid, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == mid:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})
            # otherwise it's an event; ignore


def start_chrome():
    proc = subprocess.Popen(
        [
            CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
            "--hide-scrollbars", "--disable-dev-shm-usage",
            f"--remote-debugging-port={DEBUG_PORT}",
            f"--window-size={WIDTH},1000",
            "--force-device-scale-factor=1",
            "about:blank",
        ],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        # Own session/process group so Chromium's child processes (gpu, zygote,
        # crashpad) do not inherit our stdio pipes -- otherwise the calling shell
        # never sees EOF and hangs until timeout. Lets us kill the whole tree too.
        start_new_session=True,
    )
    # wait for the debugging endpoint and grab the existing page target
    ws_url = None
    for _ in range(100):
        try:
            data = urllib.request.urlopen(
                f"http://127.0.0.1:{DEBUG_PORT}/json/list", timeout=1
            ).read()
            for t in json.loads(data):
                if t.get("type") == "page" and t.get("webSocketDebuggerUrl"):
                    ws_url = t["webSocketDebuggerUrl"]
                    break
            if ws_url:
                break
        except Exception:
            pass
        time.sleep(0.2)
    if not ws_url:
        proc.kill()
        raise RuntimeError("Chromium page target never came up")
    return proc, ws_url


def main():
    base_url, shotlist, out_dir = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(out_dir, exist_ok=True)
    shots = []
    with open(shotlist) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            out = parts[0]
            path = parts[1]
            settle = int(parts[2]) if len(parts) > 2 else 3500
            js = parts[3] if len(parts) > 3 and parts[3].strip() else None
            # optional 5th field: fixed clip height (px). Captures only that many
            # pixels from the top of a fixed-height viewport -- use it to frame a
            # centred modal or the top of a very tall page.
            clip_h = int(parts[4]) if len(parts) > 4 and parts[4].strip() else None
            shots.append((out, path, settle, js, clip_h))

    proc, page_ws = start_chrome()
    try:
        page = CDP(page_ws)
        page.call("Page.enable")
        page.call("Runtime.enable")
        page.call("Emulation.setDeviceMetricsOverride",
                  width=WIDTH, height=1000, deviceScaleFactor=1, mobile=False)

        for out, path, settle, js, clip_h in shots:
            url = path if path.startswith("http") else base_url.rstrip("/") + "/" + path.lstrip("/")
            try:
                # A fixed clip height gets its own viewport so centred modals frame
                # nicely; otherwise use a tall viewport and capture full content.
                vp_h = clip_h if clip_h else 1000
                page.call("Emulation.setDeviceMetricsOverride",
                          width=WIDTH, height=vp_h, deviceScaleFactor=1, mobile=False)
                # Force a full document load every time. Reusing one page means a
                # bare "#hash" change would be a same-document navigation and the
                # page's onload tab-selection JS would not re-run.
                page.call("Page.navigate", url="about:blank")
                time.sleep(0.25)
                page.call("Page.navigate", url=url)
                time.sleep(settle / 1000.0)
                if js:
                    # e.g. click a sub-tab / open a modal, then let it render
                    page.call("Runtime.evaluate", expression=js, awaitPromise=True)
                    time.sleep(2.0)
                if clip_h:
                    w, h = WIDTH, clip_h
                else:
                    metrics = page.call("Page.getLayoutMetrics")
                    size = metrics.get("cssContentSize") or metrics.get("contentSize")
                    h = min(int(size["height"]), 20000)  # sanity cap
                    w = int(size.get("width", WIDTH)) or WIDTH
                clip = {"x": 0, "y": 0, "width": w, "height": h, "scale": 1}
                shot = page.call(
                    "Page.captureScreenshot",
                    format="png", captureBeyondViewport=True, clip=clip,
                )
                dest = os.path.join(out_dir, out)
                with open(dest, "wb") as fh:
                    fh.write(base64.b64decode(shot["data"]))
                print(f"OK   {out}  ({w}x{h})  {url}")
            except Exception as e:
                print(f"FAIL {out}  {url}  -> {e}")
    finally:
        try:
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        except (ProcessLookupError, OSError):
            proc.kill()


if __name__ == "__main__":
    main()
