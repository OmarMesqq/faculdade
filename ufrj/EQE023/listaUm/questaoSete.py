import scipy as sp
import numpy as np


pc = 4600.0 # kPa
Tc = 191.0 # K
V = 3.0 # m³ (diferente de v)
T = 233.15 # K
p = 65000.0 # kPa
R = 0.518 # kJ/kg*K
# m = V / v

a = 0.427*(R**2)*(Tc**2.5)/pc
b = 0.0866 * (Tc / pc)

def y(v): 
  return (R * T / (v - b)) - (a/(v*(v + b) * np.sqrt(T))) - p


#res = sp.optimize.brentq(y, 1.0, 0.005, full_output=True, xtol = 1e-16)
#print(res)
print("a é igual a:", a)
print("b é igual a:", b)
# v != ± b   e v != 0 

#test = sp.optimize.anderson(y, 0.004,)