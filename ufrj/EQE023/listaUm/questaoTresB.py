import matplotlib.pyplot as plt
import numpy as np

Co = 1.0
A = np.pi * (1.27e-2)**2
At = 6.0 * 2.5
Pg = 0.0
ro = 879.4
g = 9.81
hLo = 6.0

t = np.arange(0.0, 100.0, 2)


def Qm(i):
  return ro * Co * A * np.sqrt(
    2 * (Pg / ro + g * hLo)) - ro * g * Co*2 * A*2 * i / At


def Sqm(i):
  if i == 0:
    return Qm(i)
  else:
    return Qm(i) + Sqm(i - 2)


massa_acumulada = []
for i in t:
  massa_acumulada.append(Sqm(i))

plt.plot(t, massa_acumulada)
plt.show()