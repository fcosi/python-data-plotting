#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Whole plotting script for the basics of plotting

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np

# set general plotting rules
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'DejaVu Sans','size': 18})

# plotting limits (np.pi)
start = -np.pi
end = np.pi
steps = 100

# creating x-y arrays (np.cos)
x = np.linspace(start,end,steps)
y = np.sin(x)
y1 = np.cos(x)
exp = np.exp(x)

fig, ax = plt.subplots(1,1, tight_layout=True)

ax.plot(x,y, label="sin")
ax.plot(x, y1, label="cos")
ax.plot(x,exp, label="exp")

ax.set_xlabel("x")
ax.set_ylabel("$f(x)$")

# set the limits of the y axis
ax.set_ylim((-1.5, 1.5))

# set custom ticks on the y axis
# ax.set_yticks([-0.3, 0, 0.5])

ax.legend()

# show plot
fig.show()
fig.savefig("sin-cos-exp.pdf")
