# Installing the FPP Software

Operating‑system files are called **images**. To install FPP you need a program
for "burning" the image to the micro‑SD card, and optionally one for formatting
the card first.

> **Note:** You cannot simply copy the files to the card — the image must be
> written with imaging software.

## Required programs

**An SD card formatter (optional):**

- `https://www.sdcard.org/downloads/` — versions for Windows and Mac.
- `https://gparted.org/` — for Linux systems.

**An image‑writer program:**

- **Raspberry Pi Imager** — can download the FPP image for both Raspberry Pi and
  BeagleBone hardware directly, as part of the installation process.
- **Balena Etcher** (`https://www.balena.io/etcher/`) — Windows, Mac and Linux.
- **dotNet Disk Imager** (`https://sourceforge.net/projects/dotnetdiskimager/`) —
  a good option for Windows; it can also wipe the SD card, so you won't need a
  separate formatter.

> **Note:** On some older BeagleBone Black boards (not other derivatives),
> installing a version of FPP greater than 2.0 for the first time may require
> holding down the boot button (**S2**) while powering up.

## Getting the FPP software

The software is available at `https://github.com/FalconChristmas/fpp/releases`,
where you can download the most current **image file** (not the application
source code). The image file has `.img.zip` in its name.

Image files start with `FPP` and indicate the version and SBC image. Download the
one that matches the SBC you are using:

- **Pi** — for all Raspberry Pi variants.
- **BB64** — for the PocketBeagle 2.
- **BB** — for all other BeagleBone / PocketBeagle variants.

Several releases are listed on GitHub; not all have an image. Scroll down until
you find the first version that provides images.

> **Note:** If you are going to use the Raspberry Pi Imager, you do not need to
> download the image file first.

Depending on your imaging program, you may have to unzip the file before you can
use it (uncommon). If your imaging software cannot write directly from a `.zip`,
make sure you flash the `.img` file, not the `.zip`; if unsure, unzip first.

The three most popular methods are covered below — Balena Etcher, dotNet Disk
Imager, and Raspberry Pi Imager. Use the method for the software you have.

## Formatting the micro‑SD card (optional)

Before writing the image you may format the card to remove any existing
partitions. This is not usually needed with most imaging programs. Insert the
card and do a **Quick Format** using the SD Card Formatter (not the Windows or Mac
file manager).

## Burning with Balena Etcher

1. Open Balena Etcher and click **Select Image**; choose the downloaded image
   file.
2. Make sure the correct SD card is selected as the target.
3. Click **Flash!** (confirm if prompted) and wait for the completion message.

> **Note:** Some users have resolved Balena Etcher errors by running it as an
> Administrator, or by unblocking the image file in its properties.

The written image is not in a format Windows or Mac can read, so you may see an
error after flashing. **Do not** format the card afterwards. Turn the Pi/BB off,
insert the card, and proceed to *Software Installation*.

## Burning with dotNet Disk Imager

1. Open dotNet Disk Imager (allow it to make changes if prompted).
2. *(Optional wipe)* Select your SD card under **Device** and click **Wipe
   Device**; confirm and wait for completion.
3. Choose the downloaded image file via the file icon next to the **Image file**
   box, and select the SD card as the target.
4. Click **Write to Device** (confirm if prompted) and wait for the completion
   message.

As above, do **not** format the card after writing. Turn the device off and
insert the card.

## Burning with Raspberry Pi Imager

The Raspberry Pi Imager is convenient because it downloads the chosen image as
part of the process — you do not need to download the file separately. (Steps
below match Imager 1.8.5; other versions differ slightly.)

1. Open Raspberry Pi Imager. Click **Choose OS** (do not use *Choose Device*).
2. Select **Other specific‑purpose OS**, then **FPP OS**.
3. Choose the FPP version to image — the most current is recommended — matching
   your device (**Pi** or **BBB**).
4. Click **Choose Storage** and select your SD card, then click **Next**.
5. Click **Yes** to accept overwriting the card, and wait for the progress page.

> **Note:** If you are asked that the SD card is "not readable" and whether to
> format it, **do not** select yes.

When finished, click **Continue** and proceed to *Software Installation*.

## Software Installation

FPP is configured from a web interface — you do not need to connect a monitor to
the device. You access it from a web browser on another computer.

> **Note:** Google Chrome is recommended. Some versions of Internet Explorer /
> Microsoft Edge have had trouble displaying the interface correctly.

Before you begin, decide how the device will ultimately connect to your network —
Wi‑Fi, Ethernet, or (in a few cases) both — and make sure the appropriate
connection or adapter is fitted first. You will also need to know your home
router's IP address (commonly `192.168.0.1` or `192.168.1.1`, among others).

