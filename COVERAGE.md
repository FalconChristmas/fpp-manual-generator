# Manual coverage audit

Tracks how completely the manual documents FPP's UI — **every page and every tab
within a page**. Regenerate the page/tab inventory from a running FPP with
`tools/ui-inventory.py` (see below) and re-check this list after a release.

Status key: `OK` covered · `GAP` missing/incomplete · `STALE` describes something
that no longer exists · `—` n/a.

Last audited: FPP `10.0-370e62ed7` (Pi 5, OS v2026-08).

> Chapter numbers below were refreshed 2026-08-30 for the 3-digit chapter
> restructuring (`chapters/` renumbered and several chapters split into smaller,
> single-topic files). The Content Setup chapters that were split — Scripts,
> Plugins, Packages, Variables, Recurring Tasks — are broken out into their own
> rows below to match.

## Status / Control

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| Status Page (`index.php`) | — (Scheduler Status, Player Status, Playlist Details, Channel Inputs stats) | 012 | OK |
| Network (`networkconfig.php`) | Interface Settings · Global Network Settings · Tethering | 016 | OK |
| MultiSync (`multisync.php`) | — | 018 | OK |
| FPP Settings (`settings.php`) | 13 tabs — see below | 020 | OK |
| FPP Backup (`backup.php`) | JSON Configuration Backup · File Copy Backup | 022 | OK |
| Proxy Settings (`proxies.php`) | — | 024 | OK — now its own chapter (split out of *Backup and Restore*) |
| Command Presets (`commandPresets.php`) | — | 026 | OK |
| Effects (`effects.php`) | — | 028 | OK |
| Display Testing (`testing.php`) | Channel Testing · Channel Fader · Sequence; sub-tabs RGB Test Patterns · Solid Color Fill · Single Channel | 030 | OK |
| 2D Virtual Display (`virtualdisplaywrapper.php`) | — | 106 | OK |
| 3D Virtual Display (`virtualdisplaywrapper3d.php`) | — | 106 | OK |
| Port Status (`currentmonitor.php`) | — | 014 | OK (needs current-monitoring cape) |

## FPP Settings tabs (`settings.php`)

Playback · Audio/Video · Localization · UI · Email · MQTT · Privacy ·
Input/Output · Logging · Services · Storage · System · Developer — all covered in
chapter 020.

| Tab | Status |
|---|---|
| Storage | OK — rewritten: SD Card Actions, Flash FPP to Another Device (Create / Copy / Create (BTRFS)), Storage Device + USB warnings, Mounted USB Device Actions |
| all others | OK |

## Content Setup

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| File Manager (`filemanager.php`) | Sequences · Audio · Video · Images · Effects · Scripts · Logs · Uploads · Crash Reports · Backups · Config | 034 | OK |
| Playlists (`playlists.php`) | — | 036 | OK |
| Scheduler (`scheduler.php`) | — (+ Preview and Calendar View modals) | 038 | OK |
| Script Repository (`scriptbrowser.php`) | — (deprecated in v10, removed in v11) | 040 | OK — now its own chapter (split out of *Plugins, Packages and Scripts*) |
| Plugin Manager (`plugins.php`) | Available · Installed · Updates | 042 | OK |
| Packages (`packages.php`) | — | 044 | OK — now its own chapter |
| Variables (`variables.php`) | User · FPP Read‑only · MQTT Read‑only | 046 | OK — now its own chapter (split out of *Variables and Recurring Tasks*) |
| Recurring Tasks (`recurringtasks.php`) | — | 048 | OK — now its own chapter |

## Input / Output Setup

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| Channel Inputs (`channelinputs.php`) | E1.31/ArtNet/DDP Inputs · DMX | 052 | OK |
| Channel Outputs (`channeloutputs.php`) | E1.31/ArtNet/DDP/KiNet · *cape* Pixel Strings · *cape* PWM · *cape* LED Panels (Panel Matrix 1–n) · groups added via **+ Add Output Group**: DMX/Serial, GPIO, Virtuals, SPI, PWM, Control Signal | 054 | OK — corrected: those tabs are *added*, not automatic |
| Output Processors (`outputprocessors.php`) | — | 056 | OK |
| Pixel Overlay Models (`pixeloverlaymodels.php`) | — | 058 | OK |
| GPIO Inputs (`gpio.php`) | — | 060 | OK |

## Help

