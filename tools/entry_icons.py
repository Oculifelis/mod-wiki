"""A picture beside every item, block and creature in a wiki table.

    python tools/entry_icons.py <mod> <page.md> [<page.md> ...] [--dry]

For each table whose first column names things in bold (`| **Crusher** | ... |`), looks each name up in the mod's
lang file, writes docs/<mod>/img/<id>.png if it isn't there yet, and adds a first column with the picture
(`![Crusher](img/crusher.png){ .mc-icon }`), the same shape as the Ostentum and Slowlight item tables.

Items are their flat inventory sprite from the mod's own texture files (wiki_images.picture: nearest-neighbour, 128 px).
Blocks start as their flat front face and creatures as their spawn egg; both are replaced by real in-game cut-outs
(_toolkit/mobshots) whose names are then listed in game_shots.txt so nothing here overwrites them.
Names that aren't in the lang file go in ALIASES below, or are reported and left without a picture.
Prints every block and creature id it used, for the next mobshots run (`--shots FILE` appends them to FILE).
"""
import json
import os
import re
import sys
import zipfile

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wiki_images as wi  # noqa: E402

MODDING = wi.MODDING
INST = os.path.join(os.environ["APPDATA"], "PrismLauncher", "instances", "Orbis Novus Shots Modded", "minecraft", "mods")
UPLOAD = os.path.join(os.path.expanduser("~"), "Desktop", "UPLOAD")
CLIENT = os.path.join(wi.JARS, "minecraft_26.1.2_client.jar")


def jar(prefix):
    hits = sorted(f for f in os.listdir(INST) if f.startswith(prefix) and f.endswith(".jar"))
    return os.path.join(INST, hits[-1]) if hits else None


FF = MODDING + "/Fieldframe"
PENDING = MODDING + "/_handoff/pending-install"
# mod -> namespaces, asset folders (newest first), jars searched after them
MODS = {
    "fieldframe": (["fieldframe"], [FF + "/shared/assets", FF + "/neoforge-26.1.2/src/main/resources/assets"],
                   [jar("fieldframe-0"), CLIENT]),
    "fieldframe-frameworks": (["fieldframe_frameworks", "fieldframe"],
                              [FF + "/frameworks/shared/assets", FF + "/shared/assets"],
                              [jar("fieldframe-frameworks"), jar("fieldframe-0"), CLIENT]),
    "fieldframe-transit": (["fieldframe_transit", "fieldframe"], [], [jar("fieldframe-transit"), jar("fieldframe-0"), CLIENT]),
    "metallurgy": (["metallurgy"], [], [PENDING + "/metallurgy-recast-26.1.2-neoforge-1.4.2.jar", jar("Metallurgy-Reforged"), CLIENT]),
    "floraferox": (["floraferox"], [], [jar("floraferox"), CLIENT]),
    "arcanavaria": (["arcanavaria"], [], [PENDING + "/arcanavaria-26.1.2-0.7.5.jar", jar("arcanavaria"), jar("thaumaturge"), CLIENT]),
    "netheragriculture": (["netheragriculture"], [MODDING + "/NetherAgriculture/common/src/main/resources/assets"], [CLIENT]),
    "complicatedbees": (["complicated_bees"], [], [os.path.join(UPLOAD, "23-Complicated-Bees-Unofficial", "jars",
                                         "complicated_bees-neoforge-3.6.2+26.1.2-port.5.jar"), CLIENT]),
    "mariculture": (["mariculture"], [], [PENDING + "/mariculture-0.5.0+mc26.1.2-neoforge.jar", jar("mariculture"), CLIENT]),
}

# page name -> "ns:id" where the page's wording isn't the lang name
ALIASES = {
    "Fluid Armor": "fieldframe:gold_fluid_chestplate", "Blueprints": "fieldframe:blueprint_sheet",
    "Bolted Chassis": "fieldframe:frame_bolt", "Transit Tube": "fieldframe_transit:transit_tube",
}


