# About This Manual {-}

This manual describes **Falcon Player (FPP) version 10**. FPP 10 introduces a
significant number of changes over the 9.x series, including a refreshed user
interface, a reorganised Settings page, a new audio/video pipeline based on
PipeWire and GStreamer, and expanded MultiSync and health‑monitoring features.

The screenshots in this manual were taken from a running FPP 10 system. Your
screens may differ slightly depending on your hardware platform (Raspberry Pi,
BeagleBone, or a generic Linux/Docker host), the capes or hats you have
installed, and your **UI Level** setting (see the *FPP Settings → UI* section).
Screens that require specialised cape hardware are noted where they appear.

> **Tip:** Press **F1** on any FPP page to open context‑sensitive help.

## Conventions used in this manual {-}

- **Bold** text indicates on‑screen buttons, menu items, tab names, and settings.
- Menu paths are written as **Menu → Sub‑item**, e.g. **Status/Control → FPP Settings**.
- Notes and warnings are called out in indented blocks.

## What's new in FPP 10 {-}

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
  device. See the *Protocols, Ports and the API* appendix.

Each of these areas is covered in detail in the relevant chapter.
