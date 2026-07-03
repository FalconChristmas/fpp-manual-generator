# Hardware Needed

The Raspberry Pi and BeagleBone series SBCs have different requirements and setup
instructions. Follow the instructions for your specific case. These are the
basics to get your device(s) running; depending on your setup you will need
additional items after the initial setup to actually run your show (power supply,
network cables, wiring, and so on).

## Raspberry Pi

**Required items:**

- A supported Raspberry Pi.
- A micro‑SD memory card: 4 GB minimum, Class 10 or better, A1 recommended. 16 GB
  or larger is recommended. (Samsung Evo Select and SanDisk Ultra are
  recommended.)

  > **Note:** Some SanDisk High Endurance U3 cards have been reported as
  > incompatible with recent FPP/OS versions.

- A power supply for the Pi:
    - 5 V DC 2.0 A micro‑USB for the Pi Zero and Pi 2 series
    - 5 V DC 2.5 A micro‑USB for the Pi 3 series
    - 5 V DC 3.0 A USB‑C for the Pi 4 series
    - 5 V DC 5.0 A USB‑C for the Pi 5 series (additional cooling may also be
      needed)

**Optional items:**

- A network cable (if connecting via Ethernet, or to use the Network
  Configuration process).
- A USB‑to‑micro‑USB cable (for devices that support USB tethering; tethering is
  usually the easier process).
- A Wi‑Fi USB adapter if using a Pi without built‑in Wi‑Fi (the Edimax Nano is
  recommended — *not* the V2 version; stick to 2.4 GHz‑only adapters, as some
  5 GHz cards have compatibility issues).
- A cape/hat, if you are using one.

## BeagleBone series (BB)

It is recommended to use the BeagleBone Black, BeagleBone Green, PocketBeagle or
PocketBeagle 2. The BeagleBone Green Wireless cannot be used with capes.

**Required items:**

- A supported BeagleBone SBC.
- A micro‑SD memory card: 4 GB minimum, Class 10 or better; 16 GB or larger
  recommended. (Samsung Evo Select and SanDisk Ultra are recommended.)
- An appropriate power supply.
- Depending on your controller (typically PocketBeagle‑based), a wireless USB
  adapter or USB Ethernet adapter may be required to connect FPP to your network.
  (The Edimax Nano is recommended. Some older Wi‑Fi adapters that worked with
  older Linux versions are no longer supported.)

**Optional items:**

- A network cable (if connecting via Ethernet, or to use the Network
  Configuration process).
- A USB cable — for the USB‑tether install method you need a USB‑to‑mini‑USB
  cable (micro‑USB for a PocketBeagle or BeagleBone Green). USB tethering is
  probably the easiest install method for BeagleBone‑based devices.
- An Octoscroller‑type cape if connecting the BB to P10/P5 panels.
- Another cape, if you are using one.
