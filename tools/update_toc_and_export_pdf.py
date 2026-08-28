#!/usr/bin/env python3
"""Load a .docx in a headless LibreOffice instance, recalculate its table of
contents (and any other index/field), and export the result as a PDF.

Pandoc's .docx table of contents is a Word field with no cached entries --
Word/LibreOffice normally compute it the moment a human opens the file. A
plain `soffice --headless --convert-to pdf` skips that step, so the exported
PDF's table of contents comes out empty. This script drives LibreOffice over
its UNO API (the standard automation path) to force that recalculation before
exporting, since dispatching the same fix via a `vnd.sun.star.script:` macro
URI as a one-shot headless call is unreliable (it can return immediately
without running, or hang).

Usage: update_toc_and_export_pdf.py <src.docx> <out.pdf> <profile_dir>
"""
import socket
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue


def make_prop(name, value):
    prop = PropertyValue()
    prop.Name = name
    prop.Value = value
    return prop


def free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


def wait_for_port(port, timeout):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=1):
                return True
        except OSError:
            time.sleep(0.3)
    return False


def main():
    src, out, profile = sys.argv[1], sys.argv[2], sys.argv[3]
    port = free_port()

    soffice = subprocess.Popen([
        "soffice", "--headless", "--invisible", "--nologo", "--norestore",
        f"-env:UserInstallation=file://{profile}",
        f"--accept=socket,host=localhost,port={port};urp;",
    ])
    try:
        if not wait_for_port(port, timeout=60):
            raise RuntimeError("soffice did not open its listening port in time")

        local_ctx = uno.getComponentContext()
        resolver = local_ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", local_ctx)

        ctx = None
        last_err = None
        deadline = time.time() + 30
        while time.time() < deadline:
            try:
                ctx = resolver.resolve(
                    f"uno:socket,host=localhost,port={port};urp;StarOffice.ComponentContext")
                break
            except Exception as e:  # noqa: BLE001 - retry until the bridge is ready
                last_err = e
                time.sleep(0.5)
        if ctx is None:
            raise RuntimeError(f"could not connect to soffice: {last_err}")

        desktop = ctx.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", ctx)
        doc = desktop.loadComponentFromURL(
            "file://" + src, "_blank", 0, (make_prop("Hidden", True),))

        indexes = doc.getDocumentIndexes()
        for i in range(indexes.getCount()):
            indexes.getByIndex(i).update()
        doc.getTextFields().refresh()

        doc.storeToURL("file://" + out, (make_prop("FilterName", "writer_pdf_Export"),))
        doc.close(False)
    finally:
        try:
            soffice.terminate()
            soffice.wait(timeout=10)
        except Exception:  # noqa: BLE001 - best-effort cleanup
            soffice.kill()


if __name__ == "__main__":
    main()