> **Important:** If your home router uses a subnet of `192.168.6.x`,
> `192.168.7.x` or `192.168.8.x`, FPP will likely have communication problems —
> these are the default subnets used by Windows, Mac and Linux for USB tethering
> and by FPP's Wi‑Fi tether, and can conflict. Change your home network to a
> different subnet to avoid problems.

There are three basic ways to install and configure FPP:

- **USB Tethering** — probably the easiest method: connect your computer directly
  to the device with a USB cable. Only a few devices support it: Raspberry Pi
  Zero W, BeagleBone Black, PocketBeagle, BeagleBone Green, and BeagleBone Green
  Gateway. (The PocketBeagle 2 does **not** support USB tethering.)
- **Network Connection** — connect the device to your **router** with an Ethernet
  cable (not directly to your computer). Any Pi or BeagleBone with an Ethernet
  port or adapter can use this method.
- **Wi‑Fi Tethering** — for devices with Wi‑Fi tethering capability (on‑board or
  via a supporting adapter), useful when no other method is available.

> **Warning:** If you are using the KulpLights **K4‑PB v2.0** or **K40‑PB v3.0**
> (produced in 2022), do **not** use USB tethering — it could destroy the USB
> circuitry.

### USB Tethering Installation

> **Note:** If the device needs a network adapter for its final connection, fit
> it before you start (e.g. a PocketBeagle you will later connect via Wi‑Fi).
> Some capes draw more current than a USB connection can provide — you may need to
> remove the cape before connecting the USB cable.

1. Make sure the SD card with the correct image is inserted.
2. Fit any network adapters you will need for your final configuration.
3. Connect one end of the USB cable to your computer. (Do **not** also connect a
   power supply to the device.)
4. On some older BeagleBone Black boards, for the first install you may need to
   press and hold the **S2** button (near the SD card) and hold it for 5 seconds
   after connecting.
5. All other devices — plug the USB cable into the device. (On the Pi Zero, use
   the **USB** port, not the power‑only port.)
6. Wait about one minute (a Pi Zero may take slightly longer).
7. Open a browser and go to `192.168.7.2` (Windows) or `192.168.6.2` (Mac/Linux).
   For a PocketBeagle 2 the tether IP is `192.168.7.2` on all computers.
8. Continue to *Initial Configuration*.

### Network Connection Installation

> **Note:** Some capes have RJ45 ports that are **not** Ethernet — they are for
> DMX or differential receivers and cannot be used for setup. Fit any required
> network adapter before starting.

1. Insert the SD card with the correct image.
2. Fit any network adapters you will need.
3. Connect the Pi/BB to your router with an Ethernet cable.
4. On some older BeagleBone Black boards, hold **S2** for 5 seconds after
   connecting power for the first install.
5. All other devices — connect power.
6. Wait about one minute.
7. Browse to `http://fpp/` or `http://fpp.local/`. (If you cannot connect, see the
   *Help and Troubleshooting* chapter.)
8. Continue to *Initial Configuration*.

### Wi‑Fi Tethering Installation

Use this if your device supports Wi‑Fi tethering, or to make changes when the
device cannot otherwise connect to your network (without re‑imaging). You need a
computer with a wireless connection.

1. Insert the SD card with the correct image.
2. Fit any network adapters you will need.

   > **Note:** Many USB Wi‑Fi adapters do **not** support Wi‑Fi tethering
   > (on‑board Wi‑Fi on Raspberry Pis usually does).

3. On some older BeagleBone Black boards, hold **S2** for 5 seconds after
   connecting power for the first install.
4. All other devices — connect power.
5. Wait about one minute.
6. On your computer, connect to the wireless network named **FPP**; the password
   is **Christmas**.
7. Browse to `192.168.8.1`.
8. Continue to *Initial Configuration*.

## Initial Configuration

Once FPP is installed, the **Initial Setup** page provides a convenient place to
configure common or required settings:

- **UI Password** *(required choice)* — whether to set a web‑UI password. This is
  an advanced setting; the recommended choice is **No Password (default)**. See
  *FPP Settings → UI*.
- **OS Password** *(required choice)* — used for SSH and similar access. This is
  an advanced setting; the recommended choice is **falcon (Default)**. See *FPP
  Settings → System*.
- **FPP Player Mode** — set the mode this device will run in. If unsure, leave it
  at **Player**. See *The Status Page → FPP Mode*.
- **Host Name** — a meaningful name for this device. See *Network → Host
  Settings*.
- **Installed Cape/Hat** — if your device has a cape/hat with no EEPROM, define
  the Virtual EEPROM here. See *Pixel Port Licensing*.
- **Share Crash Data with FPP Developers** — helps developers find and fix crash
  bugs. The recommended setting is *Include settings and configurations*. See
  *FPP Settings → Privacy*.
- **Email Address** — if you share crash data, providing an email lets the
  developers follow up if needed.

After completing initial setup, work through the *Initial Network Configuration*
and the rest of this manual to finish setting up your show.
