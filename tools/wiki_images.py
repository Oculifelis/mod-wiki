"""Item and block pictures for the wiki, drawn from each mod's own repo.

Each picture is what the inventory shows: the shared model renderer (H:/AI_MC_Modding/_toolkit/modelrender) draws a
block or 3D model in the inventory's isometric view, and a flat icon scaled up nearest-neighbour, all 128 px square
on a transparent background. The model shown is the one the item's assets/<ns>/items/<id>.json picks for the GUI.
Pictures go to docs/<mod>/img/<id>.png. Re-run after textures change:  python tools/wiki_images.py
"""
import json
import os
import sys

from PIL import Image

MODDING = "H:/AI_MC_Modding"
sys.path.insert(0, MODDING + "/_toolkit/modelrender")
import modelrender as mr  # noqa: E402

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
JARS = os.path.join(os.path.expanduser("~"), ".gradle", "caches", "neoformruntime", "artifacts")
SIZE = 128

# mod -> (assets folder in its repo, client jar for vanilla parents, item ids shown on the wiki)
MODS = {
    "ostentum": (MODDING + "/Ostentum/neoforge-26.1.2/src/main/resources/assets", "minecraft_26.1.2_client.jar", [
        # summoning saddles
        "horse_saddle", "donkey_saddle", "mule_saddle", "skeleton_horse_saddle", "zombie_horse_saddle",
        "camel_saddle", "pig_saddle", "strider_saddle", "llama_saddle", "dolphin_saddle", "nautilus_saddle",
        "happy_ghast_saddle",
        # grappling hooks
        "amethyst_hook", "diamond_hook", "ender_hook", "netherite_hook", "stillwind_hook",
        # summons
        "bone_whistle", "golem_heart", "vex_charm", "allay_chime", "hive_charm", "snow_heart", "bat_wing",
        "bottled_dragonling", "pink_pearl", "creeper_sprout", "guardian_totem",
        # whips
        "leather_whip", "vine_whip", "weeping_vine_whip", "twisting_vine_whip", "glow_berry_whip", "silk_whip",
        "chain_whip", "golden_heavy_whip", "thunderstorm_whip", "diamond_whip", "emerald_whip", "amethyst_whip",
        "royal_slime_whip", "blaze_whip", "untamed_sea_whip", "destruction_whip", "breeze_whip", "ender_whip",
        "end_rift_whip",
        # special weapons and the parts they come from
        "weathervane_spear", "pathfinders_glaive", "duelists_saber", "hearthblade", "soul_hearthblade",
        "cold_hearthblade", "echo_blade", "resonant_hilt", "frostbite_hatchet", "bloom_bow", "voidstring_bow",
        "engineers_crossbow", "bastion_crossbow", "fisher_kings_trident", "coral_trident", "abyssal_trident",
        "quake_hammer", "delvers_pick", "dormant_delvers_pick", "rusted_delvers_head", "recall_chime",
        "phantom_veil",
        # music discs and relics
        "music_disc_harvest_moon", "music_disc_enchanted_moon", "music_disc_glimmer_moon", "music_disc_fundamentum",
        "wither_relic", "elder_guardian_relic", "warden_relic", "dragon_relic",
        # records
        "record_shelf", "chiseled_record_shelf", "record_pendant",
    ]),
    "floraferox": (MODDING + "/ViolentVerdure/src/main/resources/assets", "minecraft_26.1.2_client.jar", [
        # herbs, grafting and the almanacs
        "pulseroot", "duskpetal", "moonwisp", "mirecap", "grafting_bench", "ember_graft", "rime_graft",
        "growers_almanac_1", "growers_almanac_2", "growers_almanac_3",
        # each weapon line's three tiers
        "mirecap_cleaver", "flare_cleaver", "rime_cleaver", "dusk_sceptre", "ember_sceptre", "rime_sceptre",
        "pulse_pistol", "scorch_spitter", "rime_repeater", "moonwisp_whip", "moonflare_whip", "moonrime_whip",
    ]),
}


def gui_model(node):
    """Follow an items/<id>.json model tree down the branch the inventory uses; return the model id."""
    t = node.get("type", "").replace("minecraft:", "")
    if t == "model":
        return node["model"]
    if t == "special":
        return node["base"]
    if t == "select":
        if node.get("property", "").endswith("display_context"):
            for case in node["cases"]:
                when = case["when"] if isinstance(case["when"], list) else [case["when"]]
                if "gui" in when:
                    return gui_model(case["model"])
        return gui_model(node.get("fallback") or node["cases"][0]["model"])
    if t == "condition":  # not in use, not swinging, not broken...
        return gui_model(node["on_false"])
    if t == "range_dispatch":
        return gui_model(node.get("fallback") or node["entries"][0]["model"])
    if t == "composite":
        return gui_model(node["models"][0])
    raise ValueError("can't follow item model type " + t)


def picture(assets, ns, item):
    path = os.path.join(assets, ns, "items", item + ".json")
    ref = gui_model(json.load(open(path))["model"]) if os.path.exists(path) else "%s:item/%s" % (ns, item)
    im = mr.render(ref, SIZE // 32)
    if im.size != (SIZE, SIZE):  # a 32x or 64x icon: bring it to the same size, still whole-pixel
        im = im.resize((SIZE, SIZE), Image.NEAREST)
    return im


# 3D in-hand models (whip handles, tridents) drawn by H:/AI_MC_Modding/_toolkit/wikirender at the inventory block
# angle; see its README to redraw them. They are copied here at 128 px as docs/<mod>/img/<id>_3d.png.
# mod -> (renders folder, {item id: render name})
RENDERS = MODDING + "/_toolkit/wikirender/renders"
THREE_D = {
    "ostentum": (RENDERS, dict({w: w for w in [
        "leather_whip", "vine_whip", "weeping_vine_whip", "twisting_vine_whip", "glow_berry_whip", "silk_whip",
        "chain_whip", "golden_heavy_whip", "thunderstorm_whip", "diamond_whip", "emerald_whip", "amethyst_whip",
        "royal_slime_whip", "blaze_whip", "untamed_sea_whip", "destruction_whip", "breeze_whip", "ender_whip",
        "fisher_kings_trident", "coral_trident", "abyssal_trident"]},
        end_rift_whip="ender_whip")),  # the End Rift Whip uses the Ender Whip's models
}


def main():
    for mod, (assets, jar, items) in MODS.items():
        mr.setup([assets], os.path.join(JARS, jar))
        out = os.path.join(WIKI, "docs", mod, "img")
        os.makedirs(out, exist_ok=True)
        for item in items:
            picture(assets, mod, item).save(os.path.join(out, item + ".png"), optimize=True)
        print("%s: %d pictures in %s" % (mod, len(items), os.path.relpath(out, WIKI)))
        src, renders = THREE_D.get(mod, (None, {}))
        for item, name in renders.items():
            im = Image.open(os.path.join(src, name + "_3d.png")).convert("RGBA")
            im.resize((SIZE, SIZE), Image.LANCZOS).save(os.path.join(out, item + "_3d.png"), optimize=True)
        if renders:
            print("%s: %d 3D renders" % (mod, len(renders)))


if __name__ == "__main__":
    main()
