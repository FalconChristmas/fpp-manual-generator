# Help and Troubleshooting

The **Help** menu gathers FPP's information, upgrade, support and diagnostic tools.

## System Upgrade (About)

The **About** page (**Help → System Upgrade**) shows the current FPP version and
statistics about the running system, and is where you perform a manual update.

![The System Upgrade / About page.](images/about.png)

### Version Info

- **FPP Version** – the current FPP version.
- **Platform** – the SBC platform of this device.
- **FPP OS Build** – the current OS build. The OS should match the requirement for
  the FPP version (see the release notes or the *Upgrade OS* drop‑down).
- **OS Version** – the SBC base OS version; some capabilities need the OS upgraded
  to match the build.
- **Hardware Serial Number** / **Kernel Version** – device identifiers.
- **System Boot Time** / **fppd Uptime** – when the device booted and how long the
  daemon has run (restarting fppd resets this).
- **Local Git Version** – the installed version (with a **ChangeLog** link and an
  update indicator).
- **Remote Git Version** – the latest available version; *Unknown* means no
  internet (often a network/DNS problem). A **Preview Changes** link shows what an
  update provides.

### Upgrade FPP

A minor update (same branch) is indicated on the Local Git Version and by an icon
in the header; click **Upgrade FPP** to install it. A major upgrade requires an OS
update. Options include:

- **FPP Upgrade Source** – upgrade from GitHub or from another of your FPP devices
  (useful when some devices have no internet); the chosen source is also used for
  upgrades launched from the MultiSync page. *(Advanced.)*
- **Upgrade OS** – select an FPPOS version to download (or download and upgrade).
  With internet access the list includes the currently supported FPPOS files.
- **Show All Platforms** – view/download files for other platforms, e.g. to act as
  an upgrade source for Pi *and* BB devices. *(Advanced.)*
- **Show Legacy OS's** – show older, deprecated versions.
- **Preserve /opt/fpp** – when already on master and newer than the fppos image,
  upgrade the OS without downgrading FPP from master. *(Developer.)*

**Upgrade methods:** **from GitHub** (updates to the newest version of the current
branch), **from another FPP** (matches another device's FPP version, not the OS;
Advanced), or **from FPPOS** (an in‑place upgrade of both FPP *and* OS without
re‑imaging — download the appropriate `.fppos` and upload it; requires being on at
least 5.5‑24 first). Major branch/OS changes otherwise require a re‑image.

> **Warning:** Always take an **FPP Backup** before upgrading.

Below Version Info the page also shows **System Utilization**, **Player Stats** and
**Disk Utilization** for the device.

## Cape Info

If a cape/hat is installed, **Help → Cape Info** shows information about it and
lets you upgrade or sign the EEPROM.

![The Cape Info page.](images/cape-info.png)

The page has four tabs:

- **About** – **Name**, **Version**, **Serial Number**, **Designer**, **Licensed
  Outputs** (and licence status), **Output Driver**, and **Vendor Name/URL/E‑mail**.
- **EEPROM Signature** – sign your EEPROM once you have an **Order number** and
  **License Key** for the pixel‑string outputs (see *Pixel Port Licensing*). This
  is also where **Off‑Line Signing** is done, for a device with no internet access
  (see *Pixel Port Licensing → Off‑Line Signing*).
- **Voucher Redemption** – redeem a voucher from your vendor or
  shop.falconplayer.com to sign your EEPROM.
- **EEPROM Upgrade** – upgrade the cape's firmware/EEPROM from a file, or restore
  it from a previous backup. An option lets you **reset the configuration to
  defaults** as part of the restore. FPP streams the progress and keeps the dialog
  open until the flash finishes.

  > **Warning:** Do not power off or reboot the device while a cape firmware
  > flash is running — an interrupted flash can leave the EEPROM unusable.

> **Note:** This page only appears when a cape or hat is detected, so it is absent
> on a bare device. The fields shown vary with what the cape's EEPROM reports.

## Get Help

**Help → Get Help** provides support resources and API references.

![The Get Help page.](images/help.png)

**Places to get help:**

- **FPP Manual** – the current manual (offline copy at
  `https://falconchristmas.github.io/FPP_Manual.pdf`).
- **FPP Facebook Group** and the **Falcon Christmas Forums** – community help.
- **xLights Zoom Room** – often the fastest way to get any lighting question
  answered (not just xLights).

**FPP API:**

- **REST API Help** – a list of endpoints with a test facility, for plugin and
  software developers; click an endpoint to run it and see your device's output.
