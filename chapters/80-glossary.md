# Glossary

**Absolute Channel** – A numbering system that uniquely identifies every channel,
simply 1 to the last channel needed. Displays can have very large channel counts,
which can be hard to manage.

**BBB** – BeagleBone Black; commonly used as shorthand for the whole BeagleBone
series of single‑board computers.

**Broadcast** – Sending the same network data to every device on the network.

**btrfs** – A Linux filesystem with advanced features including compression, at
the cost of more CPU usage.

**Channel** – An identifier for a component in a lighting display — commonly a
pixel's colour/brightness, but also DMX channels for other devices.

**DHCP** – Dynamic Host Configuration Protocol; automatically assigns IP addresses
to devices. Addresses are not permanent. Requires a DHCP server (most routers have
one).

**DNS** – Domain Name System; lets you use friendly host names instead of IP
addresses. Requires a DNS server configured in your network settings (most routers
provide one).

**E1.31** – A network protocol for transmitting DMX data; the most common protocol
in the animated‑lighting hobby.

**Effect** – A small sequence, usually for one model, used to overwrite the data a
sequence is playing; triggered by an event or manually.

**eMMC** – On‑board flash memory on the BeagleBone Black/Green; the FPP OS can be
stored on it.

**eth0** – The wired network interface of the FPP.

**Event** – A sequence or script run when a trigger fires, or triggered manually
from the FPP interface.

**ext4** – The standard Linux filesystem.

**FPP** – Falcon Player; a widely used player and operating system for
animated‑lighting displays.

**FSEQ file** – The standard raw data file format that tells controllers how to
illuminate each light or DMX channel.

**Gateway** – The IP address a device sends data to when it does not know how to
route it — usually your router, or an FPP bridging two subnets.

**Git** – A distributed version‑control system; the core of GitHub.

**Host Name** – A friendly name for a device, used instead of its IP address.

**IP Address** – A numerical device address: four parts (0–255) separated by dots.

**Multicast** – Sending the same data only to devices that requested it.

**MultiSync** – FPP's mechanism to discover relevant FPP instances in a
Player/Remote configuration and keep them synchronised.

**Netmask** – A mask defining a subnet's size; typically `255.255.255.0` on home
networks.

**Network** – A group of devices connected to share data.

**NTP** – Network Time Protocol; keeps system clocks synchronised to accurate time.

**P10/P5 panel** – Display panels (typically 6″×12″) whose pixel spacing matches
the type (P5 = 5 mm apart). Combined into larger matrices, often used for "Tune To"
signs.

**Pixel** – An individually addressable LED whose colour is independent of the
other pixels in the string.

**Player/Remote** – An FPP method to synchronise several FPP devices via small sync
signals — useful for large or widespread displays where Ethernet cabling is
impractical.

**Playlist** – An ordered list of items FPP plays to control lights and props.

**Plugin** – A component that adds functionality to FPP.

**Port** – The physical connection point on a controller for a pixel string.

**Raspberry Pi** – A single‑board computer used to play sequences or act as a
controller interface.

**Real Time Clock (RTC)** – A component with an accurate timing crystal that keeps
time when there is no network.

**SBC** – Single‑Board Computer; the Raspberry Pi and BeagleBone series are the
most common in this hobby.

**Script** – A small program that performs a specific function in FPP.

**SSH** – Secure Shell; a secure command‑line way to access a device (for advanced
users).

**Subnet** – A portion of a larger network, usually the first three segments of an
IP address (e.g. `192.168.0.x`, where `192.168.0` is the subnet).

**Tethering** – Connecting two devices directly (via Ethernet, USB or Wi‑Fi) with
no router or switch.

**UI** – User Interface; how you interact with a device or program. FPP's UI is
web‑based.

**Unicast** – Sending data individually to each target device; usually more
efficient than Multicast or Broadcast unless the same data goes to many devices.

**Universe/Channel notation** – A numbering system that groups channels into
user‑defined **universes** (up to 512 channels each), often easier to manage than
absolute numbering. Universes can have gaps and need not start at 1.

**uSD card** – A micro‑SD card; in FPP it usually holds the operating system and
related files.

**wlan0** – The Wi‑Fi (wireless) network interface of the FPP.

**WPA Pre‑Shared Key** – The password for a Wi‑Fi network.

**WPA SSID** – The technical name for a wireless network.
