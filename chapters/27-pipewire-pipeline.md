# The PipeWire Audio & Video Pipeline

FPP 10 replaces the simple audio/video handling of the 9.x series with a flexible
pipeline built on **PipeWire** (the audio/video graph), **WirePlumber** (which
links the graph together) and **GStreamer** (which decodes media and handles
network streaming). This lets FPP route one audio or video source to **multiple
simultaneous outputs**, each with its own volume, delay, equalisation and format —
and to send and receive audio and video over the network.

Everything in this chapter is reached from the buttons on **FPP Settings →
Audio/Video** (with **Media Backend** set to **PipeWire (Advanced)**). Each page
runs live against the PipeWire graph; most have **Save** and **Save & Apply**
buttons (Apply regenerates the pipeline and re‑links it).

> **Key concepts.** An **output group** is a "combine sink" that fans one signal
> out to several destinations. An **input group / mix bus** collects one or more
> sources and routes them to output groups. The **routing matrix** connects inputs
> to outputs. These apply to both **audio** and **video**.

## Sound Card Aliases

*Audio/Video → Configure Sound Card Aliases.*

![Sound Card Aliases.](images/sound-card-aliases.png)

Audio devices have long, cryptic system names (for example
`usb-Creative_Technology_Ltd_Sound_Blaster_Play__3...`). This page lets you give
each card a short, friendly **alias** (e.g. "Stu Blaster") that is then used
throughout the audio pages, making groups much easier to configure.

## Audio Output Groups

*Audio/Video → Configure Output Audio Groups.*

![PipeWire Audio Output Groups, with per‑card channel mapping, delay and parametric EQ.](images/pw-audio.png)

An **audio output group** is a virtual sink that plays the same audio through
several sound cards at once. Click **Add Group**, name it, and add the sound cards
that belong to it. For the group you set:

- **# of Channels Group Accepts** – e.g. *2ch (Stereo)* or *8ch (7.1)*.
- **Latency Compensation** – align outputs that have different latencies.
- A group **volume**.

For each **sound card** in the group:

- **Sound Card** – chosen by its alias.
- **Card Channels** – how many channels the card provides.
- **Channel Mapping** – map each group channel to a card channel (e.g. `FL → FL`,
  `FR → FR`, `LFE → LFE`), so you can send, say, only the left channel to one card.
- **Volume**, **Delay (ms)** – per‑card level and delay (delay is very useful to
  time‑align distant speakers or compensate for network/receiver latency).
- **Rate / Period** – sample‑rate and buffer period (usually **Auto**).
- **Parametric EQ** – enable per‑card EQ and **+ Band** to add bands, each with a
  **Type** (Low Shelf, Peaking, High Shelf), **Frequency (Hz)**, **Gain (dB)** and
  **Q**.

**Add Sound Card** adds another member; **Sync Calibration** helps measure and set
the per‑card delays.

## Input Mixing (Mix Buses)

*Audio/Video → Configure Input Mixing.*

![PipeWire Input Mixing — input groups and their sources.](images/pw-input-mixing.png)

An **input group** (mix bus) gathers one or more audio **sources** and routes them
to output groups. For each input group you set its name, whether it is **Enabled**,
and its channel count, then add sources. Each source has a **Type** (e.g. *fppd
Stream*), a **Source** (e.g. *FPP Media Stream 1*), a **Name**, a **Volume** and a
**Mute** control. Tick the **Route to Output Groups** boxes to send the mixed
result to the chosen output groups (or open the **Routing Matrix** for a grid
view).

## Routing Matrix

*Audio/Video → Open Routing Matrix.*

![The Routing Matrix — audio input×output grid with per‑path volume, input‑group EQ, and video routing.](images/pw-routing-matrix.png)

The **Routing Matrix** is the single place to connect everything:

- **Audio Routing** – a grid of **Input Groups** (rows) against **Output Groups**
  (columns). Tick a cell to route that input to that output, with a **per‑path
  volume** slider for each connection.
- **Input Group Effects (EQ)** – enable EQ on an input group and add bands.
- **Video Routing** – a grid of **Video Sources** against **Video Output Groups**;
  select which source feeds each video group.
- **Routing Presets** – save a complete routing configuration (audio *and* video
  assignments) by name and reload it later.

Click **Save & Apply** to activate the routing.

## Pipeline Graph

*Audio/Video → Visualise Current Pipeline.*

![The live PipeWire pipeline graph.](images/pw-graph.png)

This page draws the **live PipeWire graph** — the media streams, combine sinks,
filter chains (delay/EQ), sound cards and video nodes, and the links between them.
Producers and consumers are colour‑coded. It is a valuable troubleshooting view for
confirming that audio and video are flowing where you expect.

