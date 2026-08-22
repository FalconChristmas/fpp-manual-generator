# Playlists

A playlist can be far more than a list of songs — it is one of FPP's most
versatile features. A **playlist** is an organised group of sequences, commands,
scripts, videos and more, played in a particular order, and it is where you
combine everything to create your light show. You can keep several playlists for
different time frames or days, and you can even nest a playlist within a playlist.
Open **Content Setup → Playlists**.

![The Playlists page.](images/playlists.png)

Hover over a playlist to **edit** or **delete** it; click it to open the editor.
Click **New Playlist** to create one, entering a name and an optional description.

> **Note:** A warning icon on a card indicates the playlist references media or
> sequences that are missing from this device.

## Playlist options

Once a playlist is open, hover over its name for an **Edit** button, and use the
options at the top right:

- **Settings** – edit saved settings such as the description, **Verbose** details,
  and **Randomize**:
    - **Off** – play in the configured order.
    - **Once Per Load** – randomise each time the playlist begins.
    - **Every Iteration** – randomise after each song (with logic to prevent the
      same song playing back‑to‑back).
- **Playlist Actions** – **Copy Playlist**, **Rename Playlist**, **Randomize
  Playlist** (reorder now), **Reset Playlist** (revert to the saved version), and
  **Delete Playlist**.

## The three sections

A playlist has three sections, each showing its item count and total duration:

- **Lead In** – plays once when the playlist starts (e.g. to activate items before
  the show, or a one‑time announcement). It does **not** repeat even when Repeat is
  selected.
- **Main Playlist** – your main items; this section repeats when Repeat is selected
  in the Scheduler or on the Status page.
- **Lead Out** – plays once when the playlist ends (e.g. to switch things off, or a
  closing announcement).

## Adding entries

Adding to any section is the same: click **Add a Sequence/Entry** and choose a
**Type**. FPP 10 redesigned this editor: instead of one long list of fields, the
entry's options are grouped into labelled **sections**, and individual fields
carry **help tooltips** explaining what they expect — hover the question mark
beside a field to read it.

The available types are:

- **Sequence and Media** – the most common entry: an `.fseq` plus its associated
  audio and/or video (with a **Video Out** option).
- **Branch** – change the playlist while it runs, branching to another position
  based on test conditions (e.g. lowering the volume at a certain time of day).
  Several test conditions and settings are available.
- **Dynamic** – items created on the fly by an outside script, plugin or process.
- **FPP Command** – run any FPP Command as a playlist item (see *Command Presets*).
- **Image** – display images through the HDMI port (a virtual "picture frame").
  Enter `/home/fpp/media/images` to use all images (played in random order), or an
  individual file name; choose a transition, and add a **Pause** entry for how long
  each image shows.
- **Media Only** – play media with no lights controlled (e.g. pictures on a matrix
  or TV).
- **Pause** – wait for a set time.
- **Playlist** – embed a playlist within a playlist (e.g. a shared Lead In playlist
  reused by several daily playlists).
- **Remap** – remap channels to another range, handy if you move a prop to a
  different port and cannot rebuild the sequence.
- **Script** – run a script from the File Manager's *Scripts* tab (see *Plugins,
  Packages and Scripts*).
- **Sequence Only** – sequence data with no media (e.g. an animation).
- **URL** – send URL commands to outside programs (e.g. switch a smart power strip,
  or post the current song to a website).

Drag items to reorder them, including between sections. Hover over an item for
**Edit** and **delete** options. Save the playlist when done; it is then available
on the Status page and to the Scheduler.

## Companion media

New in FPP 10, a media entry can carry **companion media** — extra audio or video
that starts and stops with it, on its own stream slot. A playlist item that shows
a badge for extra media is running one or more companions.

The usual reasons to want this are a second audio feed (an alternate‑language
soundtrack, or a feed for a lobby or indoor speaker) or a second display running
alongside the main show. Each companion names its own media file and slot, and can
be told to stay in sync with the main entry or to target a particular video
output.

Before FPP 10 you could approximate this by firing a *Play Media* command from a
start‑of‑entry hook and a matching *Stop Media Slot* from a stop hook — but
anything that ended the entry another way (the media finishing by itself, **Stop
Now**, a playlist change, or a pause) left the companion still playing. Declaring
the companion on the entry gives it exactly the entry's lifetime instead: it stops
when the entry stops however that happens, and it is restarted at the right offset
when the entry is paused and resumed.
