# Networking Explained {#networking-explained}

Networking trips up a lot of people getting started in animated holiday
lighting. This chapter is a plain‑language, ground‑up explanation of IP
addressing and of Universe/Channel addressing — companions to the more
practical [Networking Overview](#networking-overview) and
[Channel Outputs](#channel-outputs) chapters, if you want to understand *why*
the rules there work the way they do.

## Network Overview {#network-overview-explained}

A network is a group of devices identified by an **IP address**. Think of an
IP address as a telephone number: for devices to communicate, every device
needs a unique "number". IP addresses are written as four groups of numbers
(0–255) separated by dots, e.g. `192.168.110.23`. The first three groups are
like an area code and are called the **subnet** (`192.168.110`); the last
group is like the local number and identifies the **device** (`23`). Only
devices that share a subnet — the same "area code" — can communicate
**directly**, the way you can dial a local number without an area code.

If a device needs to reach another device on a *different* subnet, that's
like calling a different area code: extra routing information is needed. When
a device gets a request for an address it doesn't recognise as local, it
sends the request to its **Gateway** — similar to an old‑fashioned telephone
operator. A Gateway is any device on the same subnet that is also able to
route traffic onward; it is usually your home router, or an FPP device sitting
between a controller and the show network. A Gateway only knows how to route
addresses in its own small "phone book" — anything it doesn't recognise, it
forwards to *its own* configured Gateway. Sometimes a Gateway needs explicit
extra instructions to route traffic correctly; this is a **Static Route** (see
[Configuring a Static Route](#configuring-a-static-route)).

You can add a Static Route on a single computer, so that when it's told to
reach an address covered by the route, it sends the data to that route's
Gateway — but only *that* computer gains access, unless you repeat the setup
on every computer on the network. Most routers let you add Static Routes
instead, which then apply to every device on the local network. Static Routes
added in Windows can be made persistent; on a Mac they are not, and need to be
re‑added after every reboot.

## Universes, Channels and Ports, oh my! {#universes-channels-and-ports}

> **Note:** xLights and FPP features like Auto Size, Auto Layout Models, the
> Visualizer and FPP Connect exist specifically so you don't *need* to
> understand channel addressing to configure your controllers and FPP
> devices — this section is background for when you want to understand what's
> happening underneath.

A **port** is simply where you plug in a string of pixels. Large lighting
networks can have tens of thousands of channels, and every device — including
you — needs a consistent way to know where every pixel is: which model it
belongs to, which controller is driving it, and which port(s) carry its data.

Animated lighting borrowed its addressing scheme from DMX: **Universes** and
**Channels**. A Universe can hold any number of Channels up to a maximum of
512 — you decide how many channels each of your Universes actually uses. You
*can* use **Absolute Addressing**, numbering every channel from 1 upward with
no Universe grouping at all, but that quickly becomes hard to manage on a
large display; breaking channels into Universes makes it easier.

An analogy: think of your pixels as passengers on a train. Each **model** in
your show is a family of passengers. Every passenger orders a drink — that's
the color/brightness data sent to that pixel. The **sequencing software**
(the travel agent) doesn't know how big the train cars will be, so it just
lists every passenger and their drink order, front to back. The **controller**
(the Terminal) knows how big each car actually is — up to 512 seats, matching
a Universe — and hands each **port** (an attendant) the drinks for its section
of passengers, in order, along with where to start serving.

For example, a show needs 1,578 channels, split across cars (Universes) of up
to 512 each — the Terminal assigns 4 cars. Attendant (port) 1 serves 490
drinks starting at car 1, seat 1. Attendant 2 serves 560 drinks starting at
car 1, seat 491 — finishing the rest of car 1, all of car 2, and the first 26
seats of car 3. Attendant 3 serves 520 drinks starting at car 3, seat 27.
Attendant 4 serves the remaining 8 drinks starting at car 4, seat 35.

A few things follow from this:

- There is no fixed relationship between a controller's ports and Universe/
  Channel addressing — a port just needs to know which Universe/channel to
  start at and how many pixels' worth of data to read, then stop.
- Universes can be numbered arbitrarily and don't need to start at 1 or run
  sequentially — a car can be numbered 100, the next 215, and so on, as long
  as every port knows which car and seat to start at.
- Universes can be any size up to 512, and don't all need to be the same size.
- A port can supply data for part of a Universe, or span more than one
  Universe.
- A port doesn't need to start at the beginning of a Universe or of a model —
  though for your own sanity, it's often worth doing so anyway.
