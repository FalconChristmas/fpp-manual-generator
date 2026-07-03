#!/bin/bash
# Build the FPP v10 manual .docx from the Markdown chapters.
#
# Usage:  ./build.sh            # builds ../FPP_Manual_v10.docx
#         OUT=/path/x.docx ./build.sh
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
MANUAL_DIR="$(dirname "$HERE")"
CHAPTERS_DIR="$MANUAL_DIR/chapters"
IMAGES_DIR="$MANUAL_DIR/images"
OUT="${OUT:-$MANUAL_DIR/FPP_Manual_v10.docx}"

# Chapters are combined in filename order (00-, 01-, 02- ...).
mapfile -t CH < <(find "$CHAPTERS_DIR" -maxdepth 1 -name '*.md' | sort)

if [ "${#CH[@]}" -eq 0 ]; then
    echo "No chapter markdown files found in $CHAPTERS_DIR" >&2
    exit 1
fi

echo "Building manual from ${#CH[@]} chapters ->"
printf '  %s\n' "${CH[@]##*/}"

# --resource-path lets image paths in the markdown be relative to images/.
pandoc \
    "$MANUAL_DIR/metadata.yaml" \
    "${CH[@]}" \
    --from=markdown+pipe_tables+backtick_code_blocks+implicit_figures \
    --reference-doc="$HERE/reference.docx" \
    --resource-path="$MANUAL_DIR:$IMAGES_DIR:$CHAPTERS_DIR" \
    --toc --toc-depth=3 \
    --number-sections \
    --top-level-division=chapter \
    -o "$OUT"

echo "Wrote $OUT"
ls -la "$OUT"
