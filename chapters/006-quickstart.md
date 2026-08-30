# FPP Quick Start Guide

This section gives you the basic configuration to get up and running. It may not
be the ultimate configuration you need for your finished show — refer to the rest
of this manual, and in particular [General Overview and Navigation](#general-overview-and-navigation), for in‑depth
explanations of each function and setting.

The essential steps are:

1. **Prepare the hardware** – gather a supported board, a suitable micro‑SD card
   and power supply (see [Hardware Needed](#hardware-needed)).
2. **Write the FPP image** to the SD card (see [Installing the FPP Software](#installing-the-fpp-software)).
   The easiest route is the **Raspberry Pi Imager**, which can download the
   correct FPP image for you.
3. **Boot and connect** – insert the card, power on, and browse to
   `http://fpp.local/` (or the device's IP address). The first boot takes a few
   minutes while the filesystem expands.
4. **Set the network** – configure the network settings so that you can communicate
   with your devices (see [Initial Network Configuration](#initial-network-configuration)).
5. **Choose the mode** – set **FPP Mode** to **Player** for your main controller,
   or **Remote** for devices that are going to be controlled from another device.
   (see [The Status Page](#status-page) and    [MultiSync](#multisync)).
6. **Set the time zone** – on [FPP Settings → Localization](#localization), so
   schedules run at the right time.
7. **Configure your outputs** – tell FPP how your lights are connected on
   *Input/Output Setup →* [Channel Outputs](#channel-outputs).
8. **Add content** – (If needed) upload sequences and media on *Content Setup →*
   [File Manager](#file-manager).
9.  **Build and schedule a playlist** – create a playlist on *Content Setup →*
   [Playlists](#playlists) and set it to run on *Content Setup →*
   [Scheduler](#scheduler).

Installing the FPP software, initial network configuration, and updating are
covered in detail in the sections below; the rest are covered in their own
chapters elsewhere in this manual.

## Installing the FPP Software {#installing-the-fpp-software}

Operating‑system files are called **images**. To install FPP you need a program
for "burning" the image to the micro‑SD card, and optionally one for formatting
the card first.

> **Note:** You cannot simply copy the files to the card — the image must be
> written with imaging software.

### Required programs

**An SD card formatter (optional):**

- ([https://www.sdcard.org/downloads/](https://www.sdcard.org/downloads/)) — versions for Windows and Mac.
- ([https://gparted.org/](https://gparted.org/)) — for Linux systems.

**An image‑writer program:**

- **Raspberry Pi Imager** — can download the FPP image for both Raspberry Pi and
  BeagleBone hardware directly, as part of the installation process.
- **Balena Etcher** ([https://www.balena.io/etcher/](https://www.balena.io/etcher/)) — Windows, Mac and Linux.
- **dotNet Disk Imager** ([https://sourceforge.net/projects/dotnetdiskimager/](https://sourceforge.net/projects/dotnetdiskimager/)) —
  a good option for Windows; it can also wipe the SD card, so you won't need a
  separate formatter.

### Getting the FPP software

The software is available at ([https://github.com/FalconChristmas/fpp/releases](https://github.com/FalconChristmas/fpp/releases)),
where you can download the most current **image file** (not the application
source code). The image file has `.img.zip` in its name.

Image files start with `FPP` and indicate the version and SBC image. Download the
one that matches the SBC you are using:

- **Pi64** — for all Raspberry Pi 3/4/5, Zero 2 W, CM4/CM5 variants
- **Pi** — for all other Raspberry Pi variants.
- **BB64** — for the PocketBeagle 2.
- **BB** — for all other BeagleBone / PocketBeagle variants.

Several releases are listed on GitHub; not all have an image. Scroll down until
you find the first version that provides images.

> **Note:** If you are going to use the Raspberry Pi Imager, you do not need to
> download the image file first.

Depending on your imaging program, you may have to unzip the file before you can
use it (uncommon). If your imaging software cannot write directly from a `.zip`,
make sure you flash the `.img` file, not the `.zip`; if unsure, unzip first.

The three most popular methods are covered below — Raspberry Pi Imager,dotNet Disk
Imager, and Balena Etcher. Use the method for the software you have.

> **Note:** Raspbery Pi Imager can be used for BeableBone images as well.

### Formatting the micro‑SD card (optional)

Before writing the image you may format the card to remove any existing
partitions. This is not usually needed with most imaging programs. Insert the
card and do a **Quick Format** using the SD Card Formatter (not the Windows or Mac
file manager).

### Burning with Raspberry Pi Imager

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

When finished, click **Continue** and proceed to [Software Installation](#software-installation).

### Burning with dotNet Disk Imager

1. Open dotNet Disk Imager (allow it to make changes if prompted).
2. *(Optional wipe)* Select your SD card under **Device** and click **Wipe
   Device**; confirm and wait for completion.
3. Choose the downloaded image file via the file icon next to the **Image file**
   box, and select the SD card as the target.
4. Click **Write to Device** (confirm if prompted) and wait for the completion
   message.

As above, do **not** format the card after writing. Turn the device off and
insert the card and proceed to [Software Installation](#software-installation).

### Burning with Balena Etcher

1. Open Balena Etcher and click **Select Image**; choose the downloaded image
   file.
2. Make sure the correct SD card is selected as the target.
3. Click **Flash!** (confirm if prompted) and wait for the completion message.

> **Note:** Some users have resolved Balena Etcher errors by running it as an
> Administrator, or by unblocking the image file in its properties.

The written image is not in a format Windows or Mac can read, so you may see an
error after flashing. **Do not** format the card afterwards. Turn the Pi/BB off,
insert the card, and proceed to [Software Installation](#software-installation).

### Software Installation {#software-installation}

FPP is configured from a web interface — **you do not need to connect a monitor to
the device.** You access it from a web browser on another computer.

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
  to the device with a USB cable. Only a few devices support USB Tethering: Raspberry Pi
  Zero W, BeagleBone Black, PocketBeagle, BeagleBone Green, and BeagleBone Green
  Gateway. (The PocketBeagle 2 does **not** support USB tethering.)
- **Network Connection** — connect the device to your **router** with an Ethernet
  cable **(not directly to your computer)**. Any Pi or BeagleBone with an Ethernet
  port or adapter can use this method.
- **Wi‑Fi Tethering** — for devices with Wi‑Fi tethering capability (on‑board or
  via a supporting adapter), useful when no other method is available.



> **Warning:** If you are using the KulpLights **K4‑PB v2.0** or **K40‑PB v3.0**
> (produced in 2022), do **not** use USB tethering — it could destroy the USB
> circuitry.

#### USB Tethering Installation {#usb-tethering-installation}

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
8. Continue to [Initial Configuration](#initial-configuration).

#### Network Connection Installation

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
   [Help and Troubleshooting](#help-and-troubleshooting) chapter.)
8. Continue to [Initial Configuration](#initial-configuration).

#### Wi‑Fi Tethering Installation

Use this if your device supports Wi‑Fi tethering, or to make changes when the
device cannot otherwise connect to your network (without re‑imaging). You need a
computer with a wireless connection.
> **Note:** Many USB Wi‑Fi adapters do **not** support Wi‑Fi tethering
> (on‑board Wi‑Fi on Raspberry Pis usually does).
   
1. Insert the SD card with the correct image.
2. Fit any network adapters you will need.
3. On some older BeagleBone Black boards, hold **S2** for 5 seconds after
   connecting power for the first install.
4. All other devices — connect power.
5. Wait about one minute.
6. On your computer, connect to the wireless network named **FPP**; the password
   is **Christmas**.
7. Browse to `192.168.8.1`.
8. Continue to [Initial Configuration](#initial-configuration).

### Initial Configuration {#initial-configuration}

Once FPP is installed, the **Initial Setup** page provides a convenient place to
configure common or required settings:

![The Initial Setup page.](images/initial-setup.png)

- **UI Password** *(required choice)* — whether to set a web‑UI password. This is
  an advanced setting; the recommended choice is **No Password (default)**. See
  [FPP Settings → UI](#ui).
- **OS Password** *(required choice)* — used for SSH and similar access. This is
  an advanced setting; the recommended choice is **falcon (Default)**. See [FPP
  Settings → System](#settingsSystem).
- **FPP Player Mode** — set the mode this device will run in. If unsure, leave it
  at **Player**. See [The Status Page → FPP Mode](#fpp-mode).
- **Host Name** — a meaningful name for this device. See *Network → Host
  Settings*.
- **Installed Cape/Hat** — if your device has a cape/hat with no EEPROM, define
  the Virtual EEPROM here. See [Pixel Port Licensing](#pixel-port-licensing).
- **Share Crash Data with FPP Developers** — helps developers find and fix crash
  bugs. The recommended setting is *Include settings and configurations*. See
  [FPP Settings → Privacy](#privacy).
- **Email Address** — if you share crash data, providing an email lets the
  developers follow up if needed.

The Initial Setup page also offers to **restore a previous configuration**, which
saves time in setting a replacement or rebuilt device up from scratch. As well as
restoring from an FPP backup file, FPP 10 adds a **File Copy Restore** option that
brings the configuration across directly. See [Backup, Restore and Proxies](#backup-restore-and-proxies).

After completing initial setup, work through the [Initial Network Configuration](#initial-network-configuration)
and the rest of this manual to finish setting up your show.

## Initial Network Configuration {#initial-network-configuration}

After completing Initial Setup, click **Finish Setup** (top‑right). Back on the
main screen you will see a reboot warning — **do not reboot yet**. Instead open
**Status/Control → Network** to configure how the device connects.

You should decide how you want your network configured before editing these
settings (see [Advanced Options → Common Network Setups](#common-network-setups) if you are unsure). For a
temporary arrangement you can use a **wired‑on‑home‑network** configuration so you
can update the software and finish configuration before deploying the device in
its final location — this is also a good testing configuration. If your device
has no Ethernet port but has a Wi‑Fi adapter, a **separate show network** may be a
better option.

> **Note:** The Network page is covered in full in the [Network](#network) chapter; this section
> walks through the first‑time setup.

### Wi‑Fi network settings

*(Skip to Ethernet settings if you do not need Wi‑Fi.)*

> **Note:** Many USB Wi‑Fi adapters do not support 5 GHz; 2.4 GHz networks are
> recommended for their better range. To configure Wi‑Fi with no adapter fitted,
> see [Network → Interface Settings](#interface-settings).

![The Network Configuration page.](images/network.png)

1. Click the **wlan0** interface (the wireless interface).
   
![Wlan0 Settings](images/Wlan0Initial.png)

2. Enter your **WPA SSID** exactly as configured in your router (including
   capitalization); you can usually pick it from the available networks.
3. Enter the **WPA Pre‑Shared Key (PSK)** — your wireless password — exactly as
    configured (use the show/hide button to check it).
4. Select your **interface mode** (Static or DHCP)

   > **Note:** With DHCP, a correctly configured **host name** and **DNS server**
   > become important.

5. If you are going to use a **Static** IP address, enter an **IP address** unique to this interface.
6. **Netmask** — for most consumer networks this is `255.255.255.0` (match your
   router).
7. Click on the Green **Update Interface** button.
   
### Ethernet network settings

*(Skip to Finishing up if you do not need Ethernet.)*

1. Click the **eth0** interface (the wired interface).
   ![Eth0 Settings](images/Eth0Initial.png)
2. Select your **interface mode** (Static or DHCP)

   > **Note:** With DHCP, a correctly configured **host name** and **DNS server**
   > become important.

3. If you are going to use a **Static** IP address, enter an **IP address** unique to this interface.
3. **Netmask** — usually `255.255.255.0` (match your router).
4. Click on the Green **Update Interface** button.

### Finishing up
1. Click on the Global Network settings button on the top of the page
![GlobalNetwork](images/GlobalNetwork.png)
2. **Host Name** Change the Host name if you need to.
3. **Default Gateway** — usually the IP address of your home/show router; it is often
   filled in automatically, but check it. Click on **Update Gateway**.If you are using DHCP, leave it blank.
4.  **DNS Server Mode** — if any interface uses a static IP, set this to **Manual**
   and configure the addresses. Click on the **Update DNS** button
5.  Select the **WiFI Regulatory Domain** to the country where you will use the device.
Once eth0, wlan0, host and DNS are all configured, double‑check them. When
correct, click **Reboot** (from the red banner at the top or the button at the
bottom).

> At this point the device must be connected to your network according to the
> configuration you set, since you may not be able to reach it otherwise.

## Final Configuration and Updating {#final-configuration-and-updating}

### Reconnecting after the network change

Once the device is connected to your network using the settings you entered, open
its web page by using either the static IP address that you configured or using the host name
you configured. To connect to the device via host name, enter the address in this format:
devicehostname.local 
The page currently on your screen may no longer reach your FPP device. If you cannot reach the FPP
page, see the [Help and Troubleshooting](#help-and-troubleshooting) chapter.

In most configurations FPP has internet access and will keep the correct time
automatically. If your device will **not** have internet access and has a
Real‑Time Clock (RTC) installed, see ([FPP Settings → Localization → Time Config](#localization)).

### Updating the software

You should update to the current version of the software. Open **Help → System
Upgrade**.

![The System Upgrade / About page.](images/about.png)

This screen shows the FPP version you are running and, if an update is available,
a notice. Click **Upgrade FPP**.

> **Note:** If the **Remote Git Version** shows *Unknown*, FPP usually cannot
> reach the internet — most often a network/DNS configuration problem. See the
> [Help and Troubleshooting](#help-and-troubleshooting) chapter.

You will get a progress screen; the update can take several minutes. When it
finishes, click **Close** at the bottom. In FPP 10 the progress pop‑up also shows
the current stage in its **title**, so you can tell how far along an FPP or FPPOS
upgrade is at a glance — useful when the window is in the background.

Sometimes an additional **major** update is offered — if so, click **Upgrade**.
You will usually see a **Release Notes** page; some updates need a matching
Operating System (OS) update to gain full functionality, and that will be noted
there.

> **Note:** If the release notes indicate an **FPPOS** upgrade may be required,
> clicking **Upgrade** will **not** upgrade the OS — that is a separate step. See
> *Help → System Upgrade* for details.

Confirm any prompts and let the update run, then click **Close**. When complete,
the screen returns to the About page and you can verify the version. When fully up
to date, the **Local Git Version** matches the **Remote Git Version**.

Your FPP software is now installed and up to date. There are many ways to use FPP,
and the settings needed to run your show vary with your particular setup — refer
to the appropriate chapters that follow for details.

> **Note:** After an **FPPOS** upgrade, FPP 10 prompts you to reinstall your
> plugins — an OS upgrade replaces the underlying system, so plugins need to be
> put back. Accept the prompt, or reinstall them yourself from the *Plugins* page
> (the **Reinstall All** button does the lot).

> **Tip:** Always take an **FPP Backup** (see the [Backup, Restore and Proxies](#backup-restore-and-proxies)
> chapter) before a major upgrade, so you can roll back if needed.
