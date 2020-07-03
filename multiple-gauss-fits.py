#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script to apply gaussian fit to all fire data

@author: filippo
"""

import numpy as np
import os

# import CLASS
from classes import my_functions

forest_dict = {}
for filename in os.listdir("data/"):
    if filename.endswith(".npy"):
        forest_dict[filename.split(".")[0]] = np.array(np.load("data/{}".format(filename), allow_pickle=True))
    else:
        continue

cl = my_functions.Analysis()

# testing the GaussFit()
# cl.GaussianFit(forest_dict["forest_temp"], printinfo=True, bin_nr=30, showmu=True, savefig="dummy_save_name")

for name in forest_dict.keys():
    cl.GaussianFit(forest_dict[name], showmu=True, savefig=name)
