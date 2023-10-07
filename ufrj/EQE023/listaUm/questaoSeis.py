import scipy as sp
import math

pt = 3.0  # atm 
K = 0.05  # adimensional 


def y(x):
  return x /(1 - x) * math.sqrt(2*pt/2+x) - K 

# Analisando a função, encontramos 3 assíntotas, 2 verticais em x = 1 e x = -2
# e uma horizontal em y = -0.05 (x tendendo a +inf). 
# Além disso, o domínio da função são os reais, com x!= 1 e  x > -2
# O primeiro chute foi 0, pois f(0) < 0. 
# Já o chute de 0.5 foi escolhido
# por estar entre 0 e 1 e f(0.5) > 0.

res = sp.optimize.brentq(y, 0.0, 0.5, full_output=True)
print(res)
