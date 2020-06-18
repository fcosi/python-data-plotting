#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the generation of three types of 2D surface plots

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import the color module for the colormap
from matplotlib import cm

# general changes to matplotlib
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'Latin Modern Roman','size': 24})

# define x and y space
steps = 100
x = np.linspace(-np.pi, np.pi, steps)
y = np.arange(-2*np.pi, 2*np.pi, 0.1)

# create meshgrid
X, Y = np.meshgrid(x, y)

Z = np.cos(X) + np.sin(Y)**2 + X*Y/4

fig, (ax1, ax2) = plt.subplots(2, figsize=(6,10), sharex=True)

colormap = cm.viridis 
# cm.seismic

twoD1 = ax1.pcolormesh(X, Y, Z, cmap=colormap)
twoD2 = ax2.contourf(X, Y, Z, cmap=colormap)

# add contourlines to the second plot
cont_colors = [ "red", "green", "white", "blue", "black"]
contlines = ax2.contour(X, Y, Z, levels = [-3, -1, 0, 1, 3], linewidth=5.0, colors=cont_colors)

# create the colorbar
cbar1 = fig.colorbar(twoD1, ax=ax1, label = "height")
cbar2 = fig.colorbar(twoD2, ax=ax2, label = "Z")

# some text cosmetics
ax1.set_title("pcolormesh")
ax2.set_title("contourf")
ax2.set_xlabel("X")
ax1.set_ylabel("Y")
ax2.set_ylabel("Y")


fig.show()
