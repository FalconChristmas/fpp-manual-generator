#!/usr/bin/env python3
"""Filter tools/shotlist.txt down to specific entries, for capture.sh --only.

Each requested token is matched against the shotlist, in order:
1. Exact match on the output filename (column 1), e.g. "network.png".
2. Exact match on the page/URL (column 2), e.g. "settings.php#settings-playback".
3. A "base page" match: column 2 with any #fragment or ?query stripped, e.g.
   "settings.php" matches every settings.php#settings-* tab. Several pages have
   more than one shotlist entry (a plain shot plus one or more modal shots, e.g.
   scheduler.php has three) -- a base-page match can resolve to all of them.

A token with a URL scheme (e.g. pasted from a browser address bar) is reduced
to just its path first, so "http://fpp.local/initialSetup.php" and
"initialSetup.php" match the same thing.

Usage: filter_shotlist.py <shotlist-file> <token1,token2,...>
Prints the matching shotlist lines to stdout, in original shotlist order, each
at most once. Prints one summary line per token to stderr: what it resolved to,
or a warning if nothing matched either way.
"""
import sys
from urllib.parse import urlsplit


def base_page(path_or_url: str) -> str:
    return path_or_url.split("#", 1)[0].split("?", 1)[0]


def normalize_token(token: str) -> str:
    if "://" in token:
        return urlsplit(token).path.lstrip("/")
    return token


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: filter_shotlist.py <shotlist-file> <comma,separated,tokens>")
    shotlist_path, tokens_arg = sys.argv[1], sys.argv[2]

    entries = []  # (outfile, path_or_url, raw_line)
    with open(shotlist_path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            cols = line.split("\t")
            if len(cols) >= 2:
                entries.append((cols[0], cols[1], line))

    matched_lines = []
    seen = set()

    for token in [t for t in tokens_arg.split(",") if t]:
        token_norm = normalize_token(token)
        matches = [e for e in entries if e[0] == token_norm]
        if not matches:
            matches = [e for e in entries if e[1] == token_norm]
        if not matches:
            token_base = base_page(token_norm)
            matches = [e for e in entries if base_page(e[1]) == token_base]

        if not matches:
            print(f"Warning: no shotlist entry matches '{token}' (checked image name and page)", file=sys.stderr)
            continue

        print(f"'{token}' -> {', '.join(m[0] for m in matches)}", file=sys.stderr)
        for m in matches:
            if m[2] not in seen:
                seen.add(m[2])
                matched_lines.append(m[2])

    for line in matched_lines:
        print(line)


if __name__ == "__main__":
    main()
