#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the basic generation of bar plots

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# general changes to matplotlib
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'DejaVu Sans','size': 24})

pop = pd.read_csv("data/populations.txt", sep="\t")

# use the pythonic list comprehensions for getting lists of the max populations and the names
pop_name = [el for el in pop.keys()[1:]]
max_pop = [max(pop[el]) for el in pop_name]

x = np.arange(len(pop_name))

fig, ax = plt.subplots(1,1, figsize=(9,6), tight_layout=True)

# the width of the bars
width = 0.35 

box = ax.bar(x, max_pop, width, label="maximum population")

# Add some text for labels and custom x-axis tick labels, etc.
ax.set_ylabel("population count")
ax.set_xticks(x)
ax.set_xticklabels(pop_name)
ax.legend()

fig.show()
