# Advanced Options

This chapter covers material beyond the basic setup and configuration — chiefly
networking, which is the source of most difficulty for people new to the hobby.

## Networking Considerations

For your devices to communicate, the network must be configured correctly. You
need to know your **home router's IP address** and **subnet** — usually
`192.168.0.1` or `192.168.1.1` (check a label on the router, or run `ipconfig` on
Windows / `ifconfig` on Mac to see the default gateway).

An IP address is four groups of numbers (0–255) separated by dots, e.g.
`192.168.0.1`. On most home networks the first three groups are the **subnet**
(here `192.168.0`) and the last group is the **host** (here `1`). Devices can
communicate **directly only with other devices in the same subnet**; reaching a
different subnet requires telling the systems how to route between them (see
*Static Routes* and *Proxy Settings*).

Some key rules that recur throughout this manual:

- Give show controllers **static** addresses (or router reservations) so they do
  not change.
- If a device uses **two interfaces**, put them on **different subnets** and give a
  **gateway to only one** (normally the home‑facing interface).
- All FPP/controller **host names must be unique**.

## Common Network Setups

There are four common "show network" arrangements. Each has trade‑offs, and you can
combine them as needed. When numbering devices, it is suggested to use the higher
end of the address range to avoid clashing with DHCP‑assigned addresses.

- **Standalone** – a single FPP device drives the whole display directly (via a
  cape/hat or a locally attached controller) with no show network. Simplest;
  suited to small displays. FPP can create its own Wi‑Fi (tethering) for
  configuration in the field.
- **Wired on Home Network** – FPP and the controllers sit on your existing home
  network. Easy to reach for configuration and updates, and good for testing, but
  show traffic shares the home network. A good temporary arrangement while you set
  things up.
- **Wired on Separate Show Network** – the controllers (and often the FPP's second
  interface) live on their own isolated network, keeping heavy pixel traffic off
  the home network. FPP typically bridges the two, and may run a **DHCP server** for
  the show network. Reach the show devices through FPP's **Proxy Settings**.
- **Player/Remote (MultiSync)** – one FPP **player** synchronises any number of FPP
  **remotes** with small sync packets, so each remote drives a nearby section of
  the display. Ideal for large or widespread displays where long cable runs are
  impractical. Each remote needs a copy of the sequences; the player holds the
  playlists and schedules. See *MultiSync*.

## Static Routes

When you need a computer to reach a controller on a different subnet without FPP
proxying, you can add a **static route** on the computer (or router) telling it to
reach the controller's subnet via the FPP device's address. Note that static routes
on Macs are not persistent across reboots — FPP's **Proxy Settings** are usually a
better solution (see *Backup, Restore and Proxies → Proxy Settings*).

## MultiSync / Remote details

A Player/Remote layout keeps devices frame‑accurate via MultiSync. Choose the sync
transport that suits your network: **Multicast** (recommended where the network
supports IP Multicast and IGMP Snooping), **Broadcast** (for networks that do
not), or **Unicast** (most reliable on troublesome networks — set remotes to
Unicast and disable multicast). Every remote must hold a copy of the sequences
being played; use the MultiSync page's **Copy Show Files** or xLights **FPP
Connect** to distribute them. See the *MultiSync* chapter for the full page
reference.

## Projector Control

FPP can control a projector (for example to power it on before the show and off
afterwards) using scheduled **Commands**, **scripts**, GPIO, or network/serial
control depending on the projector. Combine a scheduled *Command* entry a few
minutes before the show with the appropriate projector control method.

## Plugin Development

Plugins extend FPP with new pages, commands, playlist entry types and outputs. The
**Plugin Manager** includes a **Template Plugin** to help authors with the required
structure; a plugin provides a `pluginInfo.json` describing itself and hooks into
the relevant FPP menus. Refer to the FPP developer documentation in the repository
for the plugin API and packaging details.

> **Note:** This chapter summarises the most‑referenced advanced topics. The FPP
> forums, the xLights Zoom Room, and the developer documentation in the FPP GitHub
> repository are the best resources for deeper or edge‑case configurations.
