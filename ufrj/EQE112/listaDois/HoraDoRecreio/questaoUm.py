# Segunda Lista de Exercícios - EQE112
#
# Omar Mesquita Amaral Figueira
#
# Escola de Química - UFRJ

# QUESTÃO 1
# Valores negativos causam erro do tipo "math domain"

from math import sqrt  # Importar a função raiz quadrada da biblioteca de matemática

g = 9.81  # Gravidade em m/s²
h = float(input("Forneça um valor de altura: "))  # Converter para número real o valor que o usuário fornece
v = sqrt(2.0 * g * h)  # Equação da queda livre

print("A velocidade final é de:", v, "m/s", "\n")
