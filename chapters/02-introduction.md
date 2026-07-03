# Introduction

The **Falcon Player (FPP)** is a lightweight, optimised, feature‑rich sequence
player designed to run on low‑cost Single Board Computers (SBCs). It was
originally created to run on the $35 Raspberry Pi — hence the middle 'P' in the
short name — but FPP now supports many more systems. The "FPP" shorthand is still
used, but the software is now simply called **Falcon Player**. FPP is a software
solution that you download and install onto hardware which can be purchased from
numerous sources around the internet.

FPP aims to be controller‑agnostic: it can output **E1.31**, **DDP**, **DMX**,
**Pixelnet**, **Renard** and many other output types to hardware from multiple
vendors. This includes controller hardware from Falcon Christmas
(`http://pixelcontroller.com`) and Kulp Lights (`http://kulplights.com`), as well
as others.

Up until the end of the 2015 Christmas season, most users ran FPP on the
Raspberry Pi as the main player. Since then it has expanded, with the BeagleBone
series of SBCs being widely used as well.

FPP can interface to a number of controllers. It can also play synchronised audio
(via an audio port / FM transmitter) and synchronised video (via HDMI), it
supports USB devices and external interfaces via the GPIO bus, and it can drive
pixels directly via the GPIO bus. Many people use FPP as the show player by
connecting it to one or more DDP/E1.31/DMX controllers and running their light
show sequences and audio from it. Others use several FPP‑based controllers
operating in various modes to run their shows, play videos from a remote
projector, control animatronics, or handle outside events — all synchronised to
the main (Player) FPP.

A Raspberry Pi running FPP can be used with a cape to act as a controller for a
small matrix (36 P10 or 15 P5 panels) or 2 strings of pixels using the standard
Raspberry Pi outputs, or 24 strings using the DPIPixels outputs (approximately
1600 pixels per string at 20 fps, or 800 pixels per string at 40 fps; note that
DPIPixels only supports 20 and 40 fps).

> **Note:** The DPIPixels string outputs require a licence to control more than 50
> pixels per port. See the *Pixel Port Licensing* chapter.

The BeagleBone series SBCs have been used extensively with a cape to drive up to
128 P10 or 64 P5 panels (depending on the cape and BeagleBone type — check with
the vendor to determine capacity). The BeagleBone series can also support other
capes and act as a controller, such as the K4‑PB, F8‑B/K8‑B, F16‑B/K16A‑B,
F32‑B/K32A‑B, F8‑PB/K8‑PB, F40D‑PB, K40D‑PB, OctoPlus, and so on.

This manual covers the functional aspects of installing, configuring and
operating FPP — the most popular show player for animated holiday lighting
displays. It has been updated for **FPP version 10**; see *About This Manual →
What's new in FPP 10* for a summary of the changes since the 9.x series.

## Supported hardware

The current version of Falcon Player runs on the following hardware:

- Raspberry Pi 2 Model B
- Raspberry Pi 3 Model B / B+ / A+
- Raspberry Pi 4 Model B
- Raspberry Pi 5
- Raspberry Pi Zero (a micro‑USB hub may be needed for network access)
- Raspberry Pi Zero‑W / Zero‑W2
- BeagleBone Black (Rev C) / Black Wireless
- BeagleBone Green / Green Wireless (Green Wireless is not recommended with capes)
- BeagleBone Gateway
- PocketBeagle / PocketBeagle 2

The philosophy of the FPP developers is to make FPP as easy to install and use as
possible, while still providing much of the flexibility required by a diverse
group of enthusiasts. The FPP software is free to download and use, and is
provided and supported by a number of volunteers.

Please refer to the Falcon Christmas website (`https://FalconChristmas.com`) for
the latest news and discussions. In particular, the FPP forum is a great resource
for help.

## Acknowledgments

FPP exists thanks to the work of a large community of volunteers. This manual
builds on the Falcon Player Manual written by **Rick Harris (Poporacer)** with
contributions from **Mark Amber (Pixelpuppy)**.

FPP's ongoing development is led by a small core team, including **Chris Pinkham
(CaptainMurdoch)**, **Daniel Kulp (dkulp)** and **Stuart Ledingham
(OnlineDynamic)** — now one of the project's most active core developers — along
with the many contributors and users who report issues, test releases and help
one another on the forums. This v10 edition would not have been possible without
them.
