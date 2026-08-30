# Separate Network {#separate-network}

The controllers — and often the FPP device's second network interface — live on
their **own isolated network**, keeping heavy pixel traffic (E1.31/ArtNet/DDP)
off your home network entirely.

- FPP typically **bridges** the two networks: one interface faces your home
  network (for configuration/updates), the other faces the show network (the
  controllers). Keep them on **different subnets**, and give a gateway only to
  the home‑facing interface — see [Networking → Overview](#networking-overview).
- FPP can run a **DHCP server** on the show‑network interface so controllers get
  addresses automatically — see the **DHCP Server** option under
  [Network → Interface Settings](#interface-settings).
- Reach a controller's own web UI from your computer through FPP's
  [Proxy Settings](#proxy-settings) rather than adding static routes — the
  simplest way to configure a controller that only exists on the isolated show
  network. A manual [static route](#static-routes) on the computer or router
  also works but, notably, is not persistent across reboots on a Mac.
- All FPP/controller **host names must still be unique**, even though the two
  networks are otherwise isolated from each other.

This layout suits larger or permanent displays where pixel traffic could
otherwise saturate a home network, at the cost of a little more setup than
[Home Network](#home-network).
