# Network {#network}

The **Network** page (**Status/Control → Network**) is where you set up
networking so your FPP devices and controllers can all communicate as needed.
Networking works similarly whether wired or wireless, and the two work together.
The page has three tabs: **Interface Settings**, **Global Network Settings**
(host and DNS), and **Tethering**.

![Network — Interface Settings.](images/network-interface-settings-eth0.png)

> **Note:** This page shows some Advanced Level settings that you probably won't use.
> see more information below.

Because there are so many ways to configure a network, these settings cause many
people difficulty. The basic setup earlier in this manual will get you running,
though it may not be the best long‑term arrangement; the sections below should
give you a better understanding for your situation. For deeper background on IP
addressing, see [Networking → Overview](#networking-overview).

If you want a temporary network configuration you can use the [Wired on Home Network](#home-network) 
configuration so that you can update the software and make final configurations 
before using FPP in your final network configuration. This would be a good configuration 
for testing purposes as well. But if your FPP device doesn’t have an Ethernet port 
but has a Wi-Fi adapter then [Separate Show Network](#separate-network) might be a better option.

There is a good video [here](https://youtu.be/68exxlJDox4) and Keith Westley, one of the 
xLights developers, has a good video as well [here](https://youtu.be/g0fOZs6UgXw)
 
## Interface Settings {#interface-settings}

Depending on the device, FPP may have up to two built‑in network interfaces (more
if you add adapters, though that is uncommon): **eth0** for wired Ethernet and
**wlan0** for wireless. If you have both, configure each separately.

**eth0 Interface**
![Network — eth0 Interface Settings.](images/network-interface-settings-eth0.png)

- **Interface Mode:**
    - **Static** – you assign the IP address. You must ensure each address is
      unique and does not clash with one your router has already handed out via
      DHCP. You also need to make sure that your router does not assign this IP address
      to another device down the road. Many routers assign DHCP addresses from the low end of the range (not
      always), and some let you limit the DHCP range to avoid conflicts.
    - **DHCP** – your router assigns and manages the IP address and gateway. This is
      the easiest method, but your router may not retain the IP address if the device
      is disconnected for a long time (you can usually still reach FPP by host
      name), and the interface must be on a network with a DHCP server.

- **IP address** – unique to this device/interface, in the same subnet as the
  network it talks to (usually the first three number groups). The **Ping** button
  can be used to check whether an address is already in use.
- **Netmask** – defines the network size; most consumer networks use
  `255.255.255.0`.

> **Note:** If you use both interfaces they should be on **different subnets**,
> and only **one** interface should have a gateway — normally the one connected
> to your home network.

**Create Persistent Name**-If you are using more than one Ethernet interface (common for users with a Color-Light board) 
and you need the Ethernet adapter to keep the configuration order, then you can create a Persistent Name. The best practice would be: 

- Power down the FPP device.
- Make sure that only the primary Ethernet interface is installed.
- Power up the FPP device.
- Plug in the USB Ethernet adapter. 
- Configure the eth0 and eth1 devices
- Click on Update Interface
- Click on Create Persistent Name

This will save your eth0 and eth1 configurations so that they will load up in the correct order.

- **Route Metric** – leave at default for most setups. If more than one interface
  has a gateway (unusual), give your primary interface a **lower** number.
  *(This is only visible with an Advanced or higher level setting in the UI tab.)*

- **IP Forwarding** – This is typacally used when FPP connects to Wi‑Fi and also feeds a
  controller/switch over Ethernet and you are not using a Proxy Host (not needed
  with a cape/hat or in standalone mode):
    - **Off** – no forwarding.
    - **Forwarding** – forwarding within the local network only; forwarded devices
      may not have internet access.
    - **Masquerading/NAT** – forwarding with NAT, giving forwarded devices
      internet access without complex static routing. Configure this on the
      interface connected to your home network.
*(This is only visible with an Advanced or higher level setting in the UI tab.)*

> **Note:** This replaces the old "Enable Routing between network interfaces"
> option on the former Interface Routing tab and is typically used on the wlan0 interface **NOT the eth0**
> 
- **DHCP Server** – let FPP hand out IP addresses to connected devices — useful on a
  *Separate Show Network* with no router. Only **one** device on a network should
  issue DHCP, and it must have a static IP.
*(This is only visible with an Advanced or higher level setting in the UI tab.)*

> **Caution:** If you connect this interface to your home network with the DHCP
> server enabled, devices may get incorrect addresses. Assigned devices appear
> under **Static Leases**, where you can create a reservation. 
> *(This is only visible with an Advanced or higher level setting in the UI tab.)*

- **DHCP Pool Offset / Size** – the starting address and number of addresses the
  DHCP server may assign. *(*This is only visible with an Advanced or higher level 
  setting in the UI tab and with DHCP enabled.)*

> **Note:** In FPP 10 — a change that comes from the move to a newer Debian
> base — **DHCP leases survive a reboot**. Restarting FPP no longer clears the
> leases it has handed out, so a device that had an address keeps it. Lease
> times are set to sensible values by default. To start over with a clean pool,
> run **FPP Settings → System → Reset FPP Config** with **Network Config Files**
> ticked; the saved leases are then cleared on the **next reboot** rather than
> immediately, which avoids disturbing addresses on interfaces that are still in
> use.

**wlan0** Interface

![Network — Interface Settings, wlan0.](images/network-interface-settings-wlan0.png)

This page will have information about your current Wi-Fi connection such as **Connection Status** 
It will also list Available Networks if your Wi-Fi adapter can scan the networks.

- **WPA SSID** – your wireless network name (tick **Hidden** if you are connecting to a hidden SSID).
- **WPA Pre‑Shared Key** – the password; use the eye icon to reveal it and check
  it is correct.
- **Backup WPA SSID / PSK** – an alternate network that FPP tries if it cannot reach
  the primary. *(This is only visible with an Advanced or higher level setting in the UI tab.)*
- **Route Metric** – leave at default for most setups. If more than one interface
  has a gateway (unusual), give your primary interface a **lower** number.
  *(This is only visible with an Advanced or higher level setting in the UI tab.)*
- **IP Forwarding** – This is typacally used when FPP connects to Wi‑Fi and also feeds a
  controller/switch over Ethernet and you are not using a Proxy Host (not needed
  with a cape/hat or in standalone mode):
    - **Off** – no forwarding.
    - **Forwarding** – forwarding within the local network only; forwarded devices
      may not have internet access.
    - **Masquerading/NAT** – forwarding with NAT, giving forwarded devices
      internet access without complex static routing. Configure this on the
      interface connected to your home network.
*(This is only visible with an Advanced or higher level setting in the UI tab.)*

> **Note:** This replaces the old "Enable Routing between network interfaces"
> option on the former Interface Routing tab and is typically used on the wlan0 interface **NOT the eth0**
> 
- **DHCP Server** – let FPP hand out addresses to connected devices — useful on a
  *Separate Show Network* with no router. Only **one** device on a network should
  issue DHCP, and it must have a static IP.

  > **Caution:** If you connect this interface to your home network with the DHCP
  > server enabled, devices may get incorrect addresses. Assigned devices appear
  > under **Static Leases**, where you can create a reservation. 
  *(This is only visible with an Advanced or higher level setting in the UI tab.)*

- **DHCP Pool Offset / Size** – the starting address and number of addresses the
  DHCP server may assign. *(Advanced, with DHCP enabled.)*

  > **Note:** In FPP 10 — a change that comes from the move to a newer Debian
  > base — **DHCP leases survive a reboot**. Restarting FPP no longer clears the
  > leases it has handed out, so a device that had an address keeps it. Lease
  > times are set to sensible values by default. To start over with a clean pool,
  > run **FPP Settings → System → Reset FPP Config** with **Network Config Files**
  > ticked; the saved leases are then cleared on the **next reboot** rather than
  > immediately, which avoids disturbing addresses on interfaces that are still in
  > use.

- **Update Interface** – saves the settings for the current interface. Click it
  before moving to another interface, and again when finished; then reboot.
- **Add New Interface** – configure an `eth0` or `wlan0` interface even when the
  physical hardware is not yet present (e.g. configuring wlan0 for a BeagleBone
  before its Wi‑Fi adapter/cape is attached). A small dialog asks for the
  interface name — enter it exactly as the system will name it, such as `wlan0` or
  `eth1` — and the new interface then appears as its own tab to configure.
  *(This is only visible with an Advanced or higher level setting in the UI tab.)*

- **Create Persistent Name** – when using more than one Wi-fi interface
  (Not common) and you need the adapters to keep their order,
  create persistent names. 
  
  Best practice:
    1. Power down the device.
    2. Ensure only the primary Wi-fi interface is installed.
    3. Power up the device.
    4. Plug in the USB Wi-fi adapter.
    5. Configure `wlan0` and `wlan1`.
    6. Click **Update Interface**, then **Create Persistent Name**.

  This saves the configurations so they load in the correct order.

## Global Network Settings (Host & DNS)

![Network — Global Network Settings.](images/network-global-network-settings.png)

This tab assigns the device's **host name** and DNS settings.

- **Host Name** – the "human" name used to reach the device (like typing a domain
  instead of an IP). If DNS or another part of your network is misconfigured the
  host name may not resolve, but you can still reach FPP by IP address. Choose
  something meaningful and **unique** among your devices — e.g. `FPPMaster`,
  `FrontLawn`, `HouseOutline`. Names may contain only letters, numbers and hyphens
  (`-`), may not begin or end with a hyphen, and cannot contain spaces. After
  changing it you can no longer use `http://fpp.local/`; use the new name (e.g.
  `http://YardProps.local/`) or the IP address. Save after entering it.

> Keeping the default `FPP` is possible if you will never add another instance,
> but renaming is strongly recommended — shows tend to grow, and duplicate names
> cause confusion.

- **Host Description** – additional, free‑form text (no host‑name restrictions)
  shown on the [MultiSync](#multisync) page and the xLights FPP Connect screen.
- **Default Gateway** – You will typically set this to your router's IP address.
- **DNS servers** – with any static interface, set DNS to **Manual** and enter
  servers; typically your router's IP for one and an internet server such as
  `8.8.8.8` for the other.
- **Wi‑Fi Regulatory Domain** – enter your country. Some jurisdictions have
  regulations, and Wi‑Fi will not work correctly unless this is set correctly.

## Tethering {#tethering}

![Network — Tethering.](images/network-tethering.png)

FPP supports two kinds of tethering: **Wi‑Fi Tethering**, where FPP acts as its
own access point, and **USB Tethering**, where FPP connects directly to a
computer by USB cable.

### Wi‑Fi Tethering
> **Note:** Due to the number of various USB Wi-Fi adapters, the Wi-Fi Tethering might 
> not work using some USB Wi-Fi adapters. Thay have to support AP mode.
> (this does not apply to the **internal** Wi-Fi adapters on the Raspberry Pis or BeagleBones). 
> 
Wi‑Fi Tethering lets you reach FPP when nothing is connected to the Ethernet or
Wi‑Fi interfaces — especially useful on a Raspberry Pi whose on‑board Wi‑Fi
supports AP mode (not all adapters do). Bring your computer near the device,
connect to the **FPP** wireless network (password **Christmas**), and browse to
`192.168.8.1`.

> **Note:** If the device has an OLED screen it will display a QR code you can
> scan to reach it.

There are three Wi‑Fi tethering modes:

- **If no connection** *(default)* – FPP starts the **FPP** access point at boot
  only if it detects no network on any interface. (A device connected to an
  Ethernet port usually counts as a connection, so AP mode will not start.)
- **Enabled** – FPP always starts the access point at boot.
- **Off** – the access point is never started.
- 
> **Note:** It is not recommended to turn off the Wi-Fi tethering. This is a useful
> setting that can often time save you from reformatting your SD card if you mis-configure
> your network settings
 
> **Warning:** If you set the Tethering to Enabled, the **only** way you will be
> able to connect to the Wi-Fi interface of your FPP would be through the FPP AP
> it will NOT conect to the configured wlan0 interface.
>
### USB Tethering

> **Note:** Only a few devices support USB Tethering: Raspberry Pi Zero W, BeagleBone Black, 
> PocketBeagle, BeagleBone Green, and BeagleBone Green Gateway. (The PocketBeagle 2 does not support USB tethering.)
> 
USB Tethering connects FPP directly to your computer with a USB cable, as
described in [Installing the FPP Software → USB Tethering Installation](#usb-tethering-installation). It is
often the easiest way to reach a device for setup, on the hardware that supports
it.