def read_any(roots, jars, rel):
    for r in roots:
        p = os.path.join(r, rel)
        if os.path.exists(p):
            return open(p, "rb").read()
    for j in jars:
        if j:
            try:
                return zipfile.ZipFile(j).read("assets/" + rel)
            except KeyError:
                pass
    return None


SKIP_KINDS = {"enchantment", "effect", "container", "gui", "death", "advancements", "advancement", "jei", "tooltip", "key",
              "subtitles", "biome", "attribute", "config", "itemGroup", "creativetab", "fluid_type", "message", "command"}


def names(mod):
    """lower-case display name -> (kind, ns, id), items before blocks so a block's own item name wins either way."""
    nss, roots, jars = MODS[mod]
    out = {}
    for ns in reversed(nss):
        raw = read_any(roots, jars, ns + "/lang/en_us.json")
        if not raw:
            continue
        for k, v in json.loads(raw).items():
            m = re.match(r"([a-z_]+)\.%s\.([a-z0-9_/]+)$" % ns, k)
            if m and not m.group(2).endswith(("desc", "tooltip")) and m.group(1) not in SKIP_KINDS:
                kind = m.group(1) if m.group(1) in ("block", "entity") else "item"
                rank = {"block": 3, "entity": 3, "item": 2}.get(m.group(1), 1)
                key = re.sub("§.", "", v).lower()
                if key not in out or rank >= out[key][3]:
                    out[key] = (kind, ns, m.group(2), rank)
    out = {k: v[:3] for k, v in out.items()}
    return out


CUR = None


def setup(mod):
    global CUR
    CUR = mod
    nss, roots, jars = MODS[mod]
    wi.mr.setup(roots, *[j for j in jars if j])


def has_item(mod, ns, ident):
    nss, roots, jars = MODS[mod]
    return any(read_any(roots, jars, "%s/%s/%s.json" % (ns, d, ident)) for d in ("items", "models/item"))


def make(mod, kind, ns, ident):
    out = os.path.join(wi.WIKI, "docs", mod, "img", ident + ".png")
    if os.path.exists(out) or "%s/%s" % (mod, ident) in wi.GAME_SHOTS:
        return out
    os.makedirs(os.path.dirname(out), exist_ok=True)
    nss, roots, jars = MODS[mod]
    if kind == "entity":
        raw = read_any(roots, jars, "%s/textures/item/%s_spawn_egg.png" % (ns, ident))
        if raw is None:
            return None
        import io
        im = Image.open(io.BytesIO(raw)).convert("RGBA")
        im.resize((wi.SIZE, wi.SIZE), Image.NEAREST).save(out, optimize=True)
        return out
    asset = roots[0] if roots else None
    try:
        im = wi.picture(asset or "", ns, ident)
    except Exception:  # noqa: BLE001  no item model: a block with no item of its own, seen flat from the front
        try:
            im = wi.face(asset or "", ns, "", "%s:block/%s" % (ns, ident)).resize((wi.SIZE, wi.SIZE), Image.NEAREST)
        except Exception as e:  # noqa: BLE001
            print("  no picture for %s:%s (%s)" % (ns, ident, e))
            return None
    im.save(out, optimize=True)
    return out


