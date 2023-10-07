# QUESTÃO 5

# IMPORTAÇÃO DE MÓDULOS
import matplotlib.pyplot as plt
import numpy as np

# Declaração de variáveis
v0 = 3.0  # velocidade em m/s
g = 9.81  # gravidade em m/s²

# Array de 0 a 1 com 100 intervalos, já que a partícula
# é coletada no instante 0.3s e segunda raiz da parábola
# é igual a 0.6s (aproximadamente)

t = np.linspace(0.0, 1.0, 100)
y = v0 * t - (g * (pow(t, 2.0))) / 2

# As raízes da equação da distância são iguais a 0 e a 200 / 327, logo o
# instante t (Xv) em que a trajetória estiver concluída/for máxima (Yv)
# é 100 / 327 segundos (Xv = x1 + x2 / 2)

s = v0 * (100 / 327) - (g * (pow((100 / 327), 2.0))) / 2

print("A trajetória s é igual a:", s, "metros")

plt.plot(t, y, 'g--', label='Curva de deslocamento')
plt.xlabel("Tempo (s)")
plt.ylabel("Distância (m)")
plt.title("Distância da partícula em função do tempo")
plt.legend()
plt.show()
