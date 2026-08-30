# Standalone {#standalone}

A single FPP device drives the whole display directly — through a cape/hat or a
locally attached controller — with **no separate show network** at all. This is
the simplest network layout, and the one most small displays use.

- No second FPP or remote controller to keep in sync; the device that plays the
  show is the only device on the network.
- FPP can create its own Wi‑Fi access point (**tethering**, see
  [Network → Tethering](#tethering)) so you can reach the device's web UI to
  configure it in the field, even with no router nearby.
- Because there is no show‑only network segment, there is nothing extra to
  troubleshoot beyond the device's own connection to your home network (or none
  at all, if you only ever configure it over tethering).

> **Tip:** Standalone is also a good layout to fall back to while troubleshooting
> — if a MultiSync or separate‑network setup is misbehaving, confirm the same
> show plays correctly with the controllers wired directly to a single FPP
> first.

See [Networking → Overview](#common-network-setups) for how this compares with
the other layouts.
