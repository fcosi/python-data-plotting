#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:28:18 2020

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np

# general changes to matplotlib (3)
# plt.rc('text', usetex=True)
# plt.rc('font', **{'size': 24})


# plotting limits (np.pi)
start = 0
end = 100
steps = 1000

# creating x-y arrays (np.cos)
x = np.linspace(start,end,steps)
y = np.log(x)

# generate plotting instance with axes
fig, ax = plt.subplots(1,1, tight_layout=True)

# ax is one subplot instance that can be addressed
ax.plot(x,y)

# with ax one ca address many features (2)
# ax.set_xlabel("x")
# ax.set_ylabel("$\log(x)$", size=24)


# saving with savefig (4)
# fig.savefig("logarithm.pdf")
fig.show()

'''
other usefull ax methods:
    
- set_xlim((lim1, lim2))
- legend() # could make second plot
- set_xticks([])
- set_xticklabels([])
...

''' 