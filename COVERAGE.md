# Manual coverage audit

Tracks how completely the manual documents FPP's UI — **every page and every tab
within a page**. Regenerate the page/tab inventory from a running FPP with
`tools/ui-inventory.py` (see below) and re-check this list after a release.

Status key: `OK` covered · `GAP` missing/incomplete · `STALE` describes something
that no longer exists · `—` n/a.

Last audited: FPP `10.x-master-1404-g793a20341` (Pi 5, OS v2026-08).

## Status / Control

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| Status Page (`index.php`) | — (Scheduler Status, Player Status, Playlist Details, Channel Inputs stats) | 20 | OK |
| Network (`networkconfig.php`) | Interface Settings · Global Network Settings · Tethering | 22 | OK |
| MultiSync (`multisync.php`) | — | 24 | OK |
| FPP Settings (`settings.php`) | 13 tabs — see below | 26 | OK |
| FPP Backup (`backup.php`) | JSON Configuration Backup · File Copy Backup | 28 | OK |
| Proxy Settings (`proxies.php`) | — | 28 | OK |
| Command Presets (`commandPresets.php`) | — | 32 | OK |
| Effects (`effects.php`) | — | 34 | OK |
| Display Testing (`testing.php`) | Channel Testing · Channel Fader · Sequence; sub-tabs RGB Test Patterns · Solid Color Fill · Single Channel | 36 | OK |
| 2D Virtual Display (`virtualdisplaywrapper.php`) | — | 57 | OK |
| 3D Virtual Display (`virtualdisplaywrapper3d.php`) | — | 57 | OK |
| Port Status (`currentmonitor.php`) | — | 20 | OK (needs current-monitoring cape) |

## FPP Settings tabs (`settings.php`)

Playback · Audio/Video · Localization · UI · Email · MQTT · Privacy ·
Input/Output · Logging · Services · Storage · System · Developer — all covered in
chapter 26.

| Tab | Status |
|---|---|
| Storage | OK — rewritten: SD Card Actions, Flash FPP to Another Device (Create / Copy / Create (BTRFS)), Storage Device + USB warnings, Mounted USB Device Actions |
| all others | OK |

## Content Setup

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| File Manager (`filemanager.php`) | Sequences · Audio · Video · Images · Effects · Scripts · Logs · Uploads · Crash Reports · Backups · Config | 40 | OK |
| Playlists (`playlists.php`) | — | 42 | OK |
| Scheduler (`scheduler.php`) | — (+ Preview and Calendar View modals) | 44 | OK |
| Script Repository (`scriptbrowser.php`) | — (deprecated in v10, removed in v11) | 48 | OK |
| Plugin Manager (`plugins.php`) | Available · Installed · Updates | 48 | OK |
| Packages (`packages.php`) | — | 48 | OK |
| Variables (`variables.php`) | User · FPP Read-only · MQTT Read-only | 49 | OK |
| Recurring Tasks (`recurringtasks.php`) | — | 49 | OK |

## Input / Output Setup

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| Channel Inputs (`channelinputs.php`) | E1.31/ArtNet/DDP Inputs · DMX | 50 | OK |
| Channel Outputs (`channeloutputs.php`) | E1.31/ArtNet/DDP/KiNet · *cape* Pixel Strings · *cape* PWM · *cape* LED Panels (Panel Matrix 1–n) · groups added via **+ Add Output Group**: DMX/Serial, GPIO, Virtuals, SPI, PWM, Control Signal | 52 | OK — corrected: those tabs are *added*, not automatic |
| Output Processors (`outputprocessors.php`) | — | 54 | OK |
| Pixel Overlay Models (`pixeloverlaymodels.php`) | — | 56 | OK |
| GPIO Inputs (`gpio.php`) | — | 58 | OK |

## Help

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| System Upgrade (`about.php`) | — | 60 | OK |
| Cape Info (`cape-info.php`) | About · EEPROM Signature · Voucher Redemption · EEPROM Upgrade | 60 | OK |
| Get Help (`help.php`) | — | 60 | OK |
| Credits (`credits.php`) | — | 60 | OK |
| System Health Check (`system-stats.php`) | System Health · Fan Monitoring · Disk Utilization · System Uptime · System Busyness · Player Statistics | 60 | OK |
| Troubleshooting (`troubleshooting.php`) | 18 category tabs (Networking, Disk, Date/Time, Memory/CPU, USB, Audio, Media Backend, Midi, Video, OS/Kernel/SD image, i2c, Processes, Boot, Git, GPIO, PHP, RPI Utils, Webserver) | 60 | OK — all tabs tabulated |
| REST API (`api/`) | — | 95 | OK |
| SSH Shell | — | 60 | OK |

## Reached from buttons, not the menu

| Page | Reached from | Chapter | Status |
|---|---|---|---|
| PipeWire routing matrix / graph / audio / video / input mixing / video inputs | Settings → Audio/Video | 27 | OK |
| AES67, Opus RTP, Sound Card Aliases | Settings → Audio/Video | 27 | OK |
| Flash storage (`flash-storage.php`) | Settings → Storage | 26 | OK |
| Grow Filesystem / New Partition | Settings → Storage | 26 | OK |
| Reset FPP Config (`resetConfig.php`) | Settings → System | 26 | OK |
| Cape firmware upgrade (`upgradeCapeFirmware.php`) | Cape Info, Pixel Strings | 60 | OK |
| MP3Gain (`run_mp3gain.php`) | File Manager → Audio | 40 | OK |
| Initial Setup (`initialSetup.php`) | first boot | 08 | OK |
| FPPOS upgrade (`upgradeOS.php`) | System Upgrade | 12 | OK |

`cronjobs.php` exists in the tree but nothing links to it — not documented, deliberately.

## Settings coverage

Every setting FPP actually renders on a settings page is described in chapter 26
(or, where it belongs elsewhere, in that chapter — Tethering in *Network*, the
MultiSync copy options in *MultiSync*, and so on).

```bash
python3 tools/settings-coverage.py       # against /opt/fpp
```

It works out which of `settings.json`'s entries are UI-visible (printed directly,
or a member of a settingGroup a page prints) and checks each description against
`chapters/`. Current state: **173 UI-visible settings, 149 checked, 100 %
documented**; the other 24 are listed in the script's `ACCEPTED` set because the
manual covers them collectively or under a different label (the BeagleBone LEDs,
the eight schedule colour pairs, the tethering trio, password-confirmation
fields). Drop a key from `ACCEPTED` if you want the report to nag about it again.

## Regenerating the inventory

```bash
python3 tools/ui-inventory.py            # against http://localhost
python3 tools/ui-inventory.py http://192.168.1.50
```

It walks the menu, fetches each page from a running FPP, and prints the page/tab
tree this table is built from.
