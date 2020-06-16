#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Whole plotting script for plotting an array of plots

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# general changes to matplotlib
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'DejaVu Sans','size': 24})

pop = pd.read_csv("data/populations.txt", sep="\t")

# generally reccomended to use ax to adress more plots
fig2, axarr = plt.subplots(3, 1, figsize=(10,10), sharex='col', sharey=False,
                           tight_layout=True)

for ind, el in enumerate(pop.keys()[1:]):
    axarr[ind].plot(pop['# year'], pop[el], 'b--', marker="x", label=el) 
    axarr[ind].legend()
    axarr[ind].set_ylabel("population")

axarr[2].set_xlabel("year")

fig2.savefig("populations.pdf")
fig2.show()
