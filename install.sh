#!/bin/bash
# Install the software needed to generate the FPP manual.
#
#   pandoc         - converts the Markdown chapters into the .docx
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

echo "Installing pandoc, poppler-utils, python3, chromium..."
# The Chromium package is named 'chromium' on Debian and 'chromium-browser' on
# some Ubuntu releases; try both.
$SUDO apt-get install -y pandoc poppler-utils python3 chromium \
  || $SUDO apt-get install -y pandoc poppler-utils python3 chromium-browser

echo
echo "Install complete."
echo "  Generate the manual : ./generate.sh"
echo "  Re-capture screens  : ./capture.sh [http://<fpp-host>]   (needs a running FPP)"