| Page | Tabs / sub-sections | Chapter | Status |
|---|---|---|---|
| System Upgrade (`about.php`) | — | 064 | OK |
| Cape Info (`cape-info.php`) | About · EEPROM Signature · Voucher Redemption · EEPROM Upgrade | 064 | OK |
| Get Help (`help.php`) | — | 064 | OK |
| Credits (`credits.php`) | — | 064 | OK |
| System Health Check (`system-stats.php`) | System Health · Fan Monitoring · Disk Utilization · System Uptime · System Busyness · Player Statistics | 064 | OK |
| Troubleshooting (`troubleshooting.php`) | 18 category tabs (Networking, Disk, Date/Time, Memory/CPU, USB, Audio, Media Backend, Midi, Video, OS/Kernel/SD image, i2c, Processes, Boot, Git, GPIO, PHP, RPI Utils, Webserver) | 064 | OK — all tabs tabulated |
| REST API (`api/`) | — | 066 | OK |
| SSH Shell | — | 064 | OK |

## Reached from buttons, not the menu

| Page | Reached from | Chapter | Status |
|---|---|---|---|
| PipeWire routing matrix / graph / audio / video / input mixing / video inputs | Settings → Audio/Video | 116 | OK |
| AES67, Opus RTP, Sound Card Aliases | Settings → Audio/Video | 116 | OK |
| Flash storage (`flash-storage.php`) | Settings → Storage | 020 | OK |
| Grow Filesystem / New Partition | Settings → Storage | 020 | OK |
| Reset FPP Config (`resetConfig.php`) | Settings → System | 020 | OK |
| Cape firmware upgrade (`upgradeCapeFirmware.php`) | Cape Info, Pixel Strings | 064 | OK |
| MP3Gain (`run_mp3gain.php`) | File Manager → Audio | 034 | OK |
| Initial Setup (`initialSetup.php`) | first boot | 006 | OK |
| FPPOS upgrade (`upgradeOS.php`) | System Upgrade | 064 | OK |

`cronjobs.php` exists in the tree but nothing links to it — not documented, deliberately.

## Modal / dialog coverage

Configuration that lives in a dialog rather than on the page itself. Each is
described in the chapter shown, and the ones carrying real configuration options
are also screenshotted.

| Dialog | Opened from | Chapter | Shot |
|---|---|---|---|
| Configure / Edit GPIO Trigger | GPIO Inputs → Add / Edit | 060 | `gpio-edit-modal.png` |
| FPP Command Editor | anywhere a command is chosen | 026 | `command-editor-modal.png` |
| Run FPP Command | bottom bar, every page | 026 | `run-command-popup.png` |
| Playlist entry (New / Edit Entry) | Playlists → Add a Sequence/Entry | 036 | `playlist-entry-modal.png` |
| Reset FPP Config | Settings → System | 020 | `reset-config-modal.png` |
| Edit User-Defined Holidays | Scheduler → Edit Holidays | 038 | `holiday-editor.png` |
| Start Effect | Effects → Start | 028 | `start-effect-modal.png` |
| Schedule Preview: Calendar View | Scheduler / Status → Preview | 038 | `schedule-calendar.png` |
| Overlay model / submodel preview | Pixel Overlay Models | 058 | `pov-*-preview.png` |
| Add New Interface, Create Persistent Names | Network → Interface Settings | 016 | described in text |
| Sequence Info / Video Info | File Manager → Sequences / Video | 034 | described in text |
| Plugin detail | Plugins → a plugin card | 042 | described in text |
| Confirmations (Reboot, Shutdown, Delete Playlist, plugin install/uninstall, Save & Apply Audio) | various | — | not screenshotted; they only confirm an action |

Modal shots are reproducible: `tools/shotlist.txt` opens each one with a
`js_after_load` expression and a clip height. Two depend on this device's data —
the playlist entry dialog names a playlist, and the GPIO dialog edits an existing
trigger — and are commented as such.

## Networking chapters

The four common show-network layouts each now have their own chapter, alongside
an overview chapter covering IP/subnet basics and static routes:

| Topic | Chapter |
|---|---|
| Networking Overview (subnetting, key rules, static routes) | 108 |
| Standalone | 110 |
| Home Network | 112 |
| Separate Network | 114 |

Player/Remote layout (MultiSync) is covered in the [MultiSync](#multisync)
chapter (018) rather than as a fifth Networking chapter, since that page already
documents transport choice (Multicast/Broadcast/Unicast) in full.

## Settings coverage

Every setting FPP actually renders on a settings page is described in chapter 020
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
