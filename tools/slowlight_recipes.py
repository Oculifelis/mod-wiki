"""Slowlight's kiln recipe tables, written from the mod's own ageing recipes into docs/slowlight/recipes.md.

Every file in Slowlight's data/slowlight/recipe/ageing (and its compat/<mod> folders) becomes a row: what goes in, what
comes out, the days and the weather it needs. Names come from Slowlight's and vanilla 1.21.1's lang files; items from
other mods get their id title-cased. Vanilla items' pictures go into docs/slowlight/img/mc/, flat
as tools/wiki_images.py draws them (Slowlight's own come from that tool). Re-run after recipes change:  python tools/slowlight_recipes.py
"""
import glob
import json
import os
import sys
import zipfile

from PIL import Image

MODDING = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, MODDING + "/_toolkit/modelrender")
import modelrender as mr  # noqa: E402
import wiki_images as wi  # noqa: E402

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RES = MODDING + "/Slowlight/src/main/resources"
JAR = os.path.join(os.path.expanduser("~"), ".gradle", "caches", "neoformruntime", "artifacts",
                   "minecraft_1.21.1_client.jar")
OUT = os.path.join(WIKI, "docs", "slowlight")
SIZE = 128

MODS = {"twilightforest": "Twilight Forest", "undergarden": "The Undergarden", "aether": "The Aether",
        "aerialhell": "Aerial Hell"}
# Results whose item alone doesn't say what they are
SPECIAL = {"minecraft:potion": "Water Bottle", "minecraft:suspicious_gravel": "Suspicious Gravel (kiln finds)",
           "minecraft:suspicious_sand": "Suspicious Sand (kiln finds)"}
DIMENSIONS = {"minecraft:the_nether": "in the Nether", "minecraft:the_end": "in the End",
              "minecraft:overworld": "in the Overworld"}

HEAD = """# Kiln recipes

Every recipe the [kilns](kilns.md) know, read from the mod's own data. The **Patient Kiln** takes the days shown; the
**Long Kiln** takes three times as long for a whole stack; the **Ember Kiln** takes half, where the world is hot
enough. JEI shows the same list in game.

A recipe with a **condition** only counts its days while the condition holds; otherwise the wait stands still and keeps
the days it has. A recipe with a dimension exists only there, and there it wins over the same item's recipe without one
(so cobblestone turns to blackstone in the Nether and mossy everywhere else).

"""


def lang():
    names = json.load(open(RES + "/assets/slowlight/lang/en_us.json", encoding="utf8"))
    with zipfile.ZipFile(JAR) as z:
        names.update(json.loads(z.read("assets/minecraft/lang/en_us.json")))
    return names


def name(names, ident):
    if ident in SPECIAL:
        return SPECIAL[ident]
    ns, path = ident.split(":")
    for kind in ("item", "block"):
        if "%s.%s.%s" % (kind, ns, path) in names:
            n = names["%s.%s.%s" % (kind, ns, path)]
            if path.startswith("music_disc_"):  # every disc is "Music Disc"; the song is in .desc
                n = names.get("item.%s.%s.desc" % (ns, path), path).split(" - ")[-1] + " (disc)"
            if path.endswith("_smithing_template"):
                n = "Patience Armor Trim"
            return n
    return path.replace("_", " ").title()


def icon(ident, alt):
    """Markdown for an item's picture, drawing vanilla ones on the way; '' for other mods' items."""
    ns, path = ident.split(":")
    if ns == "slowlight":
        return '![%s](img/%s.png){ .mc-icon .mc-inline }' % (alt, path)
    if ns != "minecraft":
        return ""
    mc = os.path.join(OUT, "img", "mc")
    os.makedirs(mc, exist_ok=True)
    png = os.path.join(mc, path + ".png")
    if not os.path.exists(png):
        ref = "minecraft:item/" + path
        im = mr.render(ref, SIZE // 32) if not mr.model(ref)["elements"] else wi.face(RES + "/assets", "minecraft", path, ref)
        if im.size != (SIZE, SIZE):
            im = im.resize((SIZE, SIZE), Image.NEAREST)
        im.save(png, optimize=True)
    return '![%s](img/mc/%s.png){ .mc-icon .mc-inline }' % (alt, path)


def condition(c):
    if not c:
        return ""
    parts = []
    if c.get("sky") == "open":
        parts.append("open sky")
    elif c.get("sky") == "covered":
        parts.append("roofed over")
    elif c.get("sky") == "void":
        parts.append("nothing above it")
    if "weather" in c:
        parts.append({"clear": "clear weather", "rain": "rain", "thunder": "a thunderstorm"}[c["weather"]])
    if "time" in c:
        parts.append("by " + c["time"])
    if "dimension" in c:
        parts.append(DIMENSIONS.get(c["dimension"], c["dimension"]))
    if c.get("moon") in {"full", "new"}:
        parts.append(c["moon"] + " moon")
    if c.get("climate") == "cold":
        parts.append("cold biome")
    if c.get("light") == "dark":
        parts.append("dark")
    return ", ".join(parts)


def row(names, d):
    ing = d["ingredient"]["item"]
    res = d["result"]
    count = res.get("count", 1)
    ing_name, res_name = name(names, ing), name(names, res["id"])
    out = (str(count) + " × " if count > 1 else "") + res_name
    long_days = d.get("long_days", d["days"] * 3)
    requirements = condition(d.get("condition"))
    if "cellar_days" in d:
        cellar = "%d days in a cellar" % d["cellar_days"]
        requirements = ", ".join(filter(None, (requirements, cellar)))
    return res_name.lower(), "| %s %s | %s %s | %d | %d | %s |" % (
        icon(ing, ing_name), ing_name, icon(res["id"], res_name), out, d["days"], long_days,
        requirements)


def table(names, files):
    rows = sorted(row(names, json.load(open(f))) for f in files)
    return "| In | Out | Days | Long Kiln days | Condition |\n|---|---|---|---|---|\n" + "\n".join(r for _, r in rows) + "\n"


def main():
    mr.setup([RES + "/assets"], JAR)
    names = lang()
    base = RES + "/data/slowlight/recipe/ageing"
    text = HEAD + "## Slowlight and vanilla\n\n" + table(names, sorted(glob.glob(base + "/*.json")))
    text += "\n## With other mods\n\nEach of these loads only when its mod is installed.\n"
    for mod, title in MODS.items():
        files = sorted(glob.glob("%s/compat/%s/*.json" % (base, mod)))
        if files:
            text += "\n### %s\n\n" % title + table(names, files)
    open(os.path.join(OUT, "recipes.md"), "w", encoding="utf8").write(text)
    print("recipes.md: %d recipes" % len(glob.glob(base + "/**/*.json", recursive=True)))


if __name__ == "__main__":
    main()
