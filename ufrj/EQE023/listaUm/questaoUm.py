import matplotlib.pyplot as plt
import numpy as np


# Definição da faixa de fração mássica de NaOH
Y = np.linspace(0.05, 0.25, 20)

# Fórmula
YNaOH = (5 + 90 * Y)/100

# Avaliação gráfica

plt.plot(YNaOH, Y, color='fuchsia')
plt.xlabel("Concentração de NaOH em F1 (fornecedor)")
plt.ylabel("Fração mássica na corrente de saída")
plt.title("Evolução da concentração de NaOH na saída do tanque")
plt.show()