## AES67 Audio‑over‑IP

*Audio/Video → Configure AES67 Instances.*

![AES67 Audio‑over‑IP configuration: the global PTP clock settings above a send and
a receive instance.](images/aes67-config.png)

**AES67** streams uncompressed, PTP‑synchronised audio over the network as
multicast RTP — the professional standard used by many consoles, DSPs and powered
speakers. Each **AES67 instance** you define appears in the PipeWire graph as a
virtual sink (Send) or a virtual source (Receive), so you can add it to an audio
output group and per‑card **delay and EQ apply to it too**. FPP announces streams
via SAP and derives RTP timestamps from a PTP clock, so compliant receivers
discover and lock to them automatically.

Click **Add AES67 Instance** to create one, and **Save & Apply** to rebuild the
pipeline. The page requires **Media Backend** to be set to **PipeWire (Advanced)**;
otherwise it shows a notice instead of the settings.

### Stream status

The status line at the top of the page reports PipeWire's state, **how many of the
configured streams are actually running**, the PTP clock state, and how many AES67
streams have been **discovered** on the network. It refreshes every ten seconds, so
it is worth watching for the first minute after FPPD starts — PTP moves from
*listening* to master or follower as the clock election settles.

### PTP clock synchronisation

**PTP** (IEEE 1588 Precision Time Protocol) provides sample‑accurate clock
synchronisation between AES67 devices. These settings apply to the whole device,
not to a single instance:

- **Enable PTP** – run the PTP clock. Enable it when you need tight sync between
  several FPP instances or with professional AES67 gear.
- **Network Interface** – which interface the PTP clock runs on. Choose the wired
  Ethernet interface; **(Default)** uses the system's primary route.
- **Domain** – the PTP domain number, **0–127**. Every device that must share a
  clock has to be on the same domain. AES67 gear normally uses domain **0**, so
  leave this alone unless your console or DSP is set otherwise.
- **Clock Role** – who provides the clock:
    - **Auto (prefer other devices)** – the default. FPP joins the election at a
      low priority: it becomes the clock when it is the only device on the domain,
      but yields to a console or DSP that wants the role.
    - **Follower only (never master)** – FPP never becomes the clock.
    - **Prefer master** – FPP tries to win the election. Use this only if FPP is
      meant to be the master clock for the network.

Once PTP is running the status line shows either **PTP master (this device)**, or
**PTP synced to** the grandmaster's clock ID together with the current offset
(shown in ns, µs or ms as it settles). If it has not locked yet you get **PTP not
synced** plus the port state, which is normal for the first few seconds.

> **Tip:** If FPP keeps announcing itself as the clock when you have a proper
> master on the network, check that both are on the same **Domain** and set FPP's
> **Clock Role** to *Follower only*.

> **Note:** FPP marks its own traffic for QoS automatically — RTP audio as **AF41**
> (DSCP 34) and PTP messages as **EF** (DSCP 46), the codepoints AES67 recommends.
> There is nothing to configure. If the installed PTP software is too old to accept
> DSCP settings, FPP retries without them and notes it in the log.

### Per‑instance settings

Each instance has a checkbox to enable it, an editable name, a badge showing the
PipeWire node it creates, and a delete button. Its settings are:

- **Stream Mode** – **Send (Transmit)**, **Receive**, or **Both (Send &
  Receive)**. Send creates a virtual sink; Receive creates a virtual source.
- **Multicast IP Address** – the multicast group, from the AES67 `239.69.x.x`
  range. Give each instance its own address to avoid conflicts.
- **RTP Port** – the UDP port for RTP traffic; the AES67 default is **5004**. Use
  different ports if several instances share one multicast address.
- **Audio Channels** – channels in this stream (standard AES67 allows up to 8;
  most setups use 2).
- **Network Interface** – the interface used for the multicast traffic. Wired
  Ethernet gives the best results.
- **Packet Time (ptime)** – the packetisation interval: **1 ms** (lower latency,
  more CPU) or **4 ms** (the default, more widely compatible). It must match at
  both ends.
