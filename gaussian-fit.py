#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 10:14:46 2020

@author: filippo
"""

# imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# functions
def gaussian(x, mu, sigma):
    """
    Gaussian distribution
    Args:
        - x values
        - mu
        - sigma
    Returns:
        gaussian curve
    """
    return (1/(sigma*np.sqrt(2*np.pi))*np.exp(- ((x - mu)**2)/(2*sigma**2)))

fires = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/forestfires.csv', 
                   index_col=0)
temps = fires.temp
binnr = 30

vals, binedge = np.histogram(temps, bins=binnr, density=True)

# to overcome wrong positioning of the bins, compute the width of one bin and subtract half of it it to the edges
bin_width = binedge[1] - binedge[0]
bincenter = binedge[1:]- bin_width/2

# compute the fit and little information
opt_vals, cov_coeff = curve_fit(gaussian, bincenter, vals)
print("optimal expected value mu: {}\noptimal standar deviation sigma: {}".format(*opt_vals))

# =====================================================

# plot everything
mu, sigma = opt_vals[0], opt_vals[1]
gauss_fit = gaussian(bincenter, *opt_vals)
max_gauss = max(gauss_fit)

# define the plot
fig, ax = plt.subplots(1,1, figsize=(9,6), tight_layout=True)

ax.hist(temps, bins=binnr, density=True, label="temperature")
ax.plot(bincenter, vals, "ro")

label_text="$\mu$={:.3}, $\sigma^2$={:.3}".format(*opt_vals)
ax.plot(bincenter, gauss_fit, 'r-', label=label_text)

ax.set_xlabel("Temperature [$^oC$]")
ax.legend()

# find value for half max gauss
half_max_idx = np.abs(gauss_fit - max_gauss/2).argmin()
print(bincenter[half_max_idx])
starting_bin = bincenter[half_max_idx]
if starting_bin < mu:
    xmin, xmax = starting_bin, starting_bin + 2*sigma
else:
    xmax, xmin = starting_bin, starting_bin - 2*sigma

# # plot mu and sigma
ax.vlines(x=mu, color="grey", linestyle="--", ymin=0, ymax=max_gauss)
ax.hlines(y=max_gauss/2, xmin=xmin, xmax=xmax, color="grey", linestyle="--")

fig.show()