import matplotlib.pyplot as plt 
import numpy as np 

# Definição de variáveis 

Pg = 0.0  # Tanque aberto -> pressão manométrica vai a zero 
g = 9.81  # Gravidade local (m/s²)
r = 5.0   # Diâmetro igual a 10 (m)
Co = 1.0  # Foi escolhido esse valor por facilitar as contas, 
          # ser um furo arredondado e minimizar a perda 
          # de massa liberada

ro = float(input("Insira o valor de massa específica do fluido em vazamento (kg/m³): "))

# Array com as alturas a serem analisadas (m)
hL = np.array([0.1, 0.5, 1.0, 1.25, 1.4, 1.5])

# Faixa arbitrária de diâmetros a serem analisados (m)
faixa = np.linspace(0.0, 10.0, 10)

# Função de define a área do furo a partir do diâmetro fornecido (o array acima)
def A(d): 
    return np.pi * np.power(d / 2.0, 2.0)


# Taxa de liberação instantânea
Qm1 = ro * A(faixa) * Co * (2 * g * hL[0])**1/2  # g/s
Qm2 = ro * A(faixa) * Co * (2 * g * hL[1])**1/2  # g/s
Qm3 = ro * A(faixa) * Co * (2 * g * hL[2])**1/2  # g/s
Qm4 = ro * A(faixa) * Co * (2 * g * hL[3])**1/2  # g/s
Qm5 = ro * A(faixa) * Co * (2 * g * hL[4])**1/2  # g/s
Qm6 = ro * A(faixa) * Co * (2 * g * hL[5])**1/2  # g/s

# Avaliação gráfica

plt.plot(faixa, Qm1, color='b', label='hL: 0.1 m')
plt.plot(faixa, Qm2, color='g', label='hL: 0.5 m')
plt.plot(faixa, Qm3, color='r', label='hL: 1.0 m')
plt.plot(faixa, Qm4, color='c', label='hL: 1.25 m')
plt.plot(faixa, Qm5, color='m', label='hL: 1.4 m')
plt.plot(faixa, Qm6, color='y', label='hL: 1.5 m')
plt.legend()
plt.ylabel("Taxa de liberação instantânea (g/s)")
plt.xlabel("Diâmetro (m)")
plt.title("Taxa de Liberação instantânea x diâmetro")
plt.show()
