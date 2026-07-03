# FPP v10 Manual — Chapter Outline

Structure mirrors the v10 web UI navigation (Status/Control, Content Setup,
Input/Output Setup, Help) with front-matter chapters for newcomers.

Each chapter is a numbered file in `chapters/`. `build/build.sh` concatenates
them in filename order and renders `FPP_Manual_v10.docx` via Pandoc.

| # | File | Chapter | Primary screenshots |
|---|------|---------|---------------------|
| 0 | `00-frontmatter.md` | Title, licence, "What's new in v10" | — |
| 1 | `01-introduction.md` | What FPP is, player vs. remote, supported hardware & protocols | status.png |
| 2 | `02-getting-started.md` | Imaging the SD card, first boot, initial setup wizard, connecting | (imager — placeholder), initialSetup |
| 3 | `03-status-control.md` | Status page, player controls, volume, packet stats, Run FPP Command | status.png |
| 4 | `04-network.md` | Network config: wired/Wi-Fi, DHCP/static, hostname, DNS | network.png |
| 5 | `05-fpp-settings.md` | All Settings tabs (Playback, A/V, Localization, UI, Email, MQTT, Privacy, I/O, Logging, Services, Storage, System, Developer) + UI levels | settings-*.png |
| 6 | `06-multisync.md` | Player/remote sync, discovery, remotes table, MultiSync options | multisync.png |
| 7 | `07-channel-outputs.md` | E1.31/DDP/ArtNet/KiNet, Pixel Strings, LED Panels, PWM, Other | channel-outputs.png + sub-tabs |
| 8 | `08-channel-inputs.md` | E1.31/DDP/ArtNet bridge inputs | channel-inputs.png |
| 9 | `09-output-processors.md` | Remaps, colour order, brightness, gamma, etc. | output-processors.png |
| 10 | `10-pixel-overlay-models.md` | Overlay models, sub-models, virtual display use | pixel-overlay-models.png |
| 10a | `57-virtual-display-3d.md` | New v10 true‑3D virtual display: enabling the output, orbit controls, URL params, standalone mode, 3D asset upload | virtual-display-3d.png (needs 3D output + xLights map) |
| 11 | `11-gpio-inputs.md` | GPIO input triggers | gpio-inputs.png |
| 12 | `12-file-manager.md` | Uploading sequences, media, images, upload from xLights | filemanager.png |
| 13 | `13-playlists.md` | Creating playlists, entry types, playlist editor | playlists.png |
| 14 | `14-scheduler.md` | Schedule entries, repeats, sun-based times, granular scheduling | scheduler.png |
| 15 | `15-command-presets-effects.md` | Command presets, effects, testing | command-presets.png, effects.png, testing.png |
| 16 | `16-plugins-packages-scripts.md` | Plugin manager, packages, script repo browser | plugins.png, packages.png, scriptbrowser.png |
| 17 | `17-backup-restore.md` | FPP Backup/restore, proxies | backup.png, proxies.png |
| 18 | `18-help-troubleshooting.md` | System Upgrade/about, Help, System Health Check, Troubleshooting, Credits | about.png, system-health.png, troubleshooting.png |
| A | `90-appendix-cape.md` | Capes & Current Monitor (cape hardware required — screenshots pending) | (placeholder) |
| B | `91-appendix-protocols.md` | Protocol reference, ports, API pointer | — |

## Notes / decisions
- Screenshots captured at 1440px wide from the running v10 instance (`v10.x-master`), dark theme, UI level = Developer (shows all settings with level markers 🎓/🧪/</>).
- Cape-dependent pages (Cape Info, Current Monitor, per-cape string ports, PWM on real hardware) get placeholders to fill on a cape-enabled machine later.
- Where a v9 concept is unchanged, we still re-shoot to reflect the new v10 header/theme/layout.
