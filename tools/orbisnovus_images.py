"""Orbis Novus wiki pictures: one in-game shot per terrain style, dungeon kind, settlement, castle and citadel, picked
from the release's screenshot folders (a retake wins over the first take) and saved at 960 px wide into
docs/orbisnovus/img/shots/<kind>-<name>.jpg. Re-run after new shots:  python tools/orbisnovus_images.py
"""
import glob
import os
import re
import shutil

from PIL import Image

REL = "H:/AI_MC_Modding/_handoff/orbisnovus-release"
SHOTS = REL + "/screenshots/page-candidates"
WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(WIKI, "docs", "orbisnovus", "img")
# Later folders win: retakes over first takes; for terrain the eye-level vista over the aerial
# Nether shots that came out as a wall of lava
UPLOAD = os.path.expanduser("~/Desktop/UPLOAD/5-Orbis-Novus/screenshots")
# 2026-11-07 retakes (26.1.2, outside views only) from the upload folder, upload name -> wiki shot. Left out on purpose:
# far spires (vista came out empty sky), skyreach (a dark line across the frame), patchwork earth (looked like far spires), sunken temple (mostly sea), dungeons.
RETAKE = {"castle-dark-shaders": "castle-castle_dark", "castle-sand-shaders": "castle-castle_sand",
          "castle-stone-no-shaders": "castle-castle_stone"}
for _n in ("green_vale high_teeth red_steps warm_shoals verdigris_reach grey_silence painted_stillness "
           "custom_mix").split():
    RETAKE["terrain-%s-shaders" % _n.replace("_", "-")] = "terrain-" + _n
for _n in ("abstract_temple alien_temple arch castle_ruin courtyard_keep fantasy_temple giant_hand hill_fort lighthouse "
           "monastery motte ruin_field statue sun_temple windmill").split():
    RETAKE["settlement-%s-shaders" % _n.replace("_", "-")] = "settlement-" + _n
SKIP = {"dungeon-basalt_bastion", "dungeon-infernal_keep", "dungeon-soul_crypt", "settlement-nether_temple"}
ORDER = [("dungeons_a", ""), ("dungeons_b", ""), ("terrain", "-aerial"), ("terrain", "-vista1"), ("retake", "-r2")]


def main():
    os.makedirs(OUT + "/shots", exist_ok=True)
    pick = {}
    for folder, suffix in ORDER:
        for f in sorted(glob.glob("%s/%s/*.jpg" % (SHOTS, folder))):
            m = re.match(r"onshots-\d+-(\w+)-(\w+?)(-aerial\d?|-vista\d|-r2)?(-plain)?\.jpg$", os.path.basename(f))
            if not m or m.group(4) or (m.group(3) or "") != suffix:
                continue
            pick["%s-%s" % (m.group(1), m.group(2))] = f
    for key in SKIP:
        pick.pop(key, None)
    for src, key in RETAKE.items():
        pick[key] = UPLOAD + "/" + src + ".jpg"
    for key, f in sorted(pick.items()):
        im = Image.open(f).convert("RGB")
        im.resize((960, im.height * 960 // im.width), Image.LANCZOS).save(OUT + "/shots/%s.jpg" % key, quality=82)
    for src in glob.glob(REL + "/screenshots/*.jpg"):
        Image.open(src).convert("RGB").save(OUT + "/" + os.path.basename(src), quality=85)
    for name in ("terrain", "dungeons"):
        shutil.copy("%s/logo/%s/orbisnovus_%s_logo_520.png" % (REL, name, name), OUT + "/%s_logo.png" % name)
    print("%d shots: %s" % (len(pick), " ".join(sorted(pick))))


if __name__ == "__main__":
    main()
