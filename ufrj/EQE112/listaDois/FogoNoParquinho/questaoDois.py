# QUESTÃO 2

from math import e
import numpy as np
import matplotlib.pyplot as plt

# Declaração de variáveis

R = 8.314  # Constante universal dos gases em J/mol.K
E = pow(10, 5)  # Energia de ativação em J/kmol
k0 = 7 * pow(10, 16)  # Constante cinética em s⁻¹

Ta = float(input("Insira um valor de temperatura entre 320 e 350K: "))

k = k0 * pow(e, -E / (R * Ta))

# Item A

print("O valor do parâmetro cinético da reação a", Ta, "Kelvin é igual a:", k, "s⁻¹")

# Item B

intervaloK = np.linspace(3.32, 83.24, 25)  # Array com os extremos sendo o menor e o maior valor de k
print("Os valores do parâmetro cinético no intervalo de 320 a 350 Kelvin estão entre:", intervaloK, "s⁻¹")

# Item C

Ta = np.linspace(320.0, 350.0, 100)  # Criação de um array entre 320 e 350K p/ o eixo da temperatura (x)
y = k0 * pow(e, -E / (R * Ta))       # Função do parâmetro cinético que será plotada no eixo y

plt.plot(Ta, y, 'g--')                                                  # Características
plt.xlabel('Temperatura (K)')                                           # do
plt.ylabel('Parâmetro cinético da reação (s⁻¹)')                        # gráfico
plt.title('Variação do parâmetro cinético em função da temperatura')
plt.show()
