#!/usr/bin/env python3
"""Bake declarative annotations onto the manual's screenshots.

The raw screenshots in images/ stay pristine (so capture.sh can always re-shoot
them). Annotations are described in small YAML sidecar files under annotations/,
one per image — annotations/status.yaml annotates images/status.png. This script
mirrors every source image into an output dir and, where a sidecar exists, draws
the annotations onto that copy. The docx/pdf and web builds then point at the
output dir, so annotations appear in every deliverable without touching images/.

Usage:
    annotate.py <images_dir> <annotations_dir> <out_dir>

It is run automatically by tools/build.sh and tools/build-web.sh, and directly by
./annotate.sh for previewing. If Pillow / PyYAML are missing it degrades to a plain
copy (un-annotated) with a warning, so the manual still builds — install the deps
with ./install.sh.

Sidecar format (annotations/<image-stem>.yaml):

    # Coordinates are pixels from the top-left of the image. Read the source
    # screenshot to find them; numbers may be int or float.
    annotations:
      - {type: box,       at: [120, 80, 300, 140], color: red, label: "1"}
      - {type: arrow,     from: [400, 300], to: [520, 260], color: red}
      - {type: marker,    at: [700, 120], label: "2"}          # numbered badge
      - {type: circle,    at: [610, 200], radius: 28, color: red}
      - {type: highlight, at: [40, 40, 260, 96], color: yellow} # translucent fill
      - {type: text,      at: [200, 400], text: "Player mode", color: red}
      - {type: blur,      at: [50, 50, 250, 90]}                # redact a region

Shared optional keys: color (name / #rrggbb / [r,g,b]) and width (stroke px, else
auto-scaled to the image). "label" on box/circle/marker draws a numbered badge.
"""
import glob
import math
import os
import shutil
import sys

STDERR = sys.stderr


def warn(msg: str) -> None:
    print(f"annotate: {msg}", file=STDERR)


# Nice sans fonts to prefer for labels; fall back to Pillow's scalable default.
FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]


def load_font(size: int):
    from PIL import ImageFont

    size = max(8, int(round(size)))
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    try:
        return ImageFont.load_default(size=size)
    except TypeError:  # very old Pillow
        return ImageFont.load_default()


def to_rgb(value, default=(220, 30, 30)):
    from PIL import ImageColor

    if value is None:
        return default
    if isinstance(value, (list, tuple)):
        return tuple(int(v) for v in value[:3])
    try:
        return ImageColor.getrgb(str(value))
    except ValueError:
        warn(f"unknown color {value!r}; using default")
        return default


def text_size(draw, text, font):
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def draw_badge(draw, center, label, color, font, stroke):
    """A filled circular badge with a centred number/letter (classic callout)."""
    cx, cy = center
    tw, th = text_size(draw, label, font)
    r = max(tw, th) // 2 + max(6, stroke * 2)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color,
                 outline=(255, 255, 255), width=max(2, stroke))
    draw.text((cx - tw / 2, cy - th / 2 - stroke), label, font=font,
              fill=(255, 255, 255))


