#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
script to apply gaussian fit to all fire data

@author: filippo
"""

import numpy as np
import os

from importlib import reload

# import CLASS
# from classes import my_functions

# load data into dictionary
forest_dict = {}
for name in os.listdir("data/"):
    if name.endswith(".npy"):
        forest_dict[name.split(".")[0]] = np.array(np.load("data/{}".format(name), allow_pickle=True))
    else:
        continue
    
# apply the gauss fit


reload(my_functions)

cl = testing_class.Testing() # set here proper name
cl.GaussianFit

#
#for name in forest_dict.keys():
#    print(name)
#    cl.GaussianFit(forest_dict[name])