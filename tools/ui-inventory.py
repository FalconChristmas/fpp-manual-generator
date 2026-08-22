#!/usr/bin/env python3
"""
Print the FPP web UI's page/tab tree, for auditing manual coverage.

Walks the pages listed in the running FPP's navigation menu, fetches each one,
and reports the tabs (Bootstrap tab/pill triggers) inside it. Use the output to
re-check COVERAGE.md after an FPP release -- anything new here that COVERAGE.md
does not list is a page or tab the manual has not caught up with.

Usage:
    python3 tools/ui-inventory.py [base_url]      # default http://localhost

Needs a running, reachable FPP. Python standard library only.
"""
import html
import re
import sys
import urllib.request

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://localhost").rstrip("/")
TIMEOUT = 30


def fetch(path):
    try:
        with urllib.request.urlopen(f"{BASE}/{path}", timeout=TIMEOUT) as r:
            return r.read().decode("utf8", "ignore")
    except Exception as exc:
        print(f"    !! could not fetch {path}: {exc}", file=sys.stderr)
        return ""


def text(fragment):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", fragment))).strip()


def menu_pages(home):
    """Local .php pages linked from the nav menu, in menu order, de-duplicated."""
    pages, seen = [], set()
    for m in re.finditer(r'<a[^>]*href="([^"]+\.php)(?:[^"]*)?"[^>]*>', home):
        p = m.group(1).lstrip("/")
        if "://" in p or p.startswith("plugin.php") or p in seen:
            continue
        seen.add(p)
        pages.append(p)
    return pages


def tabs_in(body):
    """Tab/pill triggers, with the global nav and scripts stripped out first."""
    body = re.sub(r"(?s)<(script|style)\b.*?</\1>", " ", body)
    body = re.sub(r"(?s)<nav\b.*?</nav>", " ", body)
    found, seen = [], set()
    pattern = (
        r'<(?:a|button)[^>]*(?:data-bs-toggle|data-toggle)=["\']?(?:tab|pill)["\']?'
        r"[^>]*>(.*?)</(?:a|button)>"
    )
    for m in re.finditer(pattern, body, re.S):
        t = text(m.group(1))
        if t and len(t) < 60 and t not in seen:
            seen.add(t)
            found.append(t)
    return found


def main():
    home = fetch("index.php")
    if not home:
        sys.exit(f"Could not reach an FPP web UI at {BASE}")
    pages = menu_pages(home)
    print(f"FPP UI inventory from {BASE}  ({len(pages)} menu pages)\n")
    for page in pages:
        body = fetch(page)
        if not body:
            continue
        h1 = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
        title = text(h1.group(1)) if h1 else ""
        print(f"{page}" + (f"   [{title}]" if title else ""))
        for t in tabs_in(body):
            print(f"    tab: {t}")
    print("\nCompare against COVERAGE.md; anything unlisted there is a coverage gap.")


if __name__ == "__main__":
    main()
