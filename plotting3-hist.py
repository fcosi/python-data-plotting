#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the generation of basic histrogram plots

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# general changes to matplotlib
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'DejaVu Sans','size': 24})

pop = pd.read_csv("data/populations.txt", sep="\t")

carrots = pop["carrot"]

fig, ax = plt.subplots(1,1, figsize=(9,6), tight_layout=True)

# normalized count of carrots (density=True)
ax.hist(carrots, bins=10, density=True)

ax.set_xlabel("number of carrots")
ax.set_ylabel("\# carrots / \# carrots tot")

# set a title for the plot
ax.set_title("Histogram of carrots")

fig.show()
