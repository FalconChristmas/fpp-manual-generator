# File Manager

The **File Manager** is where you manage the personalised files on your FPP —
uploading, downloading and, in some cases, editing them. Open **Content Setup →
File Manager**. The upper‑right of the screen shows the number of items of the
selected type, and you can show or hide the filtering option.

![The File Manager.](images/filemanager.png)

> **Note:** The available options depend on the FPP mode (Player or Remote).

## Uploading files

Upload files by dragging them from your computer's file manager onto the **Drag &
Drop or Select Files to upload** area. FPP shows each file on the tab appropriate
to its type; anything that does not match a standard type appears on the
**Uploads** tab. Sort the list with the up/down icons, and, when filtering is
enabled, type in the box to filter.

> **Tip:** xLights **FPP Connect** can upload sequences and media directly, so for
> everyday sequencing you often will not need the File Manager by hand.

## File categories

Files are grouped into tabs. Most tabs share **Clear**, **Download**, **Rename**
and **Delete**; the type‑specific options are noted below.

- **Sequences** – your `.fseq` files. Options include **Play** / **Play Here**
  (Player mode only), **Sequence info** (version, compression, frame rate, …), and
  **Add To Playlist** (appends to the selected playlist without checking for
  duplicates).
- **Audio** – audio files. **Listen** plays the file on your computer; **MP3Gain**
  normalises the levels of the selected files; **Add To Playlist** as above.
- **Video** – video files. **View** plays the file on your computer; **Video info**
  shows codec, aspect ratio, duration, etc.; **Add To Playlist** as above.
- **Images** – image files, with **View**.
- **Effects** – effect sequences (`.eseq`), with **Sequence info**.
- **Scripts** – shell scripts, with **View**, **Run** (useful for testing),
  **Edit** (edit the code in the browser), **Copy** (duplicate under a new name),
  and **Add To Playlist**.
- **Logs** – system logs for troubleshooting. **Zip** bundles all logs into a
  download; **View** shows a log; **Tail** shows just the last 50 lines.
- **Uploads** – files that do not fit the standard formats, including `.fppos`
  upgrade files; supports **Copy**.
- **Crash Reports** – crash reports FPP has generated. FPP 10 keeps these on the
  device even when you have chosen not to send crash data to the developers (see
  *FPP Settings → Privacy*), so you can inspect one yourself or attach it to a
  support request.
- **Backups** – any manual backups you have created (see *Backup, Restore and
  Proxies*).
- **Config** – FPP's own configuration files. **View** shows a file and **Edit**
  opens it in an in‑browser editor to change and save directly. This is the same
  content the JSON configuration backup captures.

  > **Warning:** Editing configuration files by hand bypasses every check the
  > normal settings pages make, and a malformed file can stop FPP starting. Take
  > an *FPP Backup* first, and prefer the proper settings page whenever one
  > exists.

> **Tip:** Watch free space (shown in the header warnings and on *FPP Settings →
> Storage*). Large video files and many sequences can fill smaller SD cards.
