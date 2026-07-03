#!/bin/bash
# Render annotated screenshots into build/images/ for preview.
#
# Annotations live in annotations/<image-stem>.yaml and are drawn onto the raw
# screenshots from images/. This standalone run is handy for checking placement
# (render, then open build/images/<name>.png) — but you don't have to run it by
# hand: generate.sh and generate-web.sh apply annotations automatically.
#
# Needs python3-pil + python3-yaml (see ./install.sh).
set -e
HERE="$(cd "$(dirname "$0")" && pwd)"
python3 "$HERE/tools/annotate.py" "$HERE/images" "$HERE/annotations" "$HERE/build/images"
echo "Annotated images in build/images/ (raw screenshots in images/ are untouched)."
