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
- **Search** – the single box at the top right filters as you type. At the
  **Developer** UI level it doubles as the way to load a plugin that is not in the
  list: paste the URL of its `pluginInfo.json`, or the address of its GitHub
  repository such as `github.com/owner/repo` (add `/tree/<branch>` to use a branch
  other than the default), and FPP loads its details. (Without a valid
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

Click a card to see its details and privacy disclosure without installing
anything, or **Install** to install it. **Check for Updates** re‑queries every
plugin now (the Updates tab shows its progress and how old the last answer is). Where
several plugins need attention there are bulk **Update All**, **Reinstall All**
and **Uninstall All** actions, and each installed plugin also has its own
**Reinstall**. An installed plugin gains an **Open** button that jumps straight to
its configuration page.

Plugins marked **OFFICIAL** are maintained as part of the FPP project. Each
listed plugin also shows the month it joined the plugin list — that says nothing
about how recently its code changed. A plugin
that has not been updated for this release is flagged **NOT UPDATED FOR FPP 10**
and its button changes to **Install anyway** — it may work, but it has not been
verified against FPP 10. Plugins known to be incompatible are tucked into a
collapsed **Incompatible Plugins** section at the bottom of the page rather than
cluttering the grid.

Installed plugins whose author has set it up show a **Release notes** icon next
to the privacy lights (and a link in the plugin's details), showing what has
changed — the plugin's latest GitHub release, the list of changes an Update would
bring in, or notes the plugin writes itself.

**Plugin updates.** FPP checks for plugin updates in the background (one plugin
at a time, at low priority, when someone opens the web interface and the last
answer is a few hours old). When an update is waiting, a **puzzle‑piece icon**
appears in the header of every page; hover it to see which plugins, or click it to
open the **Updates** tab. A plugin FPP could not check — its repository has moved
or needs a token, or the player is offline — is listed there with the reason,
never as up to date. Updating a plugin also installs any new dependencies it
needs, and an upgrade reloads the plugin inside FPPD rather than needing a
restart.

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

## Privacy lights {#plugin-privacy}

A plugin has full access to the player: it can change any setting, disrupt your
show, and reach anything on the networks the player is connected to. The first
time you install a plugin, FPP shows a short note saying so and asks you to
continue (once per player, and again after each major FPP upgrade).

To help you choose, each plugin's author fills in a short **privacy disclosure**,
which FPP turns into six coloured lights — small dots on the card, and in full when
you click the card or press **Install**:

| Light | Question it answers |
|---|---|
| **Sends data** | Does it send anything off this player, and to whom? |
| **Collects data** | Does it keep information about you, your household or your visitors? |
| **Camera & mic** | Does it use a camera, microphone or similar sensor, and does it record? |
| **Remote access** | Can it be reached from outside this player, or from the internet? |
| **System changes** | Does it change the player itself, beyond its own files? |
| **Source** (*Can it be checked?*) | Is all of its code somewhere anyone can look at it? |

**Green** means the author says there is nothing to report under that heading;
**amber** and **red** describe something you may want to know about, such as
sending data to an online service or including closed‑source code. **Grey** means
the author left that heading out. Hover a light to read what the author wrote, or
tap it to open **Full disclosure**. If the author has written no disclosure at
all, FPP says so in red, every light reads *not disclosed*, and the button reads
**Install anyway**.

> **Note:** The lights come from what the author wrote. Listed plugins are scanned
> automatically to compare the disclosure with the code when they join the list
> and from time to time afterwards, which catches many omissions — but it is not
> an audit, it cannot see inside closed‑source parts, and a plugin loaded from a
> URL has had no scan at all. The lights describe what a plugin says it does; they
> do not limit what it can do.

When an **update or reinstall** would change a plugin's disclosure, FPP shows you
the new one first and asks you to accept it; **Cancel** leaves that plugin as it
is. **Update All** and **Reinstall All** ask about each such plugin in turn before
anything runs.

> **Note:** If a plugin keeps information about your visitors or passers‑by —
> phone numbers, messages, votes, camera images — its *Collects data* or *Camera &
> mic* light is red, and what happens to that information is your responsibility.

## Plugin logs and health

All plugin activity is written to a single unified **plugin.log**, which makes
install and runtime problems much easier to trace — see
[Help → Troubleshooting Commands](#troubleshooting-commands). FPP also keeps an
**install history** of the plugins installed, updated and removed on the player —
including any system packages that changed while it installed a plugin's
dependencies or ran its scripts — and lists settings and packages left behind by
removed plugins; both are on the **Plugins** tab of Troubleshooting Commands. FPP also tracks whether each installed plugin is official, community or
unknown, and surfaces that in the **System Health Check**.

> **Tip:** Take an [FPP Backup](#fpp-backup) before installing plugins, packages or scripts, so
> you can roll back if something misbehaves.
