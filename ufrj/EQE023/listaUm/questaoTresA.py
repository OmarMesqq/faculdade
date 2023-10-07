from sympy import diff, Symbol
import numpy as np

# Definimos valores aleatórios para testar
Co = 1.0
A = np.pi * (1.27e-2) ** 2
At = 6.0 * 2.5
Pg = 0.0
ro = 879.4
g = 9.81
hLo = 6.0

# Resolução analítica para a derivada
t1 = Symbol('t1')
hL = hLo - Co*A*(t1)/At * np.sqrt(2*Pg/ro + 2*g*hLo) + g/2 * pow(Co*A/At, 2.0)
dhL = diff(hL, t1)
print("Resolução analítica para a derivada: ", dhL)


# Aproximação numérica
h = 1e-7 # Tolerância
t = 1.0

hL_th = hLo - Co*A*(t + h)/At * np.sqrt(2*Pg/ro + 2*g*hLo) + g/2 * pow(Co*A/At, 2.0)
hL_t = hLo - Co*A*t/At * np.sqrt(2*Pg/ro + 2*g*hLo) + g/2 * pow(Co*A/At, 2.0)

dNum = (hL_th - hL_t)/h
print("Aproximação numérica, com t = 1.0 seg e tolerância = 10⁻⁷: ", dNum)
# Sendo que tanto faz o tempo
