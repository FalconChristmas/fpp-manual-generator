#!/usr/bin/env python3
"""
Report which of FPP's UI-visible settings the manual does not mention.

Reads FPP's settings.json, works out which settings are actually rendered by a
settings page (a setting is UI-visible if it is printed directly with
PrintSetting*, or belongs to a settingGroup that a page prints), then checks each
one's description against the text of chapters/.

Usage:
    python3 tools/settings-coverage.py [path-to-fpp]     # default /opt/fpp

Exit status is 0 always; it is a report, not a gate. A listed setting is not
automatically a defect -- some are self-explanatory, and the manual may describe
one in different words -- but the list is where to look for real omissions.
"""
import glob
import html
import json
import os
import re
import sys
import unicodedata

FPP = sys.argv[1] if len(sys.argv) > 1 else "/opt/fpp"
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEVELS = {0: "Basic", 1: "Advanced", 2: "Experimental", 3: "Developer"}


def normalise(text):
    # Settings descriptions are HTML fragments; the manual is plain text.
    text = html.unescape(text)
    text = unicodedata.normalize("NFKD", text)
    for dash in "‑–—":
        text = text.replace(dash, "-")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", text.lower())).strip()


# Settings the manual deliberately covers under a different wording, or that need
# no prose of their own. Keeping them here stops the report crying wolf; remove an
# entry if you want to be reminded to write about it.
ACCEPTED = {
    # covered collectively rather than one line each
    "BBBLeds0", "BBBLeds1", "BBBLeds2", "BBBLeds3",   # "BeagleBone LEDs"
    "tableColorPair1A", "tableColorPair1B", "tableColorPair2A", "tableColorPair2B",
    "tableColorPair3A", "tableColorPair3B", "tableColorPair4A", "tableColorPair4B",
    "TetherInterface", "TetherSSID", "TetherPSK",     # Network -> Tethering
    # documented, but the manual pairs the label with its sibling
    "MQTTPort", "emailport", "emailpass",
    "eFuseRetryInterval", "pauseBackgroundEffects", "PipeWireRoutingMatrix",
    # confirmation fields with no behaviour to describe
    "passwordVerify", "osPasswordVerify",
    # documented under a shortened label ("Rotate Kiosk")
    "KioskRotate",
}


def main():
    settings_json = os.path.join(FPP, "www", "settings.json")
    if not os.path.exists(settings_json):
        sys.exit(f"No FPP settings.json at {settings_json} -- pass the path to your fpp checkout.")
    data = json.load(open(settings_json))
    settings, groups = data["settings"], data["settingGroups"]

    printed = set()
    for path in glob.glob(os.path.join(FPP, "www", "*.php")) + glob.glob(
        os.path.join(FPP, "www", "common", "*.php")
    ):
        try:
            src = open(path, encoding="utf8", errors="ignore").read()
        except OSError:
            continue
        printed |= set(re.findall(r"PrintSetting\w*\(\s*'([A-Za-z0-9_-]+)'", src))

    visible = {k for k in printed if k in settings}
    for name in printed & set(groups):
        visible |= {k for k in groups[name].get("settings", []) if k in settings}

    manual = "".join(
        open(f, encoding="utf8").read() for f in sorted(glob.glob(os.path.join(HERE, "chapters", "*.md")))
    )
    body = normalise(manual)

    missing = []
    for key in sorted(visible):
        if key in ACCEPTED:
            continue
        desc = settings[key].get("description", "").strip()
        if not desc:
            continue
        want = normalise(desc)
        words = want.split()
        found = want in body or (len(words) > 3 and " ".join(words[:4]) in body)
        if not found:
            missing.append((settings[key].get("level", 0), key, desc))

    checked = len(visible) - len(ACCEPTED & visible)
    covered = checked - len(missing)
    pct = 100.0 * covered / checked if checked else 0.0
    print(
        f"UI-visible settings: {len(visible)}  "
        f"(checked {checked}, {len(ACCEPTED & visible)} accepted as covered elsewhere)\n"
        f"documented: {covered} ({pct:.0f}%)   unmatched: {len(missing)}\n"
    )
    for level in sorted(LEVELS):
        rows = [m for m in missing if m[0] == level]
        if rows:
            print(f"--- {LEVELS[level]} ({len(rows)}) ---")
            for _, key, desc in rows:
                print(f"   {key:34} {desc[:60]}")
            print()


if __name__ == "__main__":
    main()
