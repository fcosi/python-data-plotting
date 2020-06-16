#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 11:06:37 2020

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np

# plotting limits (np.pi)
start = 0
end = 10
steps = 100

x = np.linspace(start,end,steps)
y = np.sin(x)

plt.plot(x,y)