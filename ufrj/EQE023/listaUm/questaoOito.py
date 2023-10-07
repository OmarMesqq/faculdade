import scipy as sp 
import numpy as np 

def f(h): 

    return (4.0 * np.arccos( (2.0 - h) / 2.0) - ( (2.0 - h) * np.sqrt(4.0*h - h**2.0))) * 5.0 - 8.0



# Escolhi 0 e 3 como chutes pois a função só está definida 
# nos reais em 0 ≤ h ≤ 4 (para que o que está dentro 
# da raiz não seja negativo 

sol = sp.optimize.brentq(f, 0.0, 3.0, full_output=True) 

print(sol) 
