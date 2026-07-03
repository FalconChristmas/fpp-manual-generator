#!/usr/bin/env python3
"""Transform a manual chapter (stdin) into MkDocs-friendly Markdown (stdout).

Applied only to the *staged* copy under web/docs/ by build-web.sh; the chapters
themselves are never modified. Two transforms:

1. Strip Pandoc's "{-}" unnumbered-heading marker, which MkDocs would render
   literally.
2. Turn the manual's labelled "> **Note:** …" style blockquotes into Material
   admonition callouts (the nicely styled boxes). Only blockquotes led by a known
   keyword (Note/Tip/Warning/Important/Caution/Changed/Screenshots) are converted;
   a blockquote that merely starts with some other bold word (e.g. a button name)
   is left as an ordinary blockquote.

The .docx/.pdf build (Pandoc) is untouched and keeps the original blockquotes.
"""
import re
import sys

# keyword (first word of the bold label, lower-cased) -> admonition type
KEYWORD_TYPE = {
    "note": "note",
    "tip": "tip",
    "warning": "warning",
    "caution": "warning",
    "important": "info",
    "changed": "info",
    "screenshots": "note",
}

# First line of a candidate callout: "> **<label>** …" (the label may embed a
# trailing colon, e.g. "Note:"). Capture the label and any trailing text.
FIRST = re.compile(r"^>\s*\*\*([A-Za-z][^*]*?)\*\*\s*(.*)$")


def first_word(label: str) -> str:
    m = re.match(r"([A-Za-z]+)", label)
    return m.group(1).lower() if m else ""


def main() -> None:
    text = sys.stdin.read()
    # 1. Drop Pandoc "{-}" markers.
    lines = [re.sub(r"\s*\{-\}", "", ln) for ln in text.split("\n")]

    out: list[str] = []
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        m = FIRST.match(ln)
        if m and first_word(m.group(1).strip()) in KEYWORD_TYPE:
            label = m.group(1).strip()
            rest = m.group(2).strip()
            typ = KEYWORD_TYPE[first_word(label)]

            # Collect the rest of the blockquote (continuation "> …" lines).
            body = [rest] if rest else []
            j = i + 1
            while j < n and lines[j].startswith(">"):
                cont = lines[j][1:]
                if cont.startswith(" "):
                    cont = cont[1:]
                body.append(cont)
                j += 1

            # Title = the bold label without a trailing colon/period.
            title = label.rstrip(" :.").strip()
            if title.lower() == typ:
                out.append(f"!!! {typ}")
            else:
                out.append(f'!!! {typ} "{title}"')
            for b in body:
                out.append("    " + b if b.strip() else "")
            out.append("")  # blank line closes the admonition

            i = j
            if i < n and lines[i].strip() == "":
                i += 1  # avoid a doubled blank line
            continue

        out.append(ln)
        i += 1

    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
