# Plugins {#plugins}

Plugins are additional components — developed by the FPP developers or by others —
that add functionality within FPP, for more complex operations than a
[script](#scripts). You can install a plugin from the list, install a
third‑party plugin, or develop your own. Open **Content Setup → Plugin Manager**.

![The Plugins page.](images/plugins.png)

FPP 10 rebuilt this page around a **card grid**: every plugin is a tile showing its
icon (or its initials if it has none), name, author, a short description, its
category, how many installs it has, and an **Install** / **Uninstall** button.

## Finding a plugin

- **Tabs** – **Available**, **Installed** and **Updates** each carry a live count,
  so you can see at a glance how many plugins are installed and how many have an
  update waiting.
- **Search** – the single box at the top right filters as you type. It doubles as
  the way to add a third‑party plugin: paste the URL of a plugin's
  `pluginInfo.json` and FPP loads its details automatically. (Without a valid
  `pluginInfo.json`, a plugin will not install. FPP warns if the URL is missing a
  scheme such as `https://`.)
- **Categories** – pills across the top (**Audio**, **Automation**, **Data Feeds**,
  **Display & Video**, **Hardware**, **Interaction**, **Messaging**, **Monitoring**,
  **Payments**, **Other**, plus **All**) filter the grid, each showing how many
  plugins it holds. The counts follow your search, so you can see where the
  matches are.
- **Popular Plugins** – a row of the most‑installed plugins across the community,
  as a starting point if you do not know what you are looking for.

## Installing and managing

Click **Install** on a card to install a plugin, and **Check for Updates** to
re‑query the plugin sources (the button shows a spinner while it works). Where
several plugins need attention there are bulk **Update All**, **Reinstall All**
and **Uninstall All** actions, and each installed plugin also has its own
**Reinstall**. An installed plugin gains an **Open** button that jumps straight to
its configuration page.

Plugins marked **OFFICIAL** are maintained as part of the FPP project. A plugin
that has not been updated for this release is flagged **NOT UPDATED FOR FPP 10**
and its button changes to **Install anyway** — it may work, but it has not been
verified against FPP 10. Plugins known to be incompatible are tucked into a
collapsed **Incompatible Plugins** section at the bottom of the page rather than
cluttering the grid.

> **Note:** In FPP 10 plugins can be loaded and unloaded while FPP is running, so
> installing or removing one no longer always means restarting FPPD. FPP will tell
> you when a restart *is* needed. After an FPPOS upgrade, FPP prompts you to
> reinstall your plugins.

> **Note:** Most plugins require some configuration before they work correctly.
> The plugin author chooses which menu heading the plugin appears under; its
> configuration pages appear at the bottom of that menu drop‑down (there may be
> more than one). Refer to the plugin's home/help page for setup, and only install
> plugins you trust, as they run with full access to the device.

> **Tip:** At the **Developer** UI level each card also shows the plugin's open
> issue and pull‑request counts, which is a quick way to gauge how actively a
> plugin is maintained.

## Plugin logs and health

All plugin activity is written to a single unified **plugin.log**, which makes
install and runtime problems much easier to trace — see
[Help → Troubleshooting Commands](#troubleshooting-commands). FPP also tracks whether each installed plugin is official, community or
unknown, and surfaces that in the **System Health Check**.

> **Tip:** Take an [FPP Backup](#fpp-backup) before installing plugins, packages or scripts, so
> you can roll back if something misbehaves.
