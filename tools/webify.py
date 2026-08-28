#!/usr/bin/env python3
"""Transform a manual chapter (stdin) into MkDocs-friendly Markdown (stdout).

Applied only to the *staged* copy under web/docs/ by build-web.sh; the chapters
themselves are never modified. Three transforms:

1. Strip Pandoc's "-" unnumbered-heading marker (`{-}` on its own, or merged into
   an id block like `{- #some-id}`), which MkDocs' attr_list doesn't understand and
   would otherwise emit as a stray `-="-"` HTML attribute (or render literally, for
   the standalone-`{-}` case).
2. Turn the manual's labelled "> **Note:** …" style blockquotes into Material
   admonition callouts (the nicely styled boxes). Only blockquotes led by a known
   keyword (Note/Tip/Warning/Important/Caution/Changed/Screenshots) are converted;
   a blockquote that merely starts with some other bold word (e.g. a button name)
   is left as an ordinary blockquote.
3. Rewrite cross-chapter section links. Chapters cross-reference each other with
   plain anchor links, e.g. `[FPP Settings](#fpp-settings)` pointing at a heading
   tagged `{#fpp-settings}`. Pandoc concatenates every chapter into one document,
   so that anchor-only link already works in the .docx/.pdf as-is. MkDocs instead
   builds one HTML page per chapter, so an anchor-only link only resolves when the
   target heading is on the *same* page. This pass builds an index of every
   `{#id}` heading across all chapters and, for links whose target lives on a
   different page, rewrites the href to `<that-page>.md#id` so MkDocs points at
   the right page. Same-page anchors are left untouched.

The .docx/.pdf build (Pandoc) is untouched and keeps the original links/blockquotes.
"""
import glob
import os
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


HEADING_ATTRS = re.compile(r"^(#{1,6}\s+.*?)\s*\{([^}]*)\}\s*$")


def strip_unnumbered_token(line: str) -> str:
    """Remove Pandoc's bare "-" (unnumbered) token from a heading's {...} block,
    keeping any other attributes (like an #id) intact."""
    m = HEADING_ATTRS.match(line)
    if not m:
        return line
    prefix, attrs = m.groups()
    tokens = [t for t in attrs.split() if t != "-"]
    return f"{prefix} {{{' '.join(tokens)}}}" if tokens else prefix


# Matches a heading line carrying an explicit Pandoc/attr_list id, e.g.
# "## Localization {#localization}". Both Pandoc and MkDocs' attr_list
# extension (enabled in mkdocs.yml) honour this syntax natively.
HEADING_ID = re.compile(r"^#{1,6}\s+.*\{[^}]*#([A-Za-z0-9_-]+)[^}]*\}\s*$")
ANCHOR_LINK = re.compile(r"(\[[^\]]+\]\()#([A-Za-z0-9_-]+)(\))")


def build_anchor_index(chapters_dir: str) -> dict[str, str]:
    """Map every explicit heading id to the web filename that will define it."""
    chapter_paths = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    first_base = os.path.basename(chapter_paths[0]) if chapter_paths else None

    index: dict[str, str] = {}
    for path in chapter_paths:
        base = os.path.basename(path)
        out_name = "index.md" if base == first_base else base
        with open(path, encoding="utf-8") as f:
            for line in f:
                m = HEADING_ID.match(line)
                if m:
                    index[m.group(1)] = out_name
    return index


def rewrite_cross_chapter_links(text: str, anchor_index: dict[str, str], current_out_name: str) -> str:
    def repl(m: re.Match) -> str:
        anchor_id = m.group(2)
        target = anchor_index.get(anchor_id)
        if target is None or target == current_out_name:
            return m.group(0)  # same-page anchor, or not a tagged heading: leave as-is
        return f"{m.group(1)}{target}#{anchor_id}{m.group(3)}"

    return ANCHOR_LINK.sub(repl, text)


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit("usage: webify.py <chapters-dir> <current-chapter-basename>")
    chapters_dir, current_base = sys.argv[1], sys.argv[2]
    chapter_paths = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    first_base = os.path.basename(chapter_paths[0]) if chapter_paths else None
    current_out_name = "index.md" if current_base == first_base else current_base

    text = sys.stdin.read()
    text = rewrite_cross_chapter_links(text, build_anchor_index(chapters_dir), current_out_name)
    # 1. Drop Pandoc's "-" unnumbered-heading token, whether it's alone in its own
    # {-} block or merged with an id, e.g. "{- #some-id}" / "{#some-id -}".
    lines = [strip_unnumbered_token(ln) for ln in text.split("\n")]

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
