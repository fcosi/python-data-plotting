#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script for the generation of basic pie plots

@author: filippo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# general changes to matplotlib
plt.rc('text', usetex=True)
plt.rc('font', **{'family': 'Latin Modern Roman','size': 24})

pop = pd.read_csv("data/populations.txt", sep="\t")

# divide the pop of hare into five year chunks then compute the avg there
pop_name = [el for el in pop.keys()[1:]]

# take one year and look at the fractions of the populations
year = 1905
pop_one_year = pop[pop["# year"] == year]
tot_pop = float(pop_one_year.iloc[:,1:].sum(axis=1))

pop_fractions = pop_one_year.iloc[:,1:].divide(tot_pop)

fig, ax = plt.subplots()

ax.pie(pop_fractions*100, labels=pop_name, autopct="%1.1f\%%", radius=1.2)
ax.set_title("Populations in {}".format(year))


fig.show()
