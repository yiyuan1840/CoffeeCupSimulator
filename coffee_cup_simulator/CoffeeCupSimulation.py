# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:46:37 2020

@author: yjia


    exp. Paper: k = 0.18 [W/m-K], ro = 930 [kg/m3]
         Gold: k = 317 [W/m-K], ro = 19300 [kg/m3]
         Silver: k = 42 [W/m-K], ro = 10500 [kg/m3]
         Stainless Steel: 14.9 [W/m-K], ro = 7900 [kg/m3]
         Aluminum Alloy: k = 168 [W/m-K], ro = 2790
         Glass: k = 1.4 [W/m-K], ro = 2500 [kg/m3]


"""
# Libraries
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from math import pi# L
from matplotlib.pyplot import figure
from CoffeeCupPhysics import CoffeeCup

# Specify Cup One Properties

CupOne = CoffeeCup(V = 16*2.9574e-5, # Cup Volume [m3]
                   A = 0.0314, # Cup Wall Surface Area [m2]
                   S = 0.00785, # Cup Top Openning Area [m2]
                   Tc = 373, # Coffee Initial Temperature [K]
                   Ta = 297, # Ambient Air Temperature [K]
                   k = 1.4, # Thermal Conductivity of Cup Wall Material [W/m-K]
                   Ro_cup = 2500, # Density of Cup Wall Material [kg/m3]
                   D = 4e-3, # Thickness of Cup Wall [m]
                   Ro = 1000, # Density of Coffee
                   C = 4190, # Specific Heat of Coffee
                   dt =1, # Time Step [s]
                   Tsip_s = 5, # Time Interval of Small Sips
                   Psip_s = 0.4, # Percentage of Small Slips
                   Tsip_l = 30, # Time Interval of Large Sips
                   Psip_l = 0.6, # Percentage of Large Sips
                   V_total = 24*2.9574e-5 # Total Volume of Coffee Consumed per Day 
                   )

Tc_hist_1 =[]
while CupOne.Tc > CupOne.Ta+1:
    Tc_hist_1.append(CupOne.Tc)
    CupOne.Tc = CupOne.solve_Tc_next
    
t_cool_CupOne = len(Tc_hist_1)*CupOne.dt
t_ls_CupOne = CupOne.calc_time_last_sip()
T_ls_CupOne = Tc_hist_1[int(CupOne.calc_time_last_sip()/CupOne.dt)]
N_CupOne = CupOne.calc_N_refills()
S_CupOne = CupOne.S
W_CupOne = CupOne.calc_total_weight()
Du_CupOne = 2
Mtn_CupOne = 1
Cbn_CupOne = 3

PI1_CupOne = 10/N_CupOne ## Number of Refills
PI2_CupOne = S_CupOne/0.01*10 ## Top Openning Area
PI3_CupOne = (T_ls_CupOne-CupOne.Ta)/40*10 ## Temperature at Last Sip
PI4_CupOne = 3/W_CupOne ## Weight of Total Cup and Coffee
PI5_CupOne = Du_CupOne ## Durability of Cup
PI6_CupOne = Mtn_CupOne ## Maitenance
PI7_CupOne = Cbn_CupOne ## Embodied Carbon

# Specify Cup One Properties

CupTwo = CoffeeCup(V = 12*2.9574e-5, 
                   A = 0.0314,
                   S = 0.0001,                                                                                                                            
                   Tc = 373,
                   Ta = 297,
                   k = 0.18,
                   Ro_cup = 930,
                   D = 1.5e-3,
                   Ro = 1000,
                   C = 4190,
                   dt =1,
                   Tsip_s = 15,
                   Psip_s = 0.4,
                   Tsip_l = 45,
                   Psip_l = 0.6,
                   V_total = 24*2.9574e-5
                   )

Tc_hist_2 =[]
while CupTwo.Tc > CupTwo.Ta + 1:
    Tc_hist_2.append(CupTwo.Tc)
    CupTwo.Tc = CupTwo.solve_Tc_next
    
t_cool_CupTwo = len(Tc_hist_2)*CupTwo.dt
t_ls_CupTwo = CupTwo.calc_time_last_sip()
T_ls_CupTwo = Tc_hist_2[int(CupTwo.calc_time_last_sip()/CupTwo.dt)]
N_CupTwo = CupTwo.calc_N_refills()
S_CupTwo = CupTwo.S
W_CupTwo = CupTwo.calc_total_weight()
Du_CupTwo = 6
Mtn_CupTwo = 5
Cbn_CupTwo = 7

PI1_CupTwo = 10/N_CupTwo
PI2_CupTwo = S_CupTwo/0.01*10
PI3_CupTwo = (T_ls_CupTwo-CupTwo.Ta)/40*10
PI4_CupTwo = 3/W_CupTwo
PI5_CupTwo = Du_CupTwo
PI6_CupTwo = Mtn_CupTwo
PI7_CupTwo = Cbn_CupTwo

# print("Time to cool down to 30 C: ", t_cool_CupTwo)
# print("Time at last sip: ", t_ls_CupTwo)
# print("Temperature at last sip: ",T_ls_CupTwo)
# print("Number of Refills: ", N_CupTwo)
# print("Top Openning of Cup:", S_CupTwo)
# print("Total Weight: ", W_CupTwo)

# hourlyResults = pd.DataFrame({
#         'Tc_CupOne': Tc_hist_1,
#         'Tc_CupTwo': Tc_hist_2,
#         })


# print (len(Tc_hist))

# hourlyResults.to_csv("Tc.csv", encoding='utf-8', index=False)    
df = pd.DataFrame({
'group': ['One','Two'],
'PI1': [PI1_CupOne, PI1_CupTwo],
'PI2': [PI2_CupOne, PI2_CupTwo],
'PI3': [PI3_CupOne, PI3_CupTwo],
'PI4': [PI4_CupOne, PI4_CupTwo],
'PI5': [PI5_CupOne, PI5_CupTwo],
'PI6': [PI6_CupOne, PI6_CupTwo],
'PI7': [PI7_CupOne, PI7_CupTwo]
})
 
 
 
# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider(row, title, color):
 
    # number of variable
    categories=list(df)[1:]
    N = len(categories)
     
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
     
    # Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )
     
    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
     
    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='grey', size=8)
     
    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([2,4,6,8], ["2","4","6","8"], color="grey", size=7)
    plt.ylim(0,10)
     
    # Ind1
    values=df.loc[row].drop('group').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)
     
    # Add a title
    plt.title(title, size=11, color=color, y=1.1)
     
# ------- PART 2: Apply to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
     
# Create a color palette:
my_palette = plt.cm.get_cmap("Set2", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title='Cup '+df['group'][row], color=my_palette(row))
