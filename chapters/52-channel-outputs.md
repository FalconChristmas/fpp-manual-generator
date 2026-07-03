# Channel Outputs

The **Channel Outputs** page configures how FPP outputs channel data to the
controllers, hats and capes connected to it. Open **Input/Output Setup → Channel
Outputs**. The available tabs depend on your SBC and any attached cape.

![Channel Outputs — the E1.31 / ArtNet / DDP / KiNet tab.](images/channel-outputs.png)

Set up your outputs to match the controller connected to FPP and the settings in
your sequencing software. The output types are:

- **E1.31 / ArtNet / DDP / KiNet** – for controllers connected over Ethernet (or
  a switch). **DDP** is preferred where supported (e.g. Falcon and KulpLights
  controllers with recent firmware, ESP PixelStick). Output over Wi‑Fi is possible
  but not recommended.
- **Pixel Strings** (shown per cape, e.g. *PiHat Pixel Strings*, *K8‑B*) – WS281x
  pixels driven directly by a Pi hat or BeagleBone cape, or from the GPIO pins. FPP
  uses the attached cape's EEPROM to build the correct page; without a programmed
  EEPROM the section is blank and you must install a **Virtual EEPROM** (below). On
  a Pi 5 the pixel‑string type must be the **DPI** protocol.
- **LED Panel Matrices** – P10/P5 panels via a BeagleBone Octoscroller‑type cape, a
  Pi matrix hat, or a ColorLight card.
- **DMX / Serial** – DMX, Pixelnet and Renard over a USB/serial adapter.
- **PWM** – PWM outputs (servos, single‑colour dimming) on supported hardware.
- **Control Signal** – control/trigger signal outputs.
- **Virtuals** – virtual outputs such as the on‑screen 2D/3D virtual display.

> **Changed in v10:** The Channel Outputs screen was redesigned. The old single
> **Other** tab (which held DMX, serial, control and virtual types together) has
> been **removed**, and those outputs now have their own dedicated tabs —
> **DMX/Serial**, **PWM**, **Control Signal** and **Virtuals** — shown according to
> your platform and UI Level.

Use **Add Output Group** to combine outputs so several are treated as one.

## E1.31 / ArtNet / DDP / KiNet

> **Note:** You only need to enable/configure these outputs if this device sends
> pixel data to **external** devices over the network. It does not apply to locally
> attached hats/capes or serial DMX ports.

Your universes, FPP start channels and sizes must match your sequencer and
controller. Using **FPP Connect** in xLights (the **UDP** option under Tools) to
upload the configuration is the recommended method, as it avoids typing errors.

> **Warning:** If you do **not** intend to send E1.31/ArtNet/DDP data but select
> the UDP option in FPP Connect, it will configure **and activate** these outputs,
> which can cause lag/stutter and unexpected results.

- **Enable Output** – enable network output.
- **Sending** – the send strategy *(Advanced)*:
    - **Multi‑Threaded Blocking** *(default)* – multiple threads; send a packet and
      wait for acknowledgement before the next. Uses FPP's multi‑threading for
      better performance.
    - **Single‑Threaded Blocking** – one thread, wait for acknowledgement.
    - **Multi‑Threaded Non‑Blocking** – multiple threads, send the next packet as
      soon as it is ready.
    - **Single‑Threaded Non‑Blocking** – one thread, send as soon as ready.
- **Outputs Count** – the number of output rows, typically one **per controller**
  (even when a controller uses several universes). Click **Set** to create the
  rows.
- **Set / Save / Clone / Delete** – create the rows, save, copy a row to those
  below it, or delete a row.

For each output row:

- **Active** – transmit this line's universes (activate only the outputs you
  actually need).
- **Description** – identify the controller.
- **Output Type** – how the data is sent: **DDP** (recommended where supported),
  **E1.31 Multicast**, **E1.31 Unicast** (more efficient — prefer Unicast for
  E1.31), or **ArtNet**. **DDP** is normally *Raw Channel* numbers; **DDP‑One
  Based** makes each controller start at channel 1 (you must then configure those
  devices to match).
- **Unicast Address** – for Unicast or DDP, the target device's IP.
- **FPP Start Channel** – the absolute channel configured in your sequencer for
  this range.
- **FPP End Channel** – calculated, to help verify your entry.
- **Universe #, Universe Count, Universe Size** – the starting universe, how many
  universes on this line (multiple per line is recommended), and channels per
  universe (commonly 512 or 510 — keep it consistent across your show).
- **Universe Priority** – priority for the E1.31 packets when more than one source
  targets a device.

## Pixel Strings

The Pixel Strings tab (named for the detected cape) configures WS281x pixels wired
to the hat/cape or GPIO. Common controls:

- **Enable (Cape Type)** – enable the pixel‑string output (untick to disable
  without losing the configuration).
- **Cape Config** – the cape type from the EEPROM (some, like the K16, offer
  expansion‑board and serial options).
- **Testing** – output test patterns (stays active until turned off): **Port
  Number** (white pixels at the start of each string indicate its port), **Pixel
  Count by Port**, **Pixel Count by String**, and **Red/Green/Blue/White Fade**.
- **Pixel Timing** – normal **ws281x** or the slower **1903** protocol
  (BeagleBone only).
