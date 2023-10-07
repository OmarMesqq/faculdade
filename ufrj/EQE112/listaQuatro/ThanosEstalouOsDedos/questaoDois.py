import numpy as np
import matplotlib.pyplot as plt

# Item A


mdot = 1.2 * 10e-3  # taxa mássica em kg/s
t = np.linspace(250.0, 400.0, 50)

D = 0.01  # diâmetro do tubo circular em m
L = 1.3  # comprimento do tubo circular em m
Dab = 26.0 * 10e-6  # coeficiente de difusão H₂O, ar em m²/s
As = np.pi * D * L  # área de troca de massa em m²
roAs = 0.0226  # massa específica da água em condição de saturação em kg/m³
rob = 1.17  # massa específica do ar em kg/m³
mib = 183.6 * 10e-7  # viscosidade dinâmica do ar em N.s/m²
roAin = 1000.0  # massa específica da água em condição de entrada em kg/m³

Red = ((4 * mdot) / (np.pi * D * mib))  # Adimensional de Reynolds
Sc = (mib / (rob * Dab))  # Adimensional de Schmidt

# Regime turbulento para essa taxa mássica:

hm = (0.023 * Dab * pow(Red, 0.83) * pow(Sc, 0.44)) / D

roAout = - ((roAs - roAin) * np.exp((-As * rob * hm) / mdot)) + roAs

plt.plot(t, roAout)
plt.xlabel("Temperatura (K)")
plt.ylabel("Variação da concentração mássica (kg/m³)")
plt.show()

# Item B

t = 298.15  # Temperatura fixa em Kelvin

mdot = np.linspace(1.5 * 10e-5, 1.5 * 10e-3)

plt.plot(t, roAout)
plt.xlabel("Temperatura (K)")
plt.ylabel("Variação da concentração mássica (kg/m³)")
plt.show()