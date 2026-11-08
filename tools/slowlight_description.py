"""Pictures for Slowlight's CurseForge and Modrinth description, served from this site so the pages can link them.

Writes docs/description/slowlight/:
  icons/<id>.png    every flat item icon, 256 px, nearest-neighbour, transparent
  renders/<id>.png  every block and 3D item seen flat (its item texture or front face, as tools/wiki_images.py
                    draws it), 256 px, transparent, plus a few block states (sealed kilns, a lit lantern, the candle burning down)
  features/<name>.png  grouped panels 720 px wide for the description column
and index.md, listing each file with its GitHub Pages and raw GitHub links. Re-run after textures change:  python tools/slowlight_description.py
"""
import json
import os
import zipfile

from PIL import Image, ImageDraw

import wiki_images as wi
from wiki_images import mr

OUT = os.path.join(wi.WIKI, "docs", "description", "slowlight")
ASSETS, JAR, ITEMS = wi.MODS["slowlight"]
LANG = json.load(open(os.path.join(ASSETS, "slowlight", "lang", "en_us.json"), encoding="utf-8"))
SHOTS = os.path.join(wi.WIKI, "docs", "slowlight", "img", "shots")

# block states drawn as extra renders: file name -> model. Only states that look different from the item in this view
# (a lit lantern, a full press or a running sandglass differ only in game lighting or on hidden faces).
STATES = {
    "patient_kiln_sealed": "slowlight:block/patient_kiln_sealed",
    "long_kiln_sealed": "slowlight:block/long_kiln_sealed",
    "ember_kiln_sealed": "slowlight:block/ember_kiln_sealed",
    "slowlight_lantern_placed": "slowlight:block/slowlight_lantern",
    "slowlight_lantern_hanging": "slowlight:block/slowlight_lantern_hanging",
}
STATES.update({"slow_candle_%d" % n: "slowlight:block/slow_candle_%d" % n for n in range(1, 5)})  # 4 is new, 1 nearly out
STATE_NAMES = {"patient_kiln_sealed": "Patient Kiln, sealed", "long_kiln_sealed": "Long Kiln, bricked shut",
               "ember_kiln_sealed": "Ember Kiln, sealed", "slowlight_lantern_placed": "Slowlight Lantern, placed",
               "slowlight_lantern_hanging": "Slowlight Lantern, hanging", "slow_candle_4": "Slow Candle, new",
               "slow_candle_3": "Slow Candle, a day burnt", "slow_candle_2": "Slow Candle, half burnt",
               "slow_candle_1": "Slow Candle, nearly out"}
FEATURE_NAMES = {"kilns": "the three kilns, sealed kilns, and Long Kilns in game",
                 "lanterns": "the Slowlight Lantern, Lanternfruit Lamp, both shards and clusters, and the lantern at night",
                 "gloamwood": "the whole Gloamwood set, its weathering steps and the nineteen plank patterns",
                 "flower_press": "the Flower Press and pressed flowers on the ground",
                 "slow_candle": "the Slow Candle burning down over four days, with an in-game shot",
                 "aerial_hell": "the ten Aerial Hell kiln foods"}
PAGES = "https://oculifelis.github.io/mod-wiki/description/slowlight/"
RAW = "https://raw.githubusercontent.com/Oculifelis/mod-wiki/main/docs/description/slowlight/"

BG, PANEL, TEXT, DIM, ACCENT = (24, 22, 34, 255), (36, 33, 50, 255), (236, 230, 214), (170, 162, 150), (242, 196, 110)
WIDTH, PAD = 720, 20


