# Initial Network Configuration

After completing Initial Setup, click **Finish Setup** (top‑right). Back on the
main screen you will see a reboot warning — **do not reboot yet**. Instead open
**Status/Control → Network** to configure how the device connects.

You should decide how you want your network configured before editing these
settings (see *Advanced Options → Common Network Setups* if you are unsure). For a
temporary arrangement you can use a **wired‑on‑home‑network** configuration so you
can update the software and finish configuration before deploying the device in
its final location — this is also a good testing configuration. If your device
has no Ethernet port but has a Wi‑Fi adapter, a **separate show network** may be a
better option.

> The Network page is covered in full in the *Network* chapter; this section
> walks through the first‑time setup.

## Wi‑Fi network settings

*(Skip to Ethernet if you do not need Wi‑Fi.)*

> **Note:** Many USB Wi‑Fi adapters do not support 5 GHz; 2.4 GHz networks are
> recommended for their better range. To configure Wi‑Fi with no adapter fitted,
> see *Network → Interface Settings*.

1. Select the **country** where you will use the device.
2. Click the **wlan0** interface (the wireless interface).
3. Choose **Static** to assign the IP address yourself, or **DHCP** to have your
   router assign it.

   > **Note:** With DHCP, a correctly configured **host name** and **DNS server**
   > become important.

4. For **Static**, enter an **IP address** unique to this interface.
5. **Netmask** — for most consumer networks this is `255.255.255.0` (match your
   router).
6. **Gateway** — usually the IP address of your home/show router; it is often
   filled in automatically, but check it.
7. **DNS Server Mode** — if any interface uses a static IP, set this to **Manual**
   and configure the addresses.
8. **DNS Server 1 / 2** — typically your router's IP for one, and an
   internet‑based server for the other (`8.8.8.8` is Google's, commonly used).
   Order does not matter.
9. Enter your **WPA SSID** exactly as configured in your router (including
   capitalisation); you can usually pick it from the available networks.
10. Enter the **WPA Pre‑Shared Key (PSK)** — your wireless password — exactly as
    configured (use the show/hide button to check it).

Click **Update Interface**. The **Restart Network** button will appear — **do not
click it yet**.

## Ethernet network settings

*(Skip to the Network chapter's Host & DNS settings if you do not need Ethernet.)*

1. Click the **eth0** interface (the wired interface).
2. Choose **Static** or **DHCP** as above.
3. For **Static**, enter a unique **IP address**.
4. **Netmask** — usually `255.255.255.0` (match your router).
5. **Gateway** — the IP address of your home/show router; check it.

> **Important — one gateway only:** If you use both interfaces (for example the
> home network over Wi‑Fi and a controller/switch over eth0), leave the **eth0
> gateway blank** and set the gateway only on **wlan0** (your home/show router).
> Only one interface should have a gateway defined; all others must leave it
> blank.

Click **Update Interface** (again, do **not** click Restart Network yet).

## Finishing up

Once eth0, wlan0, host and DNS are all configured, double‑check them. When
correct, click **Reboot** (from the red banner at the top or the button at the
bottom).

> At this point the device must be connected to your network according to the
> configuration you set, since you may not be able to reach it otherwise.
