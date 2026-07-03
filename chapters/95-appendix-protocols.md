# Appendix B: Protocols, Ports and the API

## Output and input protocols

| Protocol | Transport | Typical use | In/Out |
|----------|-----------|-------------|--------|
| **E1.31 (sACN)** | UDP multicast/unicast | Ethernet pixel/DMX controllers | Out & In |
| **DDP** | UDP unicast | Efficient Ethernet pixel control (e.g. Falcon, WLED) | Out & In |
| **ArtNet** | UDP | Stage/DMX ecosystems | Out & In |
| **KiNet** | UDP | Color Kinetics gear | Out |
| **DMX** | Serial (USB) | DMX fixtures via USB dongle | Out |
| **Pixelnet** | Serial | Legacy pixel control | Out |
| **Renard** | Serial | Legacy DIY controllers | Out |

Direct **WS281x pixel strings** and **LED matrix panels** are driven through a
cape/hat rather than a network protocol (see *Capes* appendix).

## Common network ports

| Port | Protocol | Purpose |
|------|----------|---------|
| 80 | HTTP | FPP web UI and REST API |
| 5568 | E1.31 (sACN) | Streaming ACN lighting data |
| 6454 | ArtNet | ArtNet lighting data |
| 4048 | DDP | Distributed Display Protocol |
| 32320 / 32328 | FPP MultiSync | Player→remote sync and discovery |
| 1883 | MQTT | Broker connection (configurable) |

(Ports for AES67 and Opus RTP audio streaming are configured on *FPP Settings →
Audio/Video*.)

## The FPP API

FPP exposes a **REST/HTTP API** on port 80 for status and control — starting and
stopping playlists, reading status, setting channel data, controlling overlay
models, and more. The interactive API help is available in the FPP UI (the
`api.php` / API help page), and the same actions are available through
**Commands**, **MQTT** and the **Scheduler**.

## MQTT

When configured (*FPP Settings → MQTT*), FPP connects to an MQTT broker and both
publishes status and subscribes to command topics under a configurable prefix,
making it easy to integrate with home‑automation platforms such as Home
Assistant or Node‑RED. See the FPP MQTT documentation for the full topic list.

## Further resources

- **FPP GitHub:** `https://github.com/FalconChristmas/fpp`
- **FPP releases/downloads:** `https://github.com/FalconChristmas/fpp/releases`
- **xLights** (sequencing): `https://xlights.org`
- **Community support:** the FPP/xLights forums and Facebook groups.