- **FPP Commands Help** – three sections: **Command Tester**, a **Command List**
  (all commands with typical arguments), and **MQTT Instructions**.

## Credits and Donate

**Help → Credits** lists the people and projects behind FPP. If FPP has been
useful, **Donate to FPP** links to support the developers.

![The Credits page.](images/credits.png)

## System Health Check

The **System Health Check** (**Help → System Health Check**) is a consolidated
dashboard, new in FPP 10, that checks the device and surfaces anything wrong.

![The System Health Check (Health and Status) page.](images/system-health.png)

A **System Health** panel runs checks and summarises them as **Passed / Warnings /
Issues**, including: **FPPD Daemon** and **FPPD Warnings**; **Unique Hostname** and
**Root Filesystem** usage; **Time Sync (NTP)** and **Browser Time Sync**;
**PipeWire Audio** and **GStreamer**; **Scheduler**; and network checks (**Default
Gateway**, **Gateway Reachable**, **Internet Access**, **DNS Resolution**). Use
**Re‑run** to check again. Live panels below show **CPU Usage**, **Memory Usage**,
**Temperature**, **Fan Monitoring** (on devices with a controllable fan — see *FPP
Settings → System*), **Disk Utilization**, **System Uptime**, **System Busyness**
and **Player Statistics**.

> **Tip:** This is the first page to open when something is not working — a red
> **Issue** or amber **Warning** usually points straight at the cause.

## Troubleshooting Commands

**Help → Troubleshooting Commands** runs a set of read‑only system commands and
shows their output on one page — logs, process/service status, network information
and configuration dumps — so you can inspect the device (and copy the output into a
support request) without a shell.

![The Troubleshooting Commands page.](images/troubleshooting.png)

The output is grouped into tabs by subject, so you can go straight to the area you
are investigating:

| Tab | What it shows |
|---|---|
| **Networking** | Interfaces, addresses, routes, DNS and connectivity |
| **Disk** | Mounted file systems, free space and partition layout |
| **Date / Time** | System clock, time zone and time-sync (chrony) status |
| **Memory / CPU** | Memory use, load and processor information |
| **USB** | Connected USB devices — the place to confirm a dongle or adapter was detected |
| **Audio** | Sound cards, ALSA/PipeWire devices and current audio routing |
| **Media Backend** | The media backend's state (PipeWire/GStreamer) |
| **Midi** | Detected MIDI devices |
| **Video** | Video outputs, displays and modes |
| **OS, Kernel, and SD image** | OS release, kernel version and the image FPP was installed from |
| **i2c** | Devices on the I2C bus — useful for OLED displays and capes |
| **Processes** | Running processes, including whether `fppd` is up |
| **Boot** | Boot configuration and boot-time messages |
| **Git** | The FPP source checkout's branch and status |
| **GPIO** | GPIO pin state and configuration |
| **PHP** | The PHP environment behind the web UI |
| **RPI Utils** | Raspberry Pi specific tools — throttling, voltage and firmware |
| **Webserver** | Apache configuration and error logs |

> **Note:** Every command here is **read‑only** — opening a tab inspects the
> device, it does not change anything.

### Download Support Bundle

Rather than copying individual command output by hand, use **Download Support
Bundle (Logs / Config / Troubleshooting)**. It packages the device's logs, its
configuration, the troubleshooting command output and the **System Health Check**
results into a single `.zip` you can attach to a forum post or bug report. FPP
shows progress while the zip is generated, since gathering everything takes a few
moments.

> **Tip:** Attaching a support bundle is the single most useful thing you can do
> when asking for help — it saves a long back‑and‑forth about versions, settings
> and log contents.

> **Note:** A support bundle contains your configuration and logs, which may
> include your host name, network details, Wi‑Fi SSID, file names and email
> settings. Look through it before posting it somewhere public.

## SSH Shell

**Help → SSH Shell** opens a browser‑based shell to the device for advanced users.

## General troubleshooting tips

- **Raise log levels** for the relevant subsystem on *FPP Settings → Logging*,
  reproduce the problem, then read the logs from *File Manager → Logs*.
- **No output?** Check *Channel Outputs* are enabled and saved, that FPPD was
  restarted after changes, and use *Display Testing* to isolate wiring from
  configuration.
- **Audio/video issues?** Check the **PipeWire Audio** and **GStreamer** health
  checks and the *Audio/Video* settings.
- **Sync problems?** Confirm **Send MultiSync Packets** on the player, matching
  sequences on remotes, and a stable (ideally wired) network.
- **Cannot reach FPP?** Most often a network/DNS problem — check the address, host
  name, and the *Network* settings.
