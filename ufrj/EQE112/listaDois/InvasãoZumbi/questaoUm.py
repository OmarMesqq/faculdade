from math import *

# Declaração de variáveis

T = 590  # Temperatura em Kelvin
P = 1  # Pressão em bar
Ma = 28.014  # Massa molar do N2 calculada com base na tabela periódica da IUPAC 2022
Mb = 44.009  # Massa molar do CO2 calculada com base na tabela periódica da IUPAC 2022
Mab = 2 * pow((1 / Ma) + (1 / Mb), -1)  # Média ponderada da massa molecular das espécies envolvidas
sigma = 3.8695  # Comprimento característico entre as espécies químicas envolvidas

A = 1.06036  #
B = 0.15610  #
C = 0.19300  #
D = 0.47635  # Constantes para o cálculo do coeficiente integral de colisão adimensional
E = 1.03587  # propostas por Neufeld et al (1972)
F = 1.52996  #
G = 1.76474  #
H = 3.89411  #

Tasterisco = 590 / (sqrt(13937.28))  # Constante T* para o cálculo do coeficiente integral de colisão adimensional

# Coeficiente Omega D
omega = (A / pow(Tasterisco, B)) + (C / exp(D * Tasterisco)) + (E / exp(F * Tasterisco)) + (G / exp(H * Tasterisco))

# Por fim, cálculo do coeficiente de difusão (cm²/s) seguindo a correlação de Chapman e Enskog
Dab = 0.00266 * (pow(T, 1.5) / (P * sqrt(Mab) * pow(sigma, 2) * omega))

print("Para um sistema com as seguintes características:")
print("Espécies químicas envolvidas: N2 e CO2")
print("Pressão: 1 bar")
print("Temperatura: 590 K")
print("o valor do coeficiente de difusão é igual a", Dab, "cm²/s")

# O resultado obtido pela correlação corresponde a aproximadamente 88% daquele reportado
# por Ellis e Holsen (1969) experimentalmente, o qual equivale a 0.583 cm²/s
