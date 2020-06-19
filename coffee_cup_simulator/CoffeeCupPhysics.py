# -*- coding: utf-8 -*-

""" 

VRAIRABLE DEFINITIONS
Mco: Mass of coffee, [kg]
Mcup: Mass of cup, [kg] 
V: Volume of coffee cup, [m3]
D: Width of cup wall, [m] 
A: Internal suface area of coffee cup, [m2]
S: Top openning area of coffee cup, [m2]
C: Specific heat of coffee, exp. 4190 [J/kg-K]
ro: Density of Coffee, 1000 [kg/m3]
Ht: Heat transfer coefficient on top of coffee, exp. 10 [W/m2-K]
    Ht = Ht_evap + Ht_conv + Ht_rad

Hc: Heat transfer coefficient outside of coffee cup, exp. 10 [W/m2-K]
    Hc = Hc_cond + Hc_conv

k: Thermal conductivity of cup wall, [W/m-K]



    exp. Paper: k = 0.18 [W/m-K], ro = 930 [kg/m3]
         Gold: k = 317 [W/m-K], ro = 19300 [kg/m3]
         Silver: k = 42 [W/m-K], ro = 10500 [kg/m3]
         Stainless Steel: 14.9 [W/m-K], ro = 7900 [kg/m3]
         Aluminum Alloy: k = 168 [W/m-K], ro = 2790
         Glass: k = 1.4 [W/m-K], ro = 2500 [kg/m3]

Ta: Ambient Temperature, 297 [K]
Tc: Temperature of Coffee at current time step
Tc_next: Temperature of Coffee at next time step
va: Air velocity, m/s
xs: Absolute Humidity of Room Air when saturated, 0.01887 [kg/kg]
xa: Absolute Humidity of Room Air, 0.00944 [kg/kg]
 
dt: time step, [s]



"""

__authors__ = "Yiyuan Jia"
__copyright__ = "Copyright 2020"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Yiyuan Jia"
__email__ = "yiyuan1840@gmail.com"
__status__ = "production"



class CoffeeCup(object):
    '''Sets the parameters of a Coffee Cup. '''

    def __init__(self,
                 V = 12*2.9574e-5, # Cup Volume [m3]
                 va = 0.1, # Air Velocity [m/s]
                 A = 0.0314, # Cup Wall Surface Area [m2]
                 S = 0.00785, # Cup Top Openning Area [m2]
                 Tc = 373, # Coffee Initial Temperature [K]
                 Ta = 297, # Ambient Air Temperature [K]
                 k = 0.18, # Thermal Conductivity of Cup Wall Material [W/m-K]
                 Ro_cup = 930, # Density of Cup Wall Material [kg/m3]
                 D = 2e-3, # Thickness of Cup Wall [m]
                 Ro = 1000, # Density of Coffee [kg/m3]
                 C = 4190, # Specific Heat of Coffee [J/kg-K]
                 dt =1, # Time Step [s]
                 Tsip_s = 10, # Time Interval of Small Sips [s]
                 Psip_s = 0.4, # Ratio of Small Slips
                 Tsip_l = 30, # Time Interval of Large Sips [s]
                 Psip_l = 0.6, # Ratio of Large Sips 
                 V_total = 24*2.9574e-5 # Total Volume of Coffee Consumed per Day [m3]
                 ):

        self.V = V
        self.va = va
        self.A = A
        self.S = S
        self.Tc = Tc
        self.Ta = Ta
        self.k = k
        self.Ro_cup = Ro_cup
        self.D = D
        self.Ro = Ro
        self.C = C
        self.dt = dt
        self.Mco = self.Ro*self.V
        self.Tsip_s = Tsip_s
        self.Psip_s = Psip_s
        self.Tsip_l = Tsip_l
        self.Psip_l = Psip_l
        self.V_total = V_total
        
    @property
    def Hc_cond(self):
        return self.k/self.D
    @property
    def Hc_conv(self):
        return 0.22*(self.Tc-self.Ta)/3
    @property
    def Ht_conv(self):
        return 0.03*self.Tc-3.19
    @property
    def Ht_rad(self):
        return 0.03*self.Tc-3.19
    @property
    def Ht_evap(self):
        return 0.0000000820512820524878*(self.Tc**5)-0.000134765151517127*(self.Tc**4)+0.0885076410269429*(self.Tc**3)-29.0519601670975*(self.Tc**2)+4765.80794097125*self.Tc-312557.660753791
    @property 
    def solve_Tc_next(self):
        self.Ht = self.Ht_evap + self.Ht_conv + self.Ht_rad
        self.Hc = self.Hc_cond + self.Hc_conv
        self.Term_1 = -self.Hc*self.A*(self.Tc - self.Ta)
        self.Term_2 = -self.Ht*self.S*(self.Tc - self.Ta)
        return self.dt*(self.Term_1+self.Term_2)/(self.Mco*self.C)+self.Tc
        
    def calc_time_last_sip(self):
        self.N_sip = self.V/2.9574e-5/0.8
        self.t_sip = self.Psip_s*self.N_sip*self.Tsip_s +self.Psip_l*self.N_sip*self.Tsip_l
        return self.t_sip
    
    def calc_N_refills(self):
        return self.V_total/self.V
    
    def calc_total_weight(self):
        self.Mcup = self.A*self.D*self.Ro_cup
        return self.Mco+self.Mcup
    
    
        
        
        
        