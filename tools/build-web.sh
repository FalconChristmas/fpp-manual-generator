#!/bin/bash
# Build the FPP v10 manual as a browsable web site (HTML with sidebar navigation
# and built-in search) from the same Markdown chapters used for the .docx/.pdf.
#
# Usage:  ./build-web.sh            # build the static site into web/site/
#         ./build-web.sh serve      # live-preview at http://localhost:8000
#
# Requires mkdocs + the Material theme (see ../install.sh). Does NOT need a
# running FPP. The chapters remain the single source of truth: this script
# stages a lightly-transformed copy under web/docs/ and never edits chapters/.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
MANUAL_DIR="$(dirname "$HERE")"
CHAPTERS_DIR="$MANUAL_DIR/chapters"
IMAGES_DIR="$MANUAL_DIR/images"
DOCS_DIR="$MANUAL_DIR/web/docs"     # generated staging dir (git-ignored)

if ! command -v mkdocs >/dev/null 2>&1; then
    echo "mkdocs not found. Install it with ./install.sh (installs mkdocs-material)." >&2
    exit 1
fi

# --- Stage the chapters ----------------------------------------------------
# Rebuild web/docs/ from scratch so removed chapters/images don't linger.
rm -rf "$DOCS_DIR"
mkdir -p "$DOCS_DIR"

shopt -s nullglob
count=0
for md in "$CHAPTERS_DIR"/*.md; do
    base="$(basename "$md")"
    # webify.py strips Pandoc's "{-}" markers and converts the "> **Note:** …"
    # blockquotes into Material admonition callouts (web edition only; chapters/
    # are never modified).
    python3 "$HERE/webify.py" < "$md" > "$DOCS_DIR/$base"
    count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
    echo "No chapter markdown files found in $CHAPTERS_DIR" >&2
    exit 1
fi

# MkDocs needs an index.md for the site root (…/ → index.html). Promote the
# lowest-numbered chapter (the "About" page) to the home page; it also stays the
# first item in the auto-generated nav.
first="$(ls "$DOCS_DIR"/*.md | sort | head -1)"
if [ -n "$first" ] && [ ! -e "$DOCS_DIR/index.md" ]; then
    mv "$first" "$DOCS_DIR/index.md"
fi

# Copy images alongside the docs so the chapters' images/<name>.png links resolve.
# If screenshot annotations exist, bake them onto a mirror in build/images/ first
# and copy that instead (raw images/ stays pristine). See annotations/README.md.
SRC_IMAGES="$IMAGES_DIR"
shopt -s nullglob
ANN_SPECS=( "$MANUAL_DIR"/annotations/*.yaml "$MANUAL_DIR"/annotations/*.yml )
if [ "${#ANN_SPECS[@]}" -gt 0 ]; then
    # Annotations exist, so they must render (annotate.py exits non-zero if the
    # imaging libs are missing); set -e then aborts rather than silently shipping
    # un-annotated images. Repos with no sidecars skip this and need no Pillow.
    python3 "$HERE/annotate.py" "$IMAGES_DIR" "$MANUAL_DIR/annotations" \
        "$MANUAL_DIR/build/images"
    SRC_IMAGES="$MANUAL_DIR/build/images"
fi
if [ -d "$SRC_IMAGES" ]; then
    cp -r "$SRC_IMAGES" "$DOCS_DIR/images"
fi

# If the .docx/.pdf deliverables have already been built (./generate.sh), publish
# them alongside the site so the web edition offers a stable download URL
# (…/FPP_Manual_v10.pdf). MkDocs copies any non-Markdown file in docs_dir straight
# into the built site. They're optional here: if they're missing (web-only build)
# the site still builds and the header "Download" links simply 404 until a full
# build runs — CI always builds the .docx/.pdf first, so Pages always has them.
for deliverable in FPP_Manual_v10.docx FPP_Manual_v10.pdf; do
    if [ -f "$MANUAL_DIR/$deliverable" ]; then
        cp "$MANUAL_DIR/$deliverable" "$DOCS_DIR/$deliverable"
    fi
done

echo "Staged $count chapters -> web/docs/"

# --- Build or serve --------------------------------------------------------
cd "$MANUAL_DIR"
if [ "${1:-}" = "serve" ]; then
    echo "Serving live preview at http://localhost:8000 (Ctrl-C to stop)…"
    exec mkdocs serve
fi

# Note: not --strict. A not-yet-captured screenshot is only a warning here (same
# as the .docx build), so the site still builds; capture the image later with
# ./capture.sh and rebuild.
mkdocs build --clean
echo
echo "Wrote web site -> web/site/  (open web/site/index.html, or host the folder)"
