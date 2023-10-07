import numpy as np

D = 0.01  # diâmetro do tubo circular em m
L = 1.3  # comprimento do tubo circular em m
Dab = 26.0 * 10e-6  # coeficiente de difusão H₂O, ar em m²/s
As = np.pi * D * L  # área de troca de massa em m²
roAs = 0.0226  # massa específica da água em condição de saturação em kg/m³
rob = 1.17  # massa específica do ar em kg/m³
mib = 183.6 * 10e-7  # viscosidade dinâmica do ar em N.s/m²
roAin = 1000.0  # massa específica da água em condição de entrada em kg/m³

mdot = float(input("Insira um valor para taxa mássica: "))
Red = ((4 * mdot) / (np.pi * D * mib))  # Adimensional de Reynolds
Sc = (mib / (rob * Dab))  # Adimensional de Schmidt

# Bloco de "limites" para valores
# para taxa mássica. Obtidos pelo isolamento
# da equação do adimensional de Reynolds
# Para os valores dados, 0.6 <= Sc =< 2.5,
# então a seguinte relação vale:
mdotMin = 1.441991027997715e-05  # Menor valor (para 10 < Red)
mdotMaxLam = 0.00288398205599543  # Valor de virada de regime laminar para turbulento (Red = 2000)
mdotMax = 0.05046968597992002  # Valor máximo, isto é, Red < 35000

# Cálculo do coeficiente de convecção mássica (hm) em m/s
if mdot < mdotMin:
    quit("Insira um valor maior para taxa mássica")

elif mdotMin <= mdot < mdotMaxLam:  # Laminar
    hm = (1.86 * Dab * pow((D / L) * Red * Sc, 1 / 3)) / D

elif mdotMaxLam <= mdot < mdotMax:  # Turbulento
    hm = (0.023 * Dab * pow(Red, 0.83) * pow(Sc, 0.44)) / D

else:
    quit("Insira um valor menor para a taxa mássica")

roAout = - ((roAs - roAin) * np.exp((-As * hm * rob) / mdot)) + roAs

print("A concentração mássica de água na saída é igual a", roAout, "kg/m³")
