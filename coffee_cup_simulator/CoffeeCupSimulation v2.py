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
         Wood: k = 0.15 [W/m-K], ro = 640 [kg/m3] 
         Ceramics: k = 3.8 [W/m-K], ro = 3800 [kg/m3]
         Plastic: k = 0.2  [W/m-K], ro = 1390 [kg/m3]


"""
# Libraries
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from math import pi# L
from matplotlib.pyplot import figure
from CoffeeCupPhysics import CoffeeCup

# Specify Cup One Properties

CupOne = CoffeeCup(V = 11*2.9574e-5, # Cup Volume [m3]
                   A = 0.0314, # Cup Wall Surface Area [m2]
                   S = 0.00785, # Cup Top Openning Area [m2]
                   Tc = 373, # Coffee Initial Temperature [K]
                   Ta = 297, # Ambient Air Temperature [K]
                   k = 0.15, # Thermal Conductivity of Cup Wall Material [W/m-K]
                   Ro_cup = 640, # Density of Cup Wall Material [kg/m3]
                   D = 3e-3, # Thickness of Cup Wall [m]
                   Ro = 1000, # Density of Coffee
                   C = 4190, # Specific Heat of Coffee
                   dt =1, # Time Step [s]
                   Tsip_s = 60, # Time Interval of Small Sips
                   Psip_s = 0.3, # Percentage of Small Slips
                   Tsip_l = 45, # Time Interval of Large Sips
                   Psip_l = 0.7, # Percentage of Large Sips
                   V_total = 24*2.9574e-5 # Total Volume of Coffee Consumed per Day 
                   )

Tc_hist_1 =[]
while CupOne.Tc > CupOne.Ta+0.1:
    Tc_hist_1.append(CupOne.Tc)
    CupOne.Tc = CupOne.solve_Tc_next
    
t_cool_CupOne = len(Tc_hist_1)*CupOne.dt
t_ls_CupOne = CupOne.calc_time_last_sip()
try:
    T_ls_CupOne = Tc_hist_1[int(CupOne.calc_time_last_sip()/CupOne.dt)]
except IndexError:
    T_ls_CupOne = CupOne.Ta
N_CupOne = CupOne.calc_N_refills()
S_CupOne = CupOne.S
W_CupOne = CupOne.calc_total_weight()
Du_CupOne = 8
Mtn_CupOne = 5
Cbn_CupOne = 7

PI1_CupOne = 10/N_CupOne ## Number of Refills
PI2_CupOne = S_CupOne/0.01*10 ## Top Openning Area
PI3_CupOne = (T_ls_CupOne-CupOne.Ta)/60*10 ## Temperature at Last Sip
PI4_CupOne = 3/W_CupOne ## Weight of Total Cup and Coffee
PI5_CupOne = Du_CupOne ## Durability of Cup
PI6_CupOne = Mtn_CupOne ## Maitenance
PI7_CupOne = Cbn_CupOne ## Embodied Carbon

# Specify Cup Two Properties
####################################################
CupTwo = CoffeeCup(V = 11*2.9574e-5,               
                   A = 0.0314,
                   S = 0.00785,                                                                                                                           
                   Tc = 373,
                   Ta = 297,
                   k = 3.8,
                   Ro_cup = 3800,
                   D = 5e-3,
                   Ro = 1000,
                   C = 4190,
                   dt =1,
                   Tsip_s = 60,
                   Psip_s = 0.3,
                   Tsip_l = 45,
                   Psip_l = 0.7,
                   V_total = 24*2.9574e-5
                   )
#####################################################
Tc_hist_2 =[]
while CupTwo.Tc > CupTwo.Ta + 0.1:
    Tc_hist_2.append(CupTwo.Tc)
    CupTwo.Tc = CupTwo.solve_Tc_next
    
t_cool_CupTwo = len(Tc_hist_2)*CupTwo.dt
t_ls_CupTwo = CupTwo.calc_time_last_sip()
try:
    T_ls_CupTwo = Tc_hist_2[int(CupTwo.calc_time_last_sip()/CupTwo.dt)]
except IndexError:
    T_ls_CupTwo = CupTwo.Ta
N_CupTwo = CupTwo.calc_N_refills()
S_CupTwo = CupTwo.S
W_CupTwo = CupTwo.calc_total_weight()
Du_CupTwo = 6
Mtn_CupTwo = 8
Cbn_CupTwo = 5

PI1_CupTwo = 10/N_CupTwo
PI2_CupTwo = S_CupTwo/0.01*10
PI3_CupTwo = (T_ls_CupTwo-CupTwo.Ta)/60*10
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


CupThree = CoffeeCup(V = 17.7*2.9574e-5, 
                   A = 0.031,
                   S = 0.0001,                                                                                                                            
                   Tc = 373,
                   Ta = 297,
                   k = 0.2,
                   Ro_cup = 1390,
                   D = 1.5e-3,
                   Ro = 1000,
                   C = 4190,
                   dt =1,
                   Tsip_s = 60,
                   Psip_s = 0.3,
                   Tsip_l = 45,
                   Psip_l = 0.7,
                   V_total = 24*2.9574e-5
                   )

Tc_hist_3 =[]
while CupThree.Tc > CupThree.Ta + 0.1:
    Tc_hist_3.append(CupThree.Tc)
    CupThree.Tc = CupThree.solve_Tc_next
    
t_cool_CupThree = len(Tc_hist_3)*CupThree.dt
t_ls_CupThree = CupThree.calc_time_last_sip()
try:
    T_ls_CupThree = Tc_hist_3[int(CupThree.calc_time_last_sip()/CupThree.dt)]
except IndexError:
    T_ls_CupThree = CupThree.Ta
N_CupThree = CupThree.calc_N_refills()
S_CupThree = CupThree.S
W_CupThree = CupThree.calc_total_weight()
Du_CupThree = 6
Mtn_CupThree = 4
Cbn_CupThree = 5

PI1_CupThree = 10/N_CupThree
PI2_CupThree = S_CupThree/0.01*10
PI3_CupThree = (T_ls_CupThree-CupThree.Ta)/60*10
PI4_CupThree = 3/W_CupThree
PI5_CupThree = Du_CupThree
PI6_CupThree = Mtn_CupThree
PI7_CupThree = Cbn_CupThree

CupFour = CoffeeCup(V = 11*2.9574e-5, 
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
                   Tsip_s = 60,
                   Psip_s = 0.3,
                   Tsip_l = 45,
                   Psip_l = 0.7,
                   V_total = 24*2.9574e-5
                   )

Tc_hist_4 =[]
while CupFour.Tc > CupFour.Ta + 0.1:
    Tc_hist_4.append(CupFour.Tc)
    CupFour.Tc = CupFour.solve_Tc_next
    
t_cool_CupFour = len(Tc_hist_4)*CupFour.dt
t_ls_CupFour = CupFour.calc_time_last_sip()
try:
    T_ls_CupFour = Tc_hist_4[int(CupFour.calc_time_last_sip()/CupFour.dt)]
except IndexError:
    T_ls_CupFour = CupFour.Ta
N_CupFour = CupFour.calc_N_refills()
S_CupFour = CupFour.S
W_CupFour = CupFour.calc_total_weight()
Du_CupFour = 2
Mtn_CupFour = 3
Cbn_CupFour = 9

PI1_CupFour = 10/N_CupFour
PI2_CupFour = S_CupFour/0.01*10
PI3_CupFour = (T_ls_CupFour-CupFour.Ta)/60*10
PI4_CupFour = 3/W_CupFour
PI5_CupFour = Du_CupFour
PI6_CupFour = Mtn_CupFour
PI7_CupFour = Cbn_CupFour




df = pd.DataFrame({
'group': ['One','Two', 'Three', 'Four'],
'PI1': [PI1_CupOne, PI1_CupTwo, PI1_CupThree, PI1_CupFour],
'PI2': [PI2_CupOne, PI2_CupTwo, PI2_CupThree, PI2_CupFour],
'PI3': [PI3_CupOne, PI3_CupTwo, PI3_CupThree, PI3_CupFour],
'PI4': [PI4_CupOne, PI4_CupTwo, PI4_CupThree, PI4_CupFour],
'PI5': [PI5_CupOne, PI5_CupTwo, PI5_CupThree, PI5_CupFour],
'PI6': [PI6_CupOne, PI6_CupTwo, PI6_CupThree, PI6_CupFour],
'PI7': [PI7_CupOne, PI7_CupTwo, PI7_CupThree, PI7_CupFour]
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


max_length = max(max(max(len(Tc_hist_1), len(Tc_hist_2)), len(Tc_hist_3)),len(Tc_hist_4))
Tc_hist_1 += [297] * (max_length - len(Tc_hist_1))
Tc_hist_2 += [297] * (max_length - len(Tc_hist_2))
Tc_hist_3 += [297] * (max_length - len(Tc_hist_3))
Tc_hist_4 += [297] * (max_length - len(Tc_hist_4))

Tc_hist_1 = [x-273 for x in Tc_hist_1]
Tc_hist_2 = [x-273 for x in Tc_hist_2]
Tc_hist_3 = [x-273 for x in Tc_hist_3]
Tc_hist_4 = [x-273 for x in Tc_hist_4]


hourlyResults = pd.DataFrame({
        'Tc_CupOne': Tc_hist_1,
        'Tc_CupTwo': Tc_hist_2,
        'Tc_CupThree': Tc_hist_3,
        'Tc_CupFour': Tc_hist_4,       
        })
ax = hourlyResults.plot(figsize = (12,8), colormap = my_palette, fontsize = 12)
ax.set_xlabel("Time [s]")
ax.set_ylabel("Coffee Temperature [°C]")