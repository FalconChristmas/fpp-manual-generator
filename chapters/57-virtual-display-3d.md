# 3D Virtual Display

New in FPP 10, the **3D Virtual Display** renders your entire show as a live,
true‑3D model in the browser. It reads the geometry your props actually have —
including their depth (the Z axis) — and streams the sequenced pixel colours to it
in real time, so you can preview a running sequence from any angle without any
lights connected. It is ideal for testing at your desk, for demonstrating a show,
or for driving a dedicated on‑screen display.

![The 3D Virtual Display showing a running sequence in true 3D space.](images/virtual-display-3d.png)

## 2D vs. 3D virtual display

FPP has long offered a **2D Virtual Display**, which groups pixels by their
on‑screen X/Y position — pixels that sit at the same place on a flat plane share a
colour, so depth is lost. The new 3D display treats **every pixel independently**
using the Z‑axis data from your layout, so pixels at the same X/Y but different
depth (for example the front and back faces of a mega‑tree) light up separately.
The result is a faithful three‑dimensional preview you can orbit around.

Both displays are driven from the same source: the **virtualdisplaymap** that
xLights uploads to FPP.

## Requirements

The 3D display needs two things in place before its menu link appears:

1. **A layout map from xLights.** In xLights, open **FPP Connect**, tick the
   **Models** checkbox for this FPP device, and upload. This saves a
   `virtualdisplaymap` into FPP's configuration directory describing the 3D
   position of every pixel.
2. **The HTTP Virtual Display 3D output enabled** (see below). The channel count is
   detected automatically from the uploaded map, so you do not set it by hand.

## Enabling the output

Open **Input/Output Setup → Channel Outputs** and select the **Virtuals** tab. Add
an **HTTP Virtual Display 3D** output and enable it:

- **Enabled** – Yes.
- **Channel Count** – shown as **Auto**; it is taken from the virtualdisplaymap.
- **Update Interval (ms)** – how often the display is refreshed. The default is
  **25 ms** (≈ 40 fps); lower is smoother, higher is lighter on the device.

The output uses a fixed network port (32329) internally; you do not need to
configure it. Click **Save** and, when prompted, **Restart FPPD**.

Once the output is enabled, a **3D Virtual Display** entry appears in the
**Status/Control** menu (alongside **2D Virtual Display**, which shows only when the
2D output is enabled).

## Navigating the view

The display uses standard orbit controls:

- **Left mouse button – drag** to rotate the view around your display.
- **Middle mouse button (scroll‑wheel press) – drag** to pan/move the view.
- **Scroll wheel** to zoom in and out.
- **Fullscreen button** for an immersive full‑screen view; press **ESC** to exit.
- **📋 Copy View URL** captures your current camera position and settings as a
  shareable link — paste it to reopen the display at exactly that angle and zoom.

> **Tip:** If your tree models appear tilted or off‑vertical in the 3D view,
> recreate those trees in the current version of xLights and re‑upload. Older
> xLights releases generated tree geometry with alignment inaccuracies that only a
> fresh export will correct.

## URL parameters

Because the view is a normal web page, you can preset it with query parameters —
handy for a kiosk or a saved bookmark. Append them to the page URL (combine several
with `&`):

| Parameter | Effect |
|-----------|--------|
| `standalone=true` | **Full‑window visualiser with no FPP UI** — perfect for a dedicated display. |
| `cameraX`, `cameraY`, `cameraZ` | Set the exact camera position. |
| `cameraAngleH`, `cameraAngleV` | Set the horizontal/vertical camera angles (degrees). |
| `targetX`, `targetY`, `targetZ` | Set the point the camera looks at. |
| `zoom` | Zoom multiplier (`0.5` = closer, `2.0` = farther). |
| `fov` | Camera field of view in degrees (default 75). |
| `fullscreen=true` | Enter fullscreen automatically (click the page if the browser blocks it). |
| `brightness` | Pixel brightness multiplier (default 2.0). |
| `ambientLight` | Scene lighting intensity (default 1.0; `0.0` = dark). |
| `pixelSize` | Point size of each pixel (default 1). |
| `showGrid=false` | Hide the ground grid. |
| `showAxes=true` | Show the X/Y/Z axis helper. |
| `holidayMode=true` | Enable holiday animations. |

For example, a dedicated display might use:

```
virtualdisplaywrapper3d.php?standalone=true&zoom=0.8&brightness=2.5&ambientLight=0.3
```

## Uploading 3D object files

The page includes an **Upload 3D Object Files** area for adding scenery or prop
meshes to the scene — for example a model of your house or a static decoration.
Drag and drop (or select) `.obj`, `.mtl`, `.png`, `.jpg`/`.jpeg` files; they are
saved to `/home/fpp/media/virtualdisplay_assets` on the device.

> **Note:** Automatic upload of 3D object files from xLights is not yet available,
> so these assets are added manually here. The pixel layout itself always comes
> from the xLights **Models** upload described above.

## Troubleshooting

- **The menu link is missing.** Enable the **HTTP Virtual Display 3D** output on the
  **Virtuals** tab and restart FPPD; the link appears only when the output is on.
- **Nothing lights up / the display is empty.** Confirm you uploaded **Models** from
  xLights FPP Connect (this creates the `virtualdisplaymap`) and that a sequence is
  playing. Do a hard refresh (Ctrl+Shift+R) after enabling the output.
- **Pixels look grouped or flat.** That is the 2D display; make sure you opened
  **3D Virtual Display**, not 2D.
