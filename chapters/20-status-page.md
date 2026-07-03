# The Status Page

The **Status/Control** menu holds the day‑to‑day settings, status reports and
playback control of your FPP device. Its first entry — and the default page that
loads when you log into FPP — is the **Status Page**. Depending on which mode FPP
is running in, **Player** or **Remote**, the screen looks a little different.

> **Note:** Depending on your FPP device, hardware and UI Level, your options may
> differ slightly from those shown here.

![The Status page in Player mode.](images/status.png)

## The header bar

The header appears on every page and gives at‑a‑glance status. The numbered
callouts above correspond to:

1. **Logo and version** – the FPP logo with the version number beside it; the
   version links to the *System Upgrade* page.
2. **Host name** – the device's configured host name.
3. **Player state** – whether FPP is idle or playing.
4. **Sensors** – readings such as CPU temperature.
5. **IP addresses** – the device's active network addresses.
6. **Time** – the device's current date and time.

*Press F1 for help* (top right) opens context‑sensitive help for the current page.

## Player Status Page

There are several sections on the Player Status page.

### Scheduler Status

This section shows the status of your Scheduler and options to control a playlist
that is playing.

1. **Current Playlist** – shows the currently playing playlist. If nothing is
   playing it shows **Idle**. If the playlist was started by hand it shows
   *(Manually Started)* after the name.
2. **Playlist time extension** – you can manually extend (or reduce) a *scheduled*
   playlist that is running. Click **Extend** to change the scheduled end time in
   minutes (use a negative number to shorten it); a second button extends in
   5‑minute increments. You can extend the end time by at most **720 minutes (12
   hours)** or reduce it by **360 minutes (3 hours)**. Once a playlist has reached
   its scheduled end time this option is no longer available, even if a song is
   still finishing (a graceful shutdown).
3. **Playlist Started at** – the time the scheduled show started.
4. **Stop Type** – the stop strategy for the scheduled playlist that is currently
   playing, and the time it is scheduled to stop.
5. **Next Playlist** – the next scheduled playlist, with the start time and day
   it will begin.
6. **Preview** – shows a graphical representation of your schedule for the next 4
   weeks (extendable via an advanced setting in *FPP Settings*). A good way to
   verify your schedule.
7. **Start Next** – ends the current playlist immediately and starts the next
   scheduled playlist. That playlist still ends at its normally scheduled time.
8. **Abnormal Conditions** – if FPP detects conditions that can affect
   performance, the messages are listed here. These almost always need to be
   remedied for your show to run properly; see the *Help and Troubleshooting*
   chapter for common messages and fixes.

### Player Status

1. **Player Status** – lists the sequence/song currently playing. It also shows a
   "breadcrumb" when an inserted playlist is playing — for example when using
   Remote Falcon, or an FPP Command such as a push‑button that inserts a playlist
   into your normal playlist.
2. **Playlist / Sequence Selector** – shows the playlist that is playing;
   otherwise use it to select a playlist, an individual sequence, or an
   individual media file to play manually.
3. **Player controls** – control the currently queued playlist:
    a. **Play** – play the queued playlist from the selected element. If
       **Repeat** is ticked it keeps playing until stopped manually or a
       scheduled playlist starts.
    b. **Previous** – step to the previous playlist item.
    c. **Next** – step to the next playlist item.
    d. **Stop Gracefully** – finish the current song, then stop.
    e. **Stop After Loop** – stop when the end of the current playlist loop is
       reached.
    f. **Stop Now** – stop immediately.
4. **Repeat** – if ticked when you manually start a playlist or sequence, it
   keeps playing until stopped manually.
5. **Volume** – controls the output volume for the currently playing sequence.
   Useful for setting the level fed to an FM transmitter or external speakers.
6. **Song Status** – shows how long the current song has been playing and how
   much time remains; it also indicates if the playlist is set to random order.

If nothing is playing the status is **Idle**. It also indicates when a playlist
is shutting down gracefully (finishing the song, then stopping).

Two display options refine the view during playback:

- **Verbose Playlist Item Details** – show much more information for each playlist
  item (helpful for seeing all the arguments of scripts or FPP Commands).
- **Auto Scroll Playlist Item** – with many items, keep the currently playing
  item visible in the window.

### Playlist Details

This section shows the details of the currently selected playlist (see the
*Playlists* chapter for more).

1. **Lead In** – any Lead In items, with total items and per‑item durations.
2. **Playlist Status** – how long the current item has been playing and how much
   time is left.
3. **Main Playlist** – an overview of the Main playlist: number of items and
   total duration.
4. **Playlist Details** – every item in the Main playlist, showing sequence name
   and associated audio file; the currently playing item is highlighted.
5. **Lead Out** – any Lead Out items, with total items and per‑item durations.

## Remote Mode Status Page

When **FPP Mode** is set to **Remote**, the Status page instead reflects
synchronisation with a player:

1. **Abnormal Conditions** – as above, any conditions that need remedying.
2. **Remote Status** – the Remote‑mode sync status: whether it is actively
   syncing to a player, elapsed time for the current sequence, and time
   remaining.
3. **Player IP** – which device is sending the sync packets, with its IP address
   (a hyperlink to that device) and host name.
4. **Sequence Filename** – the currently playing sequence.
5. **Media Filename** – the media (audio/video) file being played, if any.
6. **Volume** – controls the volume of media played on this remote.
7. **MultiSync Packet Counts** – all of the sync messages received from other
   devices. **Live Update Stats** refreshes every second; **Update** refreshes
   once; **Reset** clears the history. Columns include:
    a. **Host** – IP addresses of devices that have communicated with this one.
    b. **Last Received** – the last day/time communication was received.
    c. **Sequence Sync** / **Media Sync** – stats for sequence and media sync
       messages.
    d. **Blank Data** – stats for blanking data received.
    e. **Ping** – devices that have pinged this remote.
    f. **Plugin** / **FPP Cmd** – stats for plugin and FPP‑command messages.
    g. **Errors** – any errors encountered.

## Channel Inputs Status Section

If you have **Channel Inputs** enabled (see the *Channel Inputs* chapter) and FPP
has received input data, an additional panel appears in the lower part of the
Status page — the **E1.31 / DDP / ArtNet Packets and Bytes Received** table. It
shows the configured universes / DDP data and packet statistics per row:
**Universe**, **Start Address**, **Packets**, **Bytes** and **Errors**. **Live
Update Stats** refreshes every second, **Update** refreshes once, and **Reset**
clears the counters.

## Current Monitor

If your FPP device has eFuses (electronic fuses) and supports current‑monitoring,
a **Current Monitor** tab is available under *Status/Control*. It shows the
measured current draw per port, which is useful for spotting shorts and balancing
power. (This requires cape hardware that reports current monitoring — see the
*Capes* appendix.)

## Bottom action bar

The buttons along the bottom of the page apply to the whole device:

- **Run FPP Command** – run any FPP command manually (the same commands available
  to presets, the scheduler and the API — see *Commands, Effects and Testing*).
- **FPP Mode** – switch the device between **Player**, **Remote** and other modes.
  Changing mode restarts the FPP daemon.
- **Reboot** / **Shutdown** – restart or safely power down the device.
- **Restart FPPD** – restart just the FPP daemon (needed after some changes).
- **Stop FPPD** – stop the FPP daemon.

> **Note:** When a change requires it, a banner appears prompting you to **Restart
> FPPD** or **Reboot**. Output does not resume until the requested action is done.
