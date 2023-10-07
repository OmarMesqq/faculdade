import matplotlib.pyplot as plt
import numpy as np

# Declaração de variáveis

Te = 25.0  # Temperatura de entrada na corrente de processo (ºC)
V = 10.0  # Volume do tanque (m³)
ro = 1000.0  # Densidade do fluido de processo (kg/m³)
Cp = 4180.0  # Capacidade calorífica do fluido de processo (J/kg.ºC)
mdot = 10.0  # Vazão mássica de líquido de processo (kg/s)
U = 2000.0  # Coeficiente de troca de calor (W/m².ºC)
A = 80.0  # Área de transferência (m²)
Tr = 100.0  # Temperatura do fluido de utilidade (ºC)

tau = (V * ro * Cp) / ((mdot * Cp) + (U * A))
Top = ((mdot * Cp * Te) + (U * A * Tr)) / ((mdot * Cp) + (U * A))

# Criação de array para representar o eixo x (tempo) em segundos
# De 0 a 1200s (20min) com 50 espaçamentos iguais
t = np.linspace(0, 1200, 50)


# Definição da equação que apresenta a evolução de temperatura na saída do tanque
def equacao(t):
    return (Te * np.exp((-t / tau))) + (Top * (1.0 - np.exp((-t / tau))))


# Análise gráfica
plt.plot(t, equacao(t), color='cyan', marker='.')
plt.xlabel("Tempo (s)")
plt.ylabel("Temperatura (ºC)")
plt.title("Evolução da temperatura na saída do tanque")
plt.show()

# Conclusão
# A partir da análise gráfica, conclui-se que a situação atinge
# o estado estacionário aproximadamente 1000s após o início do processo
