# About This Manual {-}

This manual covers **Falcon Player (FPP) version 10**. FPP 10 introduces a
significant number of changes over the 9.x series, including a refreshed user
interface, a reorganized Settings page, a new audio/video pipeline based on
PipeWire and GStreamer, and expanded MultiSync and health‑monitoring features.

The screenshots in this manual were taken from a running FPP 10 system. Your
screens may differ slightly depending on your hardware platform (Raspberry Pi,
BeagleBone, or a generic Linux/Docker host), the capes or hats you have
installed, and your **UI Level** setting (see the [FPP Settings → UI](#ui) section).
Screens that require specialised cape hardware are noted where they appear.

> **Tip:** Press **F1** on any FPP page to open context‑sensitive help.

## Conventions used in this manual {-}

- **Bold** text indicates on‑screen buttons, menu items, tab names, and settings.
- Menu paths are written as **Menu → Sub‑item**, e.g. **Status/Control → FPP Settings**.
- Notes and warnings are called out in indented blocks.

## What's new in FPP 10 {#whatsnew -} 

The most visible and important changes since 9.x include:

- **Redesigned UI** – a new top navigation bar grouped into *Status/Control*,
  *Content Setup*, *Input/Output Setup*, and *Help*, with a persistent header
  showing host name, player state, CPU temperature, IP addresses and time.
- **Reorganised FPP Settings** – settings are now split across clearly labelled
  tabs (Playback, Audio/Video, Localization, UI, Email, MQTT, Privacy,
  Input/Output, Logging, Services, Storage, System, Developer). Each setting is
  tagged with a *UI Level* marker so you can choose how much detail to see.
- **New audio/video pipeline** – audio and video routing is now handled by
  **PipeWire** with **GStreamer**, adding audio output groups (per‑output delay
  and EQ), a routing matrix, AES67 and Opus network audio, and video output/input
  groups. This is significant enough to have its own chapter, *The PipeWire Audio
  & Video Pipeline*.
- **Pixel Overlay Model improvements** – a model **preview**, plus support for
  xLights **submodels** and **model groups**, all addressable by name through the
  overlay commands.
- **Improved MultiSync** – faster remote discovery, clearer remote status, and
  more reliable synchronised playback across players and remotes.
- **System Health Check** – a consolidated health page that surfaces warnings
  about storage, services, audio/video, temperature and configuration issues.
- **Expanded plugin and package management** – a reworked Plugin Manager and a
  Packages page for installing optional software.
- **Interactive API explorer** – a built‑in, browsable reference for FPP's REST
  API (**Help → REST API**), letting you inspect and try every endpoint on the
  device. It replaces the old static API help page, and plugins can now document
  their own HTTP routes alongside FPP's. See the *Protocols, Ports and the API*
  appendix.
- **Variables and Recurring Tasks** – FPP can now store named **Variables** and
  act on them: a **Set Variable** command stores values (fixed, counter, random,
  or a calculated expression), an **If** command branches on them, and any
  command's text field can substitute one with `%VAR:name%`. **Recurring Tasks**
  run a command or preset on a repeating interval and can capture its result into
  a variable. Both are on the *Content Setup* menu at the **Advanced** UI level
  and have their own chapter, [Variables and Recurring Tasks](#variables-and-recurring-tasks).
- **Categorized FPP Commands** – the command list is now grouped (Audio, Effects,
  Events, Media, Playlist, Pixel Overlay, Outputs, System) and each command is
  tied to a UI Level, so the Basic level shows only everyday commands. Command
  arguments now carry their own help tooltips.
- **Temporary Advanced UI level** – you no longer have to change your UI Level
  permanently to reach one Advanced setting. A button on [FPP Settings → UI](#ui)
  unlocks the Advanced UI for 15 minutes, with an unlock icon in the header while
  it is active.
- **Reworked Plugins page** – a card/grid layout with plugin icons, categories,
  popularity, live counters and filtering, an *Installed / Available / Updates*
  tab strip, and a single search box that also accepts a `pluginInfo.json` URL.
  Plugins can now be loaded and unloaded without restarting FPP.
- **Playlist improvements** – the entry editor has been redesigned into labelled
  sections with help tooltips, and a media entry can now carry **companion
  media** that lives and dies with it.
- **Calendar view of the schedule** – alongside the weekly preview, the Scheduler
  offers a month/calendar view of what will actually run.
- **Support bundle** – [Help → Troubleshooting Commands](#troubleshooting-commands) can package the logs,
  configuration and health-check data into a single zip to attach to a support
  request.

Each of these areas is covered in detail in the relevant chapter.

> **Note:** FPP 10 continues to be developed after release, so a very recent
> build may show items this manual does not yet describe. The version you are
> running is shown at the top-left of every page and on *Help → System Upgrade*.
