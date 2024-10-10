import yaml
import numpy as np

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
from utils import BVH

filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rest_mixamo.bvh")
output_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skeleton_mixamo.yml")

def process_skel(filename: str):
    bvh = BVH.load(filename)
    anim = bvh[0]
    offsets = anim.offsets
    parents = anim.parents
    names = bvh[1]
    print(len(names))
    return offsets, parents, names

def select_skel_by_remove(skel, remove_joints):
    _, parents, names = skel
    selected_idx, selected_parents = [], []
    for id, name in enumerate(names):
        name = name.lower()
        for joint in remove_joints:
            if joint not in name:
                selected_idx.append(id)
                selected_parents.append(parents[id])
    return selected_idx, selected_parents

def select_skel_by_name(skel, selected_joints):
    _, parents, names = skel
    selected_idx, selected_parents = [], []
    for id, name in enumerate(names):
        name = name.lower()
        for joint in selected_joints:
            if joint in name:
                selected_idx.append(id)
                selected_parents.append(parents[id])
    return selected_idx, selected_parents

if __name__ == '__main__':
    print(sys.path)
    skel = process_skel(filename)
    print(skel)
    f = open(output_filename, "w")
    print(skel[0].tolist())
    print(skel[1].tolist())
    print(skel[2])
    yaml.dump({"offsets": skel[0].tolist(), "parents": skel[1].tolist(), "names": skel[2]}, f, default_flow_style=None)
