#!/bin/bash
# Build the FPP v10 manual .docx (and, when possible, a matching .pdf) from the
# Markdown chapters.
#
# Usage:  ./build.sh            # builds ../FPP_Manual_v10.docx (+ .pdf)
#         OUT=/path/x.docx ./build.sh
#         PDF=0 ./build.sh      # build the .docx only, skip the PDF
#
# The PDF is produced by converting the just-built .docx with LibreOffice, so it
# matches the Word styling exactly. If LibreOffice isn't installed the PDF step is
# skipped with a hint (the .docx still builds). Install it via ./install.sh.
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

# If any screenshot annotations exist, bake them onto a mirror of images/ in
# build/images/ and use that instead (raw images/ stays pristine). See
# annotations/README.md. Falls back to images/ if the annotate step fails.
IMG_DIR="$IMAGES_DIR"
RESOURCE_PATH="$MANUAL_DIR:$IMAGES_DIR:$CHAPTERS_DIR"
shopt -s nullglob
ANN_SPECS=( "$MANUAL_DIR"/annotations/*.yaml "$MANUAL_DIR"/annotations/*.yml )
if [ "${#ANN_SPECS[@]}" -gt 0 ]; then
    if python3 "$HERE/annotate.py" "$IMAGES_DIR" "$MANUAL_DIR/annotations" \
            "$MANUAL_DIR/build/images"; then
        IMG_DIR="$MANUAL_DIR/build/images"
        RESOURCE_PATH="$MANUAL_DIR/build:$RESOURCE_PATH"
    else
        echo "Annotation step failed; building with un-annotated images." >&2
    fi
fi

# --resource-path lets image paths in the markdown be relative to images/.
pandoc \
    "$MANUAL_DIR/metadata.yaml" \
    "${CH[@]}" \
    --from=markdown+pipe_tables+backtick_code_blocks+implicit_figures \
    --reference-doc="$HERE/reference.docx" \
    --resource-path="$RESOURCE_PATH" \
    --toc --toc-depth=3 \
    --number-sections \
    --top-level-division=chapter \
    -o "$OUT"

echo "Wrote $OUT"
ls -la "$OUT"

# --- PDF (optional) --------------------------------------------------------
# Convert the .docx to .pdf with LibreOffice so the PDF matches the Word styling
# from reference.docx exactly. Set PDF=0 to skip.
if [ "${PDF:-1}" != "0" ]; then
    SOFFICE="$(command -v libreoffice || command -v soffice || true)"
    if [ -n "$SOFFICE" ]; then
        PDF_OUT="${OUT%.docx}.pdf"
        OUT_DIR="$(dirname "$OUT")"
        # Use a throwaway profile dir so headless runs don't clash with a desktop
        # LibreOffice session or a locked default profile.
        PROFILE="$(mktemp -d)"
        echo "Converting to PDF with $(basename "$SOFFICE") ->"
        "$SOFFICE" --headless --convert-to pdf --outdir "$OUT_DIR" \
            -env:UserInstallation="file://$PROFILE" "$OUT" >/dev/null
        rm -rf "$PROFILE"
        if [ -f "$PDF_OUT" ]; then
            echo "Wrote $PDF_OUT"
            ls -la "$PDF_OUT"
        else
            echo "PDF conversion did not produce $PDF_OUT" >&2
            exit 1
        fi
    else
        echo "Skipping PDF: LibreOffice not found (install it with ./install.sh," \
             "or set PDF=0 to silence this)." >&2
    fi
fi
