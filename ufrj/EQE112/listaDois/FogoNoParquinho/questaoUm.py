# QUESTÃO 1
import numpy as np

# Declaração de arrays de propriedades físicas do ar a pressão ambiente
# Os arrays seguem a seguinte formatação:
# aX = [ro, Cp, mi, k]
# Onde:
# X é a temperatura em Kelvin
# ro é a massa específica em kg/m³
# Cp é a capacidade calorífica em J/kg.K
# mi é a viscosidade em N.s/m²
# k é a condutividade térmica em W/m.K


a250 = np.array([1.3947, 1006.0, 159.6 * pow(10, -7), 22.3 * pow(10, -3)])

a300 = np.array([1.1614, 1007.0, 184.6 * pow(10, -7), 26.3 * pow(10, -3)])

a350 = np.array([0.9950, 1009.0, 208.2 * pow(10, -7), 30.0 * pow(10, -3)])

a400 = np.array([0.8711, 1014.0, 230.1 * pow(10, -7), 33.8 * pow(10, -3)])


# Declaração de informações obtidas a partir das propriedades físicas
# vX é a viscosidade cinemática em m²/s a X Kelvin
# alfaX é a difusividade térmica em m²/s a X Kelvin
# prX é o número de Prandtl (adimensional) a X Kelvin

# Informações a 250K:

v250 = a250[2] / a250[0]
alfa250 = a250[3] / (a250[0] * a250[1])
pr250 = alfa250 / v250

# Informações a 300K:

v300 = a300[2] / a300[0]
alfa300 = a300[3] / (a300[0] * a300[1])
pr300 = alfa300 / v300

# Informações a 350K:

v350 = a350[2] / a350[0]
alfa350 = a350[3] / (a350[0] * a350[1])
pr350 = alfa350 / v350

# Informações a 400K:

v400 = a400[2] / a400[0]
alfa400 = a400[3] / (a400[0] * a400[1])
pr400 = alfa400 / v400

#
# FORMATAÇÃO DA TABELA DE RESULTADOS
#

print("\n")
print("\t\tViscosidade cinemática (m²/s)\t""Difusividade térmica (m²/s)\t""Número de Prandtl (-)\n")
print("250K\t", v250, "\t", alfa250, "\t", pr250)
print("300K\t", v300, "\t", alfa300, "\t", pr300)
print("350K\t", v350, "\t", alfa350, "\t", pr350)
print("400K\t", v400, "\t", alfa400, "\t", pr400)
