# Networking Overview {#networking-overview}

For your devices to communicate, the network must be configured correctly. You
need to know your **home router's IP address** and **subnet** — usually
`192.168.0.1` or `192.168.1.1` (check a label on the router, or run `ipconfig` on
Windows / `ifconfig` on Mac to see the default gateway).

An IP address is four groups of numbers (0–255) separated by dots, e.g.
`192.168.0.1`. On most home networks the first three groups are the **subnet**
(here `192.168.0`) and the last group is the **host** (here `1`). Devices can
communicate **directly only with other devices in the same subnet**; reaching a
different subnet requires telling the systems how to route between them (see
[Static Routes](#static-routes) and [Proxy Settings](#proxy-settings)).

Some key rules that recur throughout this manual:

- Give show controllers **static** addresses (or router reservations) so they do
  not change.
- If a device uses **two interfaces**, put them on **different subnets** and give a
  **gateway to only one** (normally the home‑facing interface).
- All FPP/controller **host names must be unique**.

## Choosing a show network layout {#common-network-setups}

There are four common "show network" arrangements, each covered in its own
chapter. Each has trade‑offs, and you can combine them as needed. When numbering
devices, it is suggested to use the higher end of the address range to avoid
clashing with DHCP‑assigned addresses.

- **[Standalone](#standalone)** – a single FPP device drives the whole display
  directly (via a cape/hat or a locally attached controller) with no show
  network. Simplest; suited to small displays.
- **[Home Network](#home-network)** – FPP and the controllers sit on your
  existing home network. Easy to reach for configuration and updates, and good
  for testing, but show traffic shares the home network.
- **[Separate Network](#separate-network)** – the controllers (and often the
  FPP's second interface) live on their own isolated network, keeping heavy
  pixel traffic off the home network.
- **Player/Remote (MultiSync)** – one FPP **player** synchronises any number of
  FPP **remotes** with small sync packets, so each remote drives a nearby
  section of the display. Ideal for large or widespread displays where long
  cable runs are impractical. Each remote needs a copy of the sequences; the
  player holds the playlists and schedules. See the [MultiSync](#multisync)
  chapter for the full page reference, including how to choose between
  Multicast, Broadcast and Unicast sync.

## Static Routes {#static-routes}

When you need a computer to reach a controller on a different subnet without FPP
proxying, you can add a **static route** on the computer (or router) telling it to
reach the controller's subnet via the FPP device's address. Note that static routes
on Macs are not persistent across reboots — FPP's **Proxy Settings** are usually a
better solution (see [Proxy Settings](#proxy-settings)).
