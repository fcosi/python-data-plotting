#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the generation of a linear relationship with some random noise and its fit

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def fitting_lin_slope(x, a, c):
    return a * x + c

# create a random linear dataset
N = 100
x = np.linspace(0, 1, N)
randnr = np.random.rand(N)
y = - x + 2.0 + (randnr*0.5)

opt_vals, cov_coeff = curve_fit(fitting_lin_slope, x, y, bounds=([-4,-5], [2,5]))

print("optimal a = {}\noptimal c = {}\n\nstd of a = {}\nstd of c = {}".
      format(opt_vals[0], opt_vals[1], *np.sqrt(np.diag(cov_coeff))))

fig, ax = plt.subplots(figsize=(8,5), tight_layout=True)

text_label_fit = "fit a = {:.3} c = {:.3}".format(*opt_vals)

ax.plot(x, y, ".", label="data")
ax.plot(x, fitting_lin_slope(x, *opt_vals), "r-", label = text_label_fit)

ax.legend(fontsize=18)

ax.set_xlabel("x values")
ax.set_ylabel("y values")

ax.set_title("data and its fit")

fig.show()
