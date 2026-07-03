# Screenshot annotations

Declarative overlays (arrows, boxes, numbered callouts, highlights, redactions)
for the manual's screenshots. The raw screenshots in `../images/` stay pristine so
`../capture.sh` can always re-shoot them; annotations are baked on at build time
into `build/images/` and flow into the `.docx`, `.pdf`, and web outputs.

## How it works

- One YAML sidecar per image, named after the image: `status.yaml` annotates
  `../images/status.png`. Files without a sidecar are used unchanged.
- Coordinates are **pixels from the top-left** of the source image. Open the
  screenshot to read them off (in Claude Code, the Read tool shows the image).
- Preview with `../annotate.sh` (writes `../build/images/`), then rebuild with
  `../generate.sh` and/or `../generate-web.sh`. Both apply annotations
  automatically — `annotate.sh` is only for checking placement.

## Annotation types

| type        | keys                                             | draws |
|-------------|--------------------------------------------------|-------|
| `box`       | `at: [x1,y1,x2,y2]`, optional `label`            | rectangle outline (+ numbered badge at the corner if `label`) |
| `circle`    | `at: [cx,cy]`, `radius`, optional `label`        | circle outline (+ badge at centre if `label`) |
| `marker`    | `at: [x,y]`, `label`                             | filled numbered callout badge |
| `arrow`     | `from: [x,y]`, `to: [x,y]`                       | arrow (head at `to`) |
| `highlight` | `at: [x1,y1,x2,y2]`                              | translucent filled rectangle |
| `text`      | `at: [x,y]`, `text: "…"`                         | text with a white halo for legibility |
| `blur`      | `at: [x1,y1,x2,y2]`, optional `radius`           | Gaussian-blur redaction of the region |

Shared optional keys on any annotation: `color` (name like `red`, `#rrggbb`, or
`[r,g,b]`; default red) and `width` (stroke thickness in px; default auto-scales to
the image size).

## Example

`status.yaml` (annotating `../images/status.png`):

```yaml
annotations:
  - {type: box,    at: [40, 70, 420, 130], color: red, label: "1"}
  - {type: arrow,  from: [600, 300], to: [470, 150], color: red}
  - {type: marker, at: [820, 96], label: "2"}
  - {type: blur,   at: [1150, 20, 1420, 60]}   # hide the hostname/IP
```
