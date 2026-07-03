# FPP Quick Start Guide

This section gives you the basic configuration to get up and running. It may not
be the ultimate configuration you need for your finished show — refer to the rest
of this manual, and in particular *General Overview and Navigation*, for in‑depth
explanations of each function and setting.

The essential steps are:

1. **Prepare the hardware** – gather a supported board, a suitable micro‑SD card
   and power supply (see *Hardware Needed*).
2. **Write the FPP image** to the SD card (see *Installing the FPP Software*).
   The easiest route is the **Raspberry Pi Imager**, which can download the
   correct FPP image for you.
3. **Boot and connect** – insert the card, power on, and browse to
   `http://fpp.local/` (or the device's IP address). The first boot takes a few
   minutes while the filesystem expands.
4. **Set the network** – give the device a fixed IP (or a router reservation) and
   a memorable host name (see *Initial Network Configuration*).
5. **Choose the mode** – set **FPP Mode** to **Player** for your main controller,
   or **Remote** for a follower (see *The Status Page* and *MultiSync*).
6. **Set the time zone** – on *FPP Settings → Localization*, so schedules run at
   the right time.
7. **Configure your outputs** – tell FPP how your lights are connected on
   *Input/Output Setup → Channel Outputs*.
8. **Add content** – upload sequences and media on *Content Setup → File
   Manager*.
9. **Build and schedule a playlist** – create a playlist on *Content Setup →
   Playlists* and set it to run on *Content Setup → Scheduler*.

Each of these steps is covered in detail in the chapters that follow.