- **Session Name** – the name other devices see in the SAP announcement.
- **Network Latency** – the target buffer for *receive* streams, in milliseconds
  (AES67's minimum is 1 ms; 1–20 ms is typical). Lower means less delay but more
  risk of dropouts on a busy network.
- **SAP Discovery** – announce sent streams, and auto‑create receive streams from
  announcements heard on the network.

## Opus RTP Audio Streaming

*Audio/Video → Configure Opus RTP Instances.*

![Opus RTP audio streaming configuration.](images/opus-rtp-config.png)

**Opus RTP** streams **compressed** (Opus‑encoded) audio over the network — far
lower bandwidth than AES67 and tolerant of packet loss, which makes it the right
choice for WiFi links and for remote players or listeners. Like AES67, each
instance appears in the PipeWire graph and can be used in the audio routing.

Use **unicast** (the receiver's own IP address) over WiFi: most access points send
multicast at the lowest data rate with no retransmission. On wired networks both
unicast and multicast (`239.x.x.x`) work well, and multicast lets one sender feed
several receivers.

The status line next to the PipeWire indicator shows **how many of the configured
streams are running**, along with the error text for any pipeline that failed to
start; it refreshes every ten seconds. Previously the page reported only PipeWire's
own state, so a stream that never started looked the same as a healthy one.

Each instance has:

- **Stream Mode** – **Send (Transmit)**, **Receive** or **Both**.
- **Destination IP** – the receiver's IP for unicast, or a shared multicast group
  address for wired multicast.
- **RTP Port** – the UDP port; the default is **5005**.
- **Audio Channels** – Opus handles mono and stereo natively; higher counts use
  multiple Opus streams.
- **Network Interface** – the interface to send or receive on (e.g. `wlan0` with
  unicast, `eth0` for either).
- **Bitrate** – 32 kbps to 320 kbps; **128 kbps** is the default and is ample for
  stereo music, while 64–96 kbps copes where bandwidth is tight.
- **Jitter Buffer** – receive‑side buffering in milliseconds: around 50 ms for
  wired unicast, 100–150 ms for WiFi unicast, more again if you must use WiFi
  multicast. Higher values add delay but ride out network timing variations.
- **Forward Error Correction** – Opus in‑band FEC, which adds redundancy so lost
  packets can be reconstructed. Recommended on WiFi.
- **Discontinuous Transmission (DTX)** – send fewer packets during silence to save
  bandwidth, at the cost of slight artefacts when audio resumes.
- **Expected Packet Loss** – tunes the FEC encoder for the loss rate you expect;
  5% is typical for WiFi, 0–1% for wired.

> **Note:** Opus RTP audio is marked **AF41** (DSCP 34) automatically, so switches
> and access points that honour QoS give it priority over bulk traffic.

## Video Output Groups

*Audio/Video → Configure Video Output Groups.*

![PipeWire Video Output Groups.](images/pw-video.png)

A **video output group** fans a single video stream out to several destinations at
once. (The primary HDMI display is always driven directly by GStreamer for
zero‑latency output; these groups handle *additional* outputs routed through the
PipeWire graph.) For each group set a name, the **Video Source** (Media Playback,
or a persistent input source), optionally which **Stream Slots** (1–5) it uses,
then add outputs. Each output has:

- **Output Type** – **HDMI Display**, a **Pixel Overlay** model, or a **network
  (RTP)** stream.
- **Destination** – the specific HDMI connector, overlay model, or network address.
- **Options** – scaling such as **Fit**.

This is how you drive a second HDMI screen, mirror video onto an LED matrix (via an
overlay model), and stream video over the network — all from one playing video.

## Video Input Sources

*Audio/Video → Configure Video Input Sources.*

![PipeWire Video Input Sources.](images/pw-video-inputs.png)

**Video input sources** are persistent video producers that video output groups can
route from (they survive consumers connecting and disconnecting). Supported types
include:

- **Test Pattern** (`videotestsrc`) – e.g. SMPTE bars at a chosen size/frame rate.
- **USB Camera** (`v4l2src`) – a connected camera device (`/dev/video0`, …).
- **IP Camera** (`rtspsrc`) – an RTSP stream from a network camera.

Define a source here, then select it as the **Video Source** of a video output
group to send a live camera or test pattern to HDMI, an overlay model, or the
network.

## A note on remote synchronisation

When FPP runs as a **remote**, the GStreamer pipeline continuously fine‑adjusts its
playback rate to converge on the player's position, keeping audio and video
frame‑accurate over long shows. This is automatic; the *remoteIgnoreSync* setting
disables it if ever needed. See the [MultiSync](#multisync) chapter for the player/remote
setup.

> **Note:** This chapter covers the configuration UI. The full technical
> architecture (services, WirePlumber linking, GStreamer pipelines, diagnostics)
> is documented in the FPP repository under `docs/FPP_Audio_Architecture.md`,
> `docs/PipeWire_Video_Routing.md` and `docs/GStreamer_PipeWire_Clock_and_Sync.md`.