- **Clone String** – copy a string's settings to others, advancing the start
  channel.

Per port:

- **Port** – the hat's output port; click **+** to add a **virtual string** to a
  port (for different daisy‑chained models needing individual adjustment).
- **Description** – a label for the port.
- **Start Channel** – matches the start channel in your sequencer (highlighted
  orange if there may be an error — hover for details).
- **Pixel Count** – pixels on the port (red if it exceeds the port's capacity).
- **Press F2 to auto set** – fills the next row's start channel for contiguous
  ports.
- **Group Count** – group pixels that always display identically.
- **End Channel** – the ending channel (calculated).
- **Direction** – **Reverse** feeds data as if from the end of the string.
- **Color Order** – match your pixels' colour order.
- **Start Nulls / End Nulls** – number of null nodes used to boost transmission
  distance at each end.
- **Zig Zag** – for props like a mega‑tree where one string feeds several strands;
  enter how many times the string changes direction. Do **not** use this if you set
  Strands/String in your sequencer.
- **Brightness** – lower brightness can look better on dense props and reduces
  power draw.
- **Gamma** – correction for the non‑linear way we perceive brightness, and to
  match pixels from different vendors.

### Configuring the Virtual EEPROM

From FPP 6 onward, the advanced pixel output protocols require an EEPROM. If your
hat/cape has none, configure a **Virtual EEPROM**, choosing the type for your
output. Examples:

- **PiHat** – two ports (two GPIO pins):
    - **PiHat** – uses the same PWM as the on‑board audio, so on‑board audio is
      disabled (a USB audio card still works).
    - **PiHat (DPIPixels – allows onboard audio)** – keeps on‑board audio; limited
      to 50 pixels per port without a licence.
- **DPIPixels‑24** – up to 24 ports without disabling on‑board audio; 50 pixels per
  port without a licence.
- **rPi‑28D / rPi‑MFC** – Hanson Electronics boards.
- **F16‑B / F32‑B / F4‑B / F8‑B / F8‑Bv2 / F8‑PB** – Falcon/Kulp DIY boards.
- **RGB‑123 / PB‑16 / PocketScroller / Spixel** – various boards (Spixel drives 16
  strings of APA102/LPD6803/LPD8806 directly from the Pi GPIO).

Some types offer additional board‑specific options — get the correct EEPROM and
board type from your vendor. If a Virtual EEPROM needs a licence for its advanced
features, a blue banner explains this; the **Cape Info** link opens the *Cape Info*
page with more detail and a link to obtain the licence (see *Pixel Port
Licensing*).

> **Screenshots pending — cape hardware required.** Full captures of the Pixel
> Strings tab need the relevant cape fitted so the ports are shown; these will be
> added from a cape‑enabled system.

## LED Panel Matrices

Configures LED panels (P10/P5 are most common), driven by a ColorLight card or a
connected hat/cape. One FPP device can control multiple drivers; the practical
limit depends on matrix size and the SBC's single‑core speed, so test for
performance.

> **Note:** For any output beyond a hat/cape you need a **dedicated Ethernet port
> for each ColorLight receiver**.

Click **Add Panel Matrix** and choose **Hat/Cape** or **ColorLight** (one Hat/Cape
matrix, but multiple ColorLight panels). There are three settings screens —
BeagleBone Hat/Cape, ColorLight, and Pi Hat/Cape. Common settings:

- **Enable LED Panels** – enable panel output.
- **Interface** – for ColorLight, the dedicated Ethernet port for that receiver.
- **Matrix Name** – names each matrix (shown on its Panel Tab).
- **Panel Layout (WxH)** – number of panels wide × high.
- **Single Panel Size (WxH)** – pixel size and scan rate of each panel (P10 =
  32×16, P5 = 64×32).
- **Model Start Corner** – typically **Top Left** for xLights, **Bottom Left** for
  Vixen (match your sequencer).
- **Panel Gamma** / **Brightness** – gamma correction and overall brightness.
- **Panel Interleave** – for panels using non‑standard data transmission.
- **Color Depth** – number of colours; reduce to minimise flicker on large sets
  (Hat/Cape only; ColorLight uses LEDVision for this).
- **Panel Row Address Type** / **LED Panel Type** – for panels with different row
  addressing or specialty panels (Pi Hat/Cape only).
- **Start Channel** / **Channel Count** – the panel array's absolute start channel
  and total channels.

> **Screenshots pending — cape hardware required.**

## DMX / Serial, PWM, Control Signal and Virtuals

In the redesigned v10 screen these output types each have their own tab (they were
previously combined in a single *Other* tab, which no longer exists):

- **DMX / Serial** – DMX Pro, LOR, Renard and Pixelnet over a USB/serial adapter.
  Select the serial device and protocol and map the channel range to it.
- **PWM** – map channels to PWM pins/outputs (hardware dependent), e.g. for servos
  or single‑colour dimming.
- **Control Signal** – configure control/trigger signal outputs.
- **Virtuals** – virtual outputs such as the 2D/3D on‑screen virtual display.
  Enabling **HTTP Virtual Display 3D** here is what activates the new browser‑based
  3D preview — see the *3D Virtual Display* chapter.

After any change, click **Save** and, when prompted, **Restart FPPD**.
