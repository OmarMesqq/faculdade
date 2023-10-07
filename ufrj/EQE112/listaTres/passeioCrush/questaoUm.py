# Omar Mesquita Amaral Figueira - EQE112
# Prof. Luiz Fernando Lopes
# Escola de Química - UFRJ

# Importação de módulos e bibliotecas
from math import sqrt

# Declaração de variáveis
g = 9.81  # aceleração da gravidade em m/s²
h = float(input("Insira um valor de altura em metros: "))

if h < 0:
    print("Por favor, insira um valor positivo")

v = sqrt(2*g*h)

print("A velocidade final em queda livre do corpo a", f"{h:3.2f}", "metros de altura é igual a", f"{v:3.2f}", "m/s")

# Utilizando o meu próprio código, concluí que a velocidade terminal de um corpo a 6m de altura
# equivale aproximadamente a 10,84 m/s
