import scipy.optimize as spo
import matplotlib.pyplot as plt
import numpy as np

def f(x):
   return x*3 - 6*x*2 + 11*x - 6.1


# Chute safado é 0
raiz = spo.newton(f, 0.0)

print(raiz)

nit = np.arange(1, 9, 1)
vit = []

for i in nit:
  vit.append((raiz - spo.newton(f, 0.0, maxiter=i, disp=False)) / raiz * 100.0)

plt.plot(nit, vit)
plt.show()