def annotate_image(src_path, dst_path, spec):
    from PIL import Image, ImageDraw, ImageFilter

    img = Image.open(src_path).convert("RGBA")
    W, H = img.size
    base_stroke = max(2, round(min(W, H) * 0.004))
    base_font = max(14, round(min(W, H) * 0.028))
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    for i, ann in enumerate(spec.get("annotations", []) or []):
        typ = str(ann.get("type", "")).lower()
        color = to_rgb(ann.get("color"))
        stroke = int(ann.get("width", base_stroke))
        font = load_font(ann.get("font_size", base_font))
        label = ann.get("label")
        label = None if label is None else str(label)

        if typ == "box":
            x1, y1, x2, y2 = ann["at"]
            draw.rectangle([x1, y1, x2, y2], outline=color, width=stroke)
            if label:
                draw_badge(draw, (x1, y1), label, color, font, stroke)

        elif typ == "highlight":
            x1, y1, x2, y2 = ann["at"]
            draw.rectangle([x1, y1, x2, y2], fill=color + (80,))

        elif typ == "circle":
            cx, cy = ann["at"]
            r = int(ann.get("radius", min(W, H) * 0.04))
            draw.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color,
                         width=stroke)
            if label:
                draw_badge(draw, (cx, cy), label, color, font, stroke)

        elif typ == "marker":
            draw_badge(draw, tuple(ann["at"]), label or str(i + 1), color, font,
                       stroke)

        elif typ == "arrow":
            (x1, y1), (x2, y2) = ann["from"], ann["to"]
            draw.line([x1, y1, x2, y2], fill=color, width=stroke)
            ang = math.atan2(y2 - y1, x2 - x1)
            hl, hw = stroke * 4.5, stroke * 3.0
            left = (x2 - hl * math.cos(ang) + hw * math.sin(ang),
                    y2 - hl * math.sin(ang) - hw * math.cos(ang))
            right = (x2 - hl * math.cos(ang) - hw * math.sin(ang),
                     y2 - hl * math.sin(ang) + hw * math.cos(ang))
            draw.polygon([(x2, y2), left, right], fill=color)

        elif typ == "text":
            x, y = ann["at"]
            # White halo so the label reads on any background.
            draw.text((x, y), str(ann.get("text", "")), font=font, fill=color,
                      stroke_width=max(2, stroke // 2), stroke_fill=(255, 255, 255))

        elif typ == "blur":
            x1, y1, x2, y2 = (int(v) for v in ann["at"])
            region = img.crop((x1, y1, x2, y2))
            radius = int(ann.get("radius", max(6, min(W, H) * 0.02)))
            img.paste(region.filter(ImageFilter.GaussianBlur(radius)), (x1, y1))

        else:
            warn(f"{os.path.basename(src_path)}: unknown annotation type {typ!r}")

    out = Image.alpha_composite(img, overlay).convert("RGB")
    out.save(dst_path)


def main(argv):
    if len(argv) != 4:
        warn("usage: annotate.py <images_dir> <annotations_dir> <out_dir>")
        return 2
    images_dir, ann_dir, out_dir = argv[1:4]
    os.makedirs(out_dir, exist_ok=True)

    # Mirror every source image first (so out_dir is a complete image set).
    srcs = [p for p in glob.glob(os.path.join(images_dir, "*"))
            if os.path.isfile(p)]
    for src in srcs:
        shutil.copy2(src, os.path.join(out_dir, os.path.basename(src)))

    specs = sorted(glob.glob(os.path.join(ann_dir, "*.yaml")) +
                   glob.glob(os.path.join(ann_dir, "*.yml")))
    if not specs:
        return 0

    try:
        import yaml  # noqa: F401
        import PIL  # noqa: F401
    except ImportError as e:
        # Fail loudly: there ARE annotations to render but we can't, so shipping
        # un-annotated images would silently drop them. (A repo with no sidecars
        # never reaches here — the build skips this step entirely.)
        warn(f"{len(specs)} annotation spec(s) in the annotations/ folder, but "
             f"'{e.name or 'Pillow/PyYAML'}' is not installed, so screenshots "
             f"cannot be annotated. "
             f"Install it (./install.sh, or: pip install pillow pyyaml) — or "
             f"remove the annotations/ sidecars. Refusing to build un-annotated.")
        return 3

    import yaml
    done = 0
    for spec_path in specs:
        stem = os.path.splitext(os.path.basename(spec_path))[0]
        src = os.path.join(images_dir, stem + ".png")
        if not os.path.exists(src):
            warn(f"{os.path.basename(spec_path)}: no matching image {stem}.png "
                 f"(skipped)")
            continue
        try:
            with open(spec_path) as fh:
                spec = yaml.safe_load(fh) or {}
            annotate_image(src, os.path.join(out_dir, stem + ".png"), spec)
            done += 1
        except Exception as e:  # keep building even if one spec is malformed
            warn(f"{os.path.basename(spec_path)}: {e} (using un-annotated image)")

    if done:
        print(f"annotate: rendered {done} annotated image(s) -> {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