class McFont:
    """Minecraft's own text: the 8x8 glyphs of the client jar's font/ascii.png, widths measured the way the game does
    (last lit column + 1, one pixel gap, space 4), scaled by a whole number, with the game's drop shadow."""
    sheet = None

    def __init__(self, scale):
        if McFont.sheet is None:
            with zipfile.ZipFile(os.path.join(wi.JARS, JAR)) as z:
                with z.open("assets/minecraft/textures/font/ascii.png") as f:
                    McFont.sheet = Image.open(f).convert("RGBA")
        self.k = scale

    def glyph(self, ch):
        n = ord(ch)
        if ch == " " or n > 255:
            return None, 4
        g = McFont.sheet.crop((n % 16 * 8, n // 16 * 8, n % 16 * 8 + 8, n // 16 * 8 + 8))
        a = g.getchannel("A")
        cols = [x for x in range(8) if any(a.getpixel((x, y)) for y in range(8))]
        return g, (cols[-1] + 2 if cols else 4)

    def length(self, text):
        return sum(self.glyph(c)[1] for c in text) * self.k - self.k

    def draw(self, im, xy, text, fill, anchor="la"):
        x, y = xy
        if anchor == "ma":
            x -= self.length(text) / 2
        x, y = round(x), round(y)
        shade = tuple(c // 4 for c in fill[:3])
        for c in text:
            g, adv = self.glyph(c)
            if g is not None:
                mask = g.getchannel("A").resize((8 * self.k, 8 * self.k), Image.NEAREST)
                im.paste(Image.new("RGBA", mask.size, shade + (255,)), (x + self.k, y + self.k), mask)
                im.paste(Image.new("RGBA", mask.size, tuple(fill[:3]) + (255,)), (x, y), mask)
            x += adv * self.k


def name(item):
    return LANG.get("item.slowlight." + item) or LANG.get("block.slowlight." + item) or item.replace("_", " ").title()


def ref(item):
    path = os.path.join(ASSETS, "slowlight", "items", item + ".json")
    return wi.gui_model(json.load(open(path))["model"]) if os.path.exists(path) else "slowlight:item/" + item


def draw(thing, px):
    """An item id or a block model ref, px square (a whole multiple of 32 for a block, of 16 for an icon)."""
    if ":" in thing:
        im = wi.face(ASSETS, "slowlight", thing.rsplit("/", 1)[1], thing)
        return im.resize((px, px), Image.NEAREST)
    wi.SIZE = px
    return wi.picture(ASSETS, "slowlight", thing)


def is_flat(item):
    return item in wi.AERIAL_RECOLOURS or not mr.model(ref(item))["elements"]


def wrap(d, text, f, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if f.length(trial) <= width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    return lines + [line]


def panel(title, blurb, rows, shot=None, caption=None):
    """rows: (heading or None, icon px, [(thing, label or None)], optional columns) in centred rows across the panel."""
    tf, bf, lf, hf = McFont(3), McFont(2), McFont(2), McFont(2)
    scratch = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    inner = WIDTH - 2 * PAD
    blurb_lines = wrap(scratch, blurb, bf, inner)
    parts, h = [], PAD + 38 + 24 * len(blurb_lines) + 12
    for heading, px, things, *cols in rows:
        labelled = any(label for _, label in things)
        pitch = px + (36 if labelled and px < 100 else 24 if labelled else 12)
        if labelled:
            pitch = max(pitch, max(lf.length(w) for _, label in things if label for w in label.split()) + 8)
        per_row = cols[0] if cols else max(1, (inner + pitch - px) // pitch)
        if cols and labelled:  # spread a labelled row across the panel so long names fit on two lines
            pitch = max(pitch, (inner + 24) // cols[0])
        lines = max(len(wrap(scratch, label, lf, pitch - 4)) for _, label in things if label) if labelled else 0
        cell_h = px + (14 + 20 * lines if labelled else 8)
        n_rows = -(-len(things) // per_row)
        parts.append((heading, px, things, pitch, per_row, cell_h, labelled))
        h += (24 if heading else 0) + n_rows * cell_h + 10
    if shot:
        im_shot = Image.open(os.path.join(SHOTS, shot)).convert("RGBA")
        im_shot = im_shot.resize((inner, round(im_shot.height * inner / im_shot.width)), Image.LANCZOS)
        h += im_shot.height + (26 if caption else 6)
    h += PAD - 4

    im = Image.new("RGBA", (WIDTH, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, WIDTH - 1, h - 1), 18, fill=BG)
    tf.draw(im, (PAD, PAD), title, ACCENT)
    y = PAD + 38
    for line in blurb_lines:
        bf.draw(im, (PAD, y), line, TEXT)
        y += 24
    y += 12
    for heading, px, things, pitch, per_row, cell_h, labelled in parts:
        if heading:
            hf.draw(im, (PAD, y), heading, DIM)
            y += 24
        for i, (thing, label) in enumerate(things):
            used = min(per_row, len(things) - i // per_row * per_row)
            x0 = PAD + (inner - (used * pitch - (pitch - px))) // 2
            cx, cy = x0 + (i % per_row) * pitch, y + (i // per_row) * cell_h
            d.rounded_rectangle((cx - 4, cy - 4, cx + px + 3, cy + px + 3), 10, fill=PANEL)
            pic = draw(thing, px)
            im.alpha_composite(pic, (cx, cy))
            if label:
                ly = cy + px + 6
                for line in wrap(d, label, lf, pitch - 4):
                    lf.draw(im, (cx + px / 2, ly), line, TEXT, anchor="ma")
                    ly += 20
        y += -(-len(things) // per_row) * cell_h + 10
    if shot:
        im.alpha_composite(im_shot, (PAD, y))
        y += im_shot.height
        if caption:
            lf.draw(im, (WIDTH / 2, y + 8), caption, DIM, anchor="ma")
    return im


def labelled(items):
    return [(i, name(i)) for i in items]


FEATURES = {
    "kilns": lambda: panel(
        "Kilns that count in days",
        "No fuel and no screen: put something in, close it, and come back once its days have passed. The Patient "
        "Kiln holds one thing, the Long Kiln a whole stack, and the Ember Kiln works in half the days where the "
        "world is hot.",
        [(None, 128, labelled(["patient_kiln", "long_kiln", "ember_kiln"])),
         ("Sealed, while they wait", 64, [("slowlight:block/patient_kiln_sealed", None),
                                          ("slowlight:block/long_kiln_sealed", None),
                                          ("slowlight:block/ember_kiln_sealed", None)])],
        "shot_long_kilns.jpg", "Long Kilns at work"),
    "lanterns": lambda: panel(
        "Light that keeps its own hours",
        "The Slowlight Lantern is dim through the day and bright from dusk to dawn. Its shard takes a week in a kiln; "
        "the Still Shard is an ender pearl gone quiet in the End.",
        [(None, 128, [("slowlight:block/slowlight_lantern", "Slowlight Lantern"),
                      ("slowlight:block/slowlight_lantern_hanging", "Hanging"),
                      ("lanternfruit_lamp", name("lanternfruit_lamp"))]),
         (None, 64, labelled(["slowlight_shard", "still_shard", "slowlight_shard_cluster", "still_shard_cluster"]))],
        "shot_lantern_at_night.jpg", "The Slowlight Lantern at night"),
    "gloamwood": lambda: panel(
        "Gloamwood",
        "A blue-grey tree with a full set of wood. Left under open sky its planks fade, weather and silver like "
        "copper, and the stonecutter cuts them into nineteen patterns.",
        [("The full set", 64, [(i, None) for i in [
            "gloamwood_sapling", "gloamwood_leaves", "gloamwood_log", "gloamwood_wood", "stripped_gloamwood_log",
            "stripped_gloamwood_wood", "gloamwood_planks", "gloamwood_stairs", "gloamwood_slab", "gloamwood_fence",
            "gloamwood_fence_gate", "gloamwood_door", "gloamwood_trapdoor", "gloamwood_button",
            "gloamwood_pressure_plate", "gloamwood_sign", "gloamwood_hanging_sign", "gloamwood_boat",
            "gloamwood_chest_boat", "gloamwood_bookshelf"]], 7),
         ("Weathering under open sky", 64, labelled(["gloamwood_planks", "faded_gloamwood_planks",
                                                     "weathered_gloamwood_planks", "silvered_gloamwood_planks"])),
         ("Nineteen plank patterns", 64, [("gloamwood_planks_" + p, None) for p in wi.PLANK_PATTERNS], 7)]),
    "flower_press": lambda: panel(
        "Flower Press",
        "Any flower, vanilla or modded, comes out three days later as a Pressed Flower in its own colours, in one of "
        "47 petal shapes. Lay them on the ground, up to four to a block, or on a wall.",
        [(None, 128, [("flower_press", "Flower Press")])],
        "shot_pressed_flowers.jpg", "Pressed flowers on the ground"),
    "slow_candle": lambda: panel(
        "Slow Candle",
        "String, honeycomb and a copper ingot. Light it and it burns down over four days.",
        [(None, 96, [("slowlight:block/slow_candle_%d" % n, label) for n, label in
                     zip((4, 3, 2, 1), ("Day 1", "Day 2", "Day 3", "Day 4"))])],
        "shot_crafts.jpg", "Slow Candles, the Flower Press and weathered Gloamwood"),
    "aerial_hell": lambda: panel(
        "With Aerial Hell",
        "Ten kiln foods from Aerial Hell's fruit and meat. Five of the icons are drawn in game from Aerial Hell's own "
        "textures, recoloured.",
        [(None, 64, labelled(["aerial_berry_preserve", "ruby_aerial_berry_preserve", "volucite_aerial_berry_preserve",
                              "vibrant_aerial_berry_preserve", "shadow_fruit_preserve",
                              "candied_glowing_stick_fruit", "stellar_rock_sugar", "cured_phantom_meat",
                              "cured_turtle_meat", "stellar_rusk"]), 5)]),
}


def index(groups):
    md = ["# Slowlight description pictures", "",
          "Pictures for Slowlight's CurseForge and Modrinth pages. Link the GitHub Pages address; the raw GitHub one is",
          "the fallback. All are PNG with a transparent background except the feature panels, which have their own dark",
          "background. Made by `tools/slowlight_description.py`.", ""]
    heads = {"features": "## Feature panels (720 px wide)",
             "icons": "## Item icons (256 px, nearest-neighbour)",
             "renders": "## Blocks and 3D items, flat (256 px, nearest-neighbour)"}
    for sub, rows in groups:
        md += [heads[sub], "", "| | File | Shows | Links |", "|---|---|---|---|"]
        for fname, shows in rows:
            path = "%s/%s.png" % (sub, fname)
            width = 160 if sub == "features" else 48
            md.append("| ![](%s){ width=%d } | `%s` | %s | [Pages](%s%s) / [raw](%s%s) |"
                      % (path, width, path, shows, PAGES, path, RAW, path))
        md.append("")
    open(os.path.join(OUT, "index.md"), "w", encoding="utf-8", newline="\n").write("\n".join(md))


def main():
    mr.setup([ASSETS], os.path.join(wi.JARS, JAR))
    for sub in ("icons", "renders", "features"):
        os.makedirs(os.path.join(OUT, sub), exist_ok=True)
    icons, renders = [], []
    for item in ITEMS:
        sub = "icons" if is_flat(item) else "renders"
        draw(item, 256).save(os.path.join(OUT, sub, item + ".png"), optimize=True)
        (icons if sub == "icons" else renders).append((item, name(item)))
    for fname, model in STATES.items():
        draw(model, 256).save(os.path.join(OUT, "renders", fname + ".png"), optimize=True)
        renders.append((fname, STATE_NAMES[fname]))
    for fname, make in FEATURES.items():
        make().save(os.path.join(OUT, "features", fname + ".png"), optimize=True)
    index([("features", [(f, FEATURE_NAMES[f]) for f in FEATURES]), ("icons", icons), ("renders", renders)])
    print("%d icons, %d renders, %d feature panels and index.md in %s"
          % (len(icons), len(renders), len(FEATURES), os.path.relpath(OUT, wi.WIKI)))


if __name__ == "__main__":
    main()
