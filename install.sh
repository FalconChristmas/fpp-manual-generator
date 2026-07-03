#!/bin/bash
# Install the software needed to generate the FPP manual.
#
#   pandoc         - converts the Markdown chapters into the .docx
#   libreoffice    - converts the .docx into a matching .pdf (headless). Large; if
#                    you only need the .docx you can skip it and build with PDF=0.
#   mkdocs-material - builds the browsable web edition (sidebar nav + search)
#                    from the same chapters (./generate-web.sh)
#   chromium       - headless browser used to screenshot the FPP web UI
#   poppler-utils  - pdftotext/pdfinfo, used only when refreshing content from a
#                    reference PDF (optional; safe to keep)
#   python3        - runs the build and screenshot scripts
#   python3-pil    - Pillow: draws screenshot annotations (annotations/ -> images)
#   python3-yaml   - reads the annotation sidecar files
#
# Works on the FPP OS image (Debian) and other Debian/Ubuntu systems.
set -e

SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

echo "Updating package lists..."
$SUDO apt-get update

echo "Installing pandoc, poppler-utils, python3, python3-pil, python3-yaml, chromium, libreoffice-writer, mkdocs-material..."
# libreoffice-writer (not the full suite) is enough for the headless docx->pdf
# conversion and is much smaller.
# mkdocs-material builds the web edition; it pulls in mkdocs itself as a dep.
# python3-pil (Pillow) + python3-yaml render the screenshot annotations.
# The Chromium package is named 'chromium' on Debian and 'chromium-browser' on
# some Ubuntu releases; try both.
$SUDO apt-get install -y pandoc poppler-utils python3 python3-pil python3-yaml libreoffice-writer mkdocs-material chromium \
  || $SUDO apt-get install -y pandoc poppler-utils python3 python3-pil python3-yaml libreoffice-writer mkdocs-material chromium-browser

echo
echo "Install complete."
echo "  Generate the manual : ./generate.sh       (.docx + .pdf)"
echo "  Generate web edition: ./generate-web.sh   (static site in web/site/)"
echo "  Re-capture screens  : ./capture.sh [http://<fpp-host>]   (needs a running FPP)"
