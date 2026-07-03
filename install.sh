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
#   python3        - runs the build and screenshot scripts (standard library only)
#
# Works on the FPP OS image (Debian) and other Debian/Ubuntu systems.
set -e

SUDO=""
if [ "$(id -u)" -ne 0 ]; then SUDO="sudo"; fi

echo "Updating package lists..."
$SUDO apt-get update

echo "Installing pandoc, poppler-utils, python3, chromium, libreoffice-writer, mkdocs-material..."
# libreoffice-writer (not the full suite) is enough for the headless docx->pdf
# conversion and is much smaller.
# mkdocs-material builds the web edition; it pulls in mkdocs itself as a dep.
# The Chromium package is named 'chromium' on Debian and 'chromium-browser' on
# some Ubuntu releases; try both.
$SUDO apt-get install -y pandoc poppler-utils python3 libreoffice-writer mkdocs-material chromium \
  || $SUDO apt-get install -y pandoc poppler-utils python3 libreoffice-writer mkdocs-material chromium-browser

echo
echo "Install complete."
echo "  Generate the manual : ./generate.sh       (.docx + .pdf)"
echo "  Generate web edition: ./generate-web.sh   (static site in web/site/)"
echo "  Re-capture screens  : ./capture.sh [http://<fpp-host>]   (needs a running FPP)"
