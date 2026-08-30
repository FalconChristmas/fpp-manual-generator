# Advanced Options

This chapter covers material beyond the basic setup and configuration. For
networking topics — subnetting, static routes, and choosing a show network
layout — see the [Networking](#networking-overview) chapters.

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
