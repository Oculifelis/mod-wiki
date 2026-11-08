"""Offline pictures of box-UV entity models, for the bestiary: no game client.

The models are read from the Java the game itself loads (Flora Ferox's tool-written VerdureModels.java: one ModelSpec per
mob, parts with pivots, rotations and box-UV cubes) and drawn at rest in a three-quarter view with the mob's own texture
and glow sheet, by the software renderer in ViolentVerdure/tools/gen/boxrender.py (z-buffered, Minecraft's box-UV
mapping and entity lighting). The picture is drawn large and scaled down, so it comes out smooth.
"""
import os
import re
import sys
from types import SimpleNamespace

import numpy as np
from PIL import Image

_F = r"(-?[\d.]+(?:[eE]-?\d+)?)f"
_PART = re.compile(r'new Part\("(\w+)", (-?\d+), ' + ", ".join([_F] * 6) + r", new Cube\[\] \{(.*?)\}\)")
_CUBE = re.compile(r"new Cube\((\d+), (\d+), " + ", ".join([_F] * 3) + r", (\d+), (\d+), (\d+), " + _F + r", (true|false)\)")
_SPEC = re.compile(r'static final ModelSpec SPEC = new ModelSpec\("(\w+)", (\d+), (\d+), new Part\[\] \{(.*?)\n        \}\);', re.S)


def load_specs(java_path):
    """Every ModelSpec in a tool-written models file, as {name: model} in boxrender's shape."""
    models = {}
    for name, tw, th, body in _SPEC.findall(open(java_path, encoding="utf-8").read()):
        parts = []
        for pname, parent, px, py, pz, rx, ry, rz, cubes in _PART.findall(body):
            cs = [SimpleNamespace(u=int(u), v=int(v), origin=(float(x), float(y), float(z)), size=(int(w), int(h), int(d)),
                                  inflate=float(g), mirror=m == "true")
                  for u, v, x, y, z, w, h, d, g, m in _CUBE.findall(cubes)]
            parts.append(SimpleNamespace(name=pname, parent=parts[int(parent)].name if int(parent) >= 0 else None,
                                         pivot=(float(px), float(py), float(pz)), rot=(float(rx), float(ry), float(rz)),
                                         cubes=cs))
        models[name] = SimpleNamespace(name=name, tex_w=int(tw), tex_h=int(th), parts=parts)
    return models


def _texture(path, model):
    if not os.path.exists(path):
        return None
    im = Image.open(path).convert("RGBA")
    if im.size != (model.tex_w, model.tex_h):  # a hi-res sheet: sample it in the model's UV units
        im = im.resize((model.tex_w, model.tex_h), Image.NEAREST)
    return np.asarray(im)


def picture(br, model, base_png, glow_png, size=256, yaw=-35, pitch=20, supersample=4, margin=0.06):
    """The model at rest, three-quarter view from the front left and a little above, fitted into a square."""
    base, glow = _texture(base_png, model), _texture(glow_png, model)
    pose = br.Pose(model)
    view = br.view_matrix(yaw, pitch)
    # fit: project every corner once, then scale so the larger extent fills the square inside the margin
    pts = []
    for m, p in zip(br.part_matrices(model, pose), model.parts):
        for verts, _, _ in br.part_faces(p):
            pts.append((view @ ((m[:3, :3] @ verts.T).T + m[:3, 3]).T).T)
    pts = np.concatenate(pts)
    lo, hi = pts[:, :2].min(axis=0), pts[:, :2].max(axis=0)
    big = size * supersample
    scale = big * (1 - 2 * margin) / max(hi - lo)
    centre = (lo + hi) / 2
    origin = (big / 2 - centre[0] * scale, big / 2 + centre[1] * scale)
    cv = br.Canvas(big, big)
    br.render(cv, model, base, glow, pose, view, scale, origin)
    im = cv.image()
    # premultiply before shrinking so transparent edges don't bleed black into the outline
    a = np.asarray(im).astype(float)
    a[..., :3] *= a[..., 3:4] / 255.0
    small = np.asarray(Image.fromarray(a.astype(np.uint8), "RGBA").resize((size, size), Image.LANCZOS)).astype(float)
    alpha = small[..., 3:4]
    small[..., :3] = np.where(alpha > 0, small[..., :3] * 255.0 / np.maximum(alpha, 1), 0)
    return Image.fromarray(np.clip(small, 0, 255).astype(np.uint8), "RGBA")


def boxrender(gen_dir):
    sys.path.insert(0, gen_dir)
    import boxrender as br
    return br
