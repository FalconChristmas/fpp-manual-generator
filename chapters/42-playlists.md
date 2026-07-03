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
**Type**:

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
- **Script** – run a script (pre‑written or your own; see *Script Repository
  Browser*).
- **Sequence Only** – sequence data with no media (e.g. an animation).
- **URL** – send URL commands to outside programs (e.g. switch a smart power strip,
  or post the current song to a website).

Drag items to reorder them, including between sections. Hover over an item for
**Edit** and **delete** options. Save the playlist when done; it is then available
on the Status page and to the Scheduler.
