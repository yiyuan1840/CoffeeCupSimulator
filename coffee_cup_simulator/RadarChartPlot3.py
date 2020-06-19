# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:07:25 2020

@author: yjia
"""


# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from matplotlib.pyplot import figure
 
# Set data
df = pd.DataFrame({
'group': ['A','B','C','D'],
'Number of Refills': [38, 1.5, 30, 4],
'var2': [29, 10, 9, 34],
'var3': [8, 39, 23, 24],
'Number of Refill': [7, 31, 33, 14],
'var5': [28, 15, 32, 14]
})
 
 
figure(num=None, figsize=(12, 6), dpi=100, facecolor='w', edgecolor='k')

# ------- PART 1: Create background

# number of variable
categories=list(df)[1:]
N = len(categories)
 
# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]
 
# Initialise the spider plot
ax = plt.subplot(111, polar=True)
 
# If you want the first axis to be on top:
ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)
 
# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, rotation = 90)
# ax.set_xticklabels(categories, rotation = 45)
 
# Draw ylabels
ax.set_rlabel_position(1)
plt.yticks([10,20,30,40], ["10","20","30","40"], color="grey", size=7)
plt.ylim(0,50)
 
 
# ------- PART 2: Add plots
 
# Plot each individual = each line of the data
# I don't do a loop, because plotting more than 3 groups makes the chart unreadable
# plt.figure(figsize=(10, 10)) 
# Ind1
values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group A")
ax.fill(angles, values, 'b', alpha=0.1)
 
# Ind2
values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="group B")
ax.fill(angles, values, 'r', alpha=0.1)


# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
