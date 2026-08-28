# Plugins, Packages and Scripts

FPP can be extended beyond its built‑in features with **plugins**, optional
software **packages**, and user **scripts**.

## Plugin Manager

Plugins are additional components — developed by the FPP developers or by others —
that add functionality within FPP, for more complex operations than scripts. You
can install a plugin from the list, install a third‑party plugin, or develop your
own. Open **Content Setup → Plugin Manager**.

![The Plugins page.](images/plugins.png)

FPP 10 rebuilt this page around a **card grid**: every plugin is a tile showing its
icon (or its initials if it has none), name, author, a short description, its
category, how many installs it has, and an **Install** / **Uninstall** button.

### Finding a plugin

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

### Installing and managing

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

### Plugin logs and health

All plugin activity is written to a single unified **plugin.log**, which makes
install and runtime problems much easier to trace — see
[Help → Troubleshooting Commands](#troubleshooting-commands). FPP also tracks whether each installed plugin is official, community or
unknown, and surfaces that in the **System Health Check**.

## Packages

The **Packages** page (**Content Setup → Packages**) installs optional
operating‑system software that some workflows need but that is not part of the
base image. This keeps the base image lean while still allowing advanced setups to
add what they require.

![The Packages page.](images/packages.png)

## Scripts and the Script Repository

Scripts are small programs that perform specific functions. They can be used
within a playlist, from a Command Preset, the Scheduler or a GPIO input, or as
part of a plugin.

You write, upload, edit and run your own scripts from the **Scripts** tab of the
**File Manager** ([Content Setup → File Manager](#file-manager)). That is unaffected by the
change described below.

### The Script Repository is deprecated

**Content Setup → Script Repository Browser** used to list community scripts by
category and install them for you. In FPP 10 that in‑app browser has been
**deprecated**, and the page now shows only a notice explaining the change.

![The Script Repository page in FPP 10.](images/scriptbrowser.png)

Scripts contributed to the FPP‑sanctioned `fpp-scripts` repository over the years
were often never revisited or updated for later FPP versions, and most of what
they did has since been replaced by **FPP Commands**, **Pixel Overlay Models** and
better‑maintained **plugins** — so keeping a separate catalogue and installer
around no longer made sense.

The [fpp-scripts GitHub repository](https://github.com/FalconChristmas/fpp-scripts)
is still available, and its **README** documents which scripts are still relevant,
which have been replaced (and by what), and which are deprecated. If you still
need one of the historical scripts, download it from the repository by hand and
install it via the **Scripts** tab in the File Manager.

> **Note:** The Script Repository page **will be removed in FPP 11**. If any of
> your workflow depends on installing scripts from it, move to the File Manager
> route now.

> **Note:** Scripts run on the device with full access to it, so only install
> scripts you trust — the same caution that applies to plugins.

> **Tip:** Take an [FPP Backup](#fpp-backup) before installing plugins, packages or scripts, so
> you can roll back if something misbehaves.