BOLD = re.compile(r"^\*\*\[?([^*\]]+?)\]?(?:\([^)]*\))?\*\*")
SEP = re.compile(r"^\|[\s:|-]+\|?\s*$")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def annotate(mod, path, dry=False, shots=None):
    lookup = names(mod)
    lines = open(path, encoding="utf-8").read().split("\n")
    out, i, missing, used = [], 0, [], set()
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("|") and i + 1 < len(lines) and SEP.match(lines[i + 1]):
            j = i + 2
            while j < len(lines) and lines[j].startswith("|"):
                j += 1
            rows = lines[i + 2:j]
            firsts = [cells(r)[0] for r in rows]
            if PLAIN:
                firsts = [f if BOLD.match(f) or not resolve(lookup, f) else "**%s**" % f for f in firsts]
            if rows and not any("![" in r or "<img" in r for r in rows) and sum(bool(BOLD.match(f)) for f in firsts) * 2 >= len(rows)                     and any(BOLD.match(f) and resolve(lookup, BOLD.match(f).group(1).strip()) for f in firsts):
                out.append("|  " + ln)
                out.append("|---" + lines[i + 1])
                for r, f in zip(rows, firsts):
                    m = BOLD.match(f)
                    pic = ""
                    if m:
                        name = m.group(1).strip()
                        hit = resolve(lookup, name)
                        if hit:
                            kind, ns, ident = hit
                            p = None if dry else make(mod, kind, ns, ident)
                            if p or dry:
                                pic = "![%s](img/%s.png){ .mc-icon }" % (name, ident)
                                used.add((kind, ns, ident))
                        if not pic:
                            missing.append(name)
                    out.append("| " + pic + " " + r)
                i = j
                continue
        out.append(ln)
        i += 1
    if not dry:
        open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print("%s: %d pictured, %d missing %s" % (os.path.relpath(path, wi.WIKI), len(used), len(missing), missing))
    for kind, ns, ident in sorted(used):
        if kind != "item" and shots is not None:
            shots.append("%s %s:%s" % ("mob" if kind == "entity" else "block", ns, ident))
    return missing


PROSE_BOLD = re.compile(r"(?<![)\]}] )\*\*([A-Z][A-Za-z' -]+?):?\*\*")


def resolve(lookup, name):
    hit = ALIASES.get(name)
    if isinstance(hit, str):
        ns, ident = hit.split(":")
        return ("block" if any(v[2] == ident and v[0] == "block" for v in lookup.values()) else "item", ns, ident)
    for n in (name, name[:-1] if name.endswith("s") else None, name[:-2] if name.endswith("es") else None,
              name + " ingot"):  # a metal's name alone means its ingot
        if n and n.lower() in lookup:
            hit = lookup[n.lower()]
            if hit[0] == "entity" or not CUR or has_item(CUR, hit[1], hit[2]) or                     read_any(MODS[CUR][1], MODS[CUR][2], "%s/models/block/%s.json" % (hit[1], hit[2])):
                return hit
    return None


def prose(mod, path, dry=False, shots=None):
    """First bold mention of each known thing outside tables and headings gets a small picture in front of it."""
    lookup = names(mod)
    text = open(path, encoding="utf-8").read()
    seen = set(re.findall(r"img/([a-z0-9_]+)\.png\)\{ \.mc-icon", text))
    used, out = set(), []
    for ln in text.split("\n"):
        if not ln.startswith(("|", "#", "!", "    ", "```")):
            def sub(m):
                hit = resolve(lookup, m.group(1))
                if not hit or hit[2] in seen:
                    return m.group(0)
                if not dry and not make(mod, *hit):
                    return m.group(0)
                seen.add(hit[2]); used.add(hit)
                return "![%s](img/%s.png){ .mc-icon .mc-inline } %s" % (m.group(1), hit[2], m.group(0))
            ln = PROSE_BOLD.sub(sub, ln)
        out.append(ln)
    if not dry:
        open(path, "w", encoding="utf-8", newline="\n").write("\n".join(out))
    print("%s (prose): %d pictured %s" % (os.path.relpath(path, wi.WIKI), len(used), sorted(u[2] for u in used)))
    for kind, ns, ident in sorted(used):
        if kind != "item" and shots is not None:
            shots.append("%s %s:%s" % ("mob" if kind == "entity" else "block", ns, ident))


PLAIN = "--plain" in sys.argv  # also plain (not bold) first cells that name a known thing


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    shots_file = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--shots=")), None)
    mod, pages = args[0], args[1:]
    setup(mod)
    shots = []
    for p in pages:
        annotate(mod, p, dry, shots)
        if "--prose" in sys.argv:
            prose(mod, p, dry, shots)
    if shots_file and shots:
        with open(shots_file, "a", encoding="utf-8") as f:
            f.write("\n".join(sorted(set(shots))) + "\n")


if __name__ == "__main__":
    main()
