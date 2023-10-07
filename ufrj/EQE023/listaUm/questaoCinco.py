import scipy.optimize as spo
import math

g = 9.8 # m/s²
Cd = 0.25 # kg/m
t = 4.0  # s
v = 36.0 # m/s

def y(m):
  return math.sqrt(g*m/Cd) * math.tanh(math.sqrt(g*Cd/m)*t) - v


res = spo.newton(y, 80.0, full_output=True)
print(res) 