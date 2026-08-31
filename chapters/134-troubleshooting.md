# Troubleshooting {#resources-troubleshooting}

This chapter collects two kinds of troubleshooting information from the
FPP community: warnings you may see on the **Status** page during normal
operation, and problems that come up while installing FPP for the first time.
For the built‑in diagnostic tools (System Health Check, Troubleshooting
Commands, support bundles), see
[Help and Troubleshooting](#help-and-troubleshooting).

## Status page warnings

The [Status page](#status-page) surfaces warnings when FPP detects an abnormal
condition. Some of the messages you may see, and what they usually mean:

- **Multiple Frame Skips During Playback – Likely Slow Network.** Something on
  your network is slowing the data down — usually caused by configuring
  E1.31/DDP outputs on devices that don't actually need them.
- **Could not resolve Host Name "some name here" – disabling output.** Your
  DNS server isn't configured correctly. The configured DNS server address
  needs to point at a device that can actually process DNS requests — most
  computers and SBCs don't run one, but a home router usually does.
- **Repeated frames taking more than 20ms to send to Colorlite.** Usually a
  slow network connection to the Colorlight receiver card.
- **Could not create output type "some output type here". Check Logs for
  details.**
- **Could not initialize output type "some output type here". Check Logs for
  details.**
- **FSEQ Data Block not available – Likely slow storage.** Usually caused by
  storing sequences on a USB drive, or a uSD card that isn't rated Class 10 or
  higher.
- **Could not ping DDP/E1.31 Channel Data Target "some IP address".** Usually
  means the controller at that address is powered off, or isn't configured
  correctly, while FPP is set to output E1.31/DDP data to it.
- **Received DDP/E1.31 data from "some IP address".** Usually means FPP or
  xLights is configured to send E1.31/DDP data to an FPP device that shouldn't
  normally receive it, such as one running in Player or Remote mode.
- **Sequence file /home/fpp/media/sequences/(some sequence here) does not
  exist.** Appears on a Remote that received a sync command to start a
  sequence it doesn't have a copy of.

## Common installation problems

| Symptom | Possible causes | Remedy |
|---|---|---|
| Can't access the FPP device during **USB Tether** installation. | 1. The FPP device has no power.<br>2. (Pi Zero only) The USB cable is in the wrong port.<br>3. The USB cable is faulty.<br>4. Wrong IP address for USB tethering.<br>5. The image on the uSD card is corrupt.<br>6. The uSD card itself is faulty.<br>7. The FPP device doesn't support USB tethering. | 1. Confirm the FPP device is connected via USB and its power indicator is lit.<br>2. The Pi Zero has two USB ports — one is power‑only. Use the one closer to the center of the board, labeled USB (not PWR).<br>3. Some USB cables are charge‑only; use one known to support power *and* data.<br>4. You can't use the device's Host Name over USB tethering — use the tethering IP address instead: `192.168.7.2` on Windows, `192.168.6.2` on Mac/Linux.<br>5. Format and re‑image the uSD card — see [Installing the FPP Software](#installing-the-fpp-software).<br>6. Format and re‑image a known‑good uSD card — see [Installing the FPP Software](#installing-the-fpp-software).<br>7. USB tethering is only supported by Raspberry Pi Zero and BeagleBone devices. |
| Can't access the FPP device during **Network Connection** installation. | 1. The FPP device has no power.<br>2. The Ethernet cable is faulty.<br>3. The Ethernet cable isn't fully seated in the RJ45 jacks.<br>4. The Ethernet cable is in the wrong port on the router.<br>5. The RJ45 connector's pins are damaged.<br>6. You're trying to access the FPP device directly with a keyboard and monitor.<br>7. You're using the wrong Host Name.<br>8. DNS isn't resolving local names.<br>9. The FPP device doesn't have a good network connection.<br>10. The image on the uSD card is corrupt.<br>11. The uSD card itself is faulty. | 1. Check the power connection and confirm the power LED is lit.<br>2. Test the Ethernet cable, or substitute a known‑good one.<br>3. Check that the cable is fully inserted at both ends.<br>4. Make sure the cable is in a LAN port, not the WAN port.<br>5. Visually inspect the pins for damage.<br>6. FPP has no local display — you access its web UI through a browser (e.g. Google Chrome) from another device, not a keyboard/monitor attached directly to it.<br>7. The correct Host Name for a fresh install is `http://fpp/` or `http://fpp.local/`. If you have other FPP devices already on the network, Host Name access may not work — see the next item.<br>8. Some routers won't resolve local host names like `http://fpp`, so you'll need the FPP device's IP address instead. Log into your router's admin page (often on a sticker on the router, or look up the default login for your brand), find the connected‑devices/DHCP table, and look for a device named FPP to get its IP. If you can't access your router, use xScanner in xLights or an IP scanning utility.<br>9. Check your computer's available networks for an entry named FPP — if one exists, the FPP device couldn't join your network; check all cables. Also confirm you aren't on a `192.168.7.x` subnet (the USB‑tether subnet).<br>10. Format and re‑image the uSD card — see [Installing the FPP Software](#installing-the-fpp-software).<br>11. Format and re‑image a known‑good uSD card — see [Installing the FPP Software](#installing-the-fpp-software). |
| Can't access the FPP device during **Wi‑Fi Tether** installation. | 1. The FPP device has no power.<br>2. The FPP device isn't broadcasting the FPP network.<br>3. The FPP network is broadcasting, but you can't connect to it.<br>4. The image on the uSD card is corrupt.<br>5. The uSD card itself is faulty. | 1. Check the power connection and confirm the power LED is lit.<br>2. Make sure the FPP device isn't already connected via Ethernet or USB to anything — it won't broadcast its own Wi‑Fi network while tethered another way. Confirm the device actually has a Wi‑Fi adapter, and that the adapter supports Wi‑Fi tethering (most USB Wi‑Fi adapters don't; the on‑board adapters on Raspberry Pi and BeagleBone wireless models do).<br>3. Your Wi‑Fi adapter likely doesn't support Wi‑Fi tethering — see above.<br>4. Format and re‑image the uSD card — see [Installing the FPP Software](#installing-the-fpp-software).<br>5. Format and re‑image a known‑good uSD card — see [Installing the FPP Software](#installing-the-fpp-software). |

> **Tip:** Most of these installation problems trace back to one of two
> things — a faulty uSD card/cable, or the wrong address for the connection
> method you're using. Re‑imaging a known‑good card and double‑checking the
> address (`192.168.7.2`, `192.168.6.2`, `http://fpp.local/`) resolves the
> majority of them.
