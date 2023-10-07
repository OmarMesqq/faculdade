import numpy as np 
import matplotlib.pyplot as plt 
import scipy.linalg as linalg

G = 40.8    # kmol/h
L = 66.7    # kmol/h
a = 0.72
yin = 0.2

#### Caso 2 estágios ####

# n = 1
# -(L + G*a)*X1 + G*a*X2 = 0
# n = 2
# L*X1 - (L + G*a)*X2 = -G*yin

A2 = np.array([
    [ -(L + G*a), G*a],
    [L, -(L + G*a)]
])

B2 = np.array([0.0, -G*yin])

es2 = linalg.solve(A2, B2)


#### Caso 3 estágios ####

# n = 1
# -(L + G*a)*X1 + G*a*X2 = 0
# n = 2 
# L*X1 - (L + G*a)*X2 + G*a*X3 = 0
# n = 3
# L*X2 - (L + G*a)*X3 = -G*yin
#
A3 = np.array([
    [-(L + G*a), G*a, 0.0],
    [L, -(L + G*a), G*a],
    [0.0, L, -(L + G*a)]
])

B3 = np.array([0.0, 0.0, -G*yin])

es3 = linalg.solve(A3, B3)

#### Caso 6 estágios ####

# n = 1
# -(L + G*a)*X1 + G*a*X2 = 0
# n = 2 
# L*X1 - (L + G*a)*X2 + G*a*X3 = 0
# n = 3
# L*X2 - (L + G*a)*X3 + G*a*X4 = 0
# n = 4
# L*X3 - (L + G*a)*X4 + G*a*X5 = 0
# n = 5
# L*X4 - (L + G*a)*X5 + G*a*X6 = 0
# n = 6
# L*X5 - (L + G*a)*X6 = -G*yin

A6 = ([
    [-(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0],
    [L, -(L + G*a), G*a, 0.0, 0.0, 0.0],
    [0.0, L, -(L + G*a), G*a, 0.0, 0.0],
    [0.0, 0.0, L, -(L + G*a), G*a, 0.0],
    [0.0, 0.0, 0.0, L, -(L + G*a), G*a],
    [0.0, 0.0, 0.0, 0.0, L, -(L + G*a)]
])

B6 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, -G*yin])

es6 = linalg.solve(A6, B6)

#### Caso 8 estágios ####

# n = 1
# -(L + G*a)*X1 + G*a*X2 = 0
# n = 2 
# L*X1 - (L + G*a)*X2 + G*a*X3 = 0
# n = 3
# L*X2 - (L + G*a)*X3 + G*a*X4 = 0
# n = 4
# L*X3 - (L + G*a)*X4 + G*a*X5 = 0
# n = 5
# L*X4 - (L + G*a)*X5 + G*a*X6 = 0
# n = 6
# L*X5 - (L + G*a)*X6 + G*a*X7 = 0
# n = 7
# L*X6 - (L + G*a)*X7 + G*a*X8 = 0
# n = 8
# L*X7 - (L + G*a)*X8 = - G*yin

A8 = np.array([
    [-(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a)]
    ])

B8 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, - G*yin])

es8 = linalg.solve(A8, B8)

#### Caso 12 estágios ####

# n = 1
# -(L + G*a)*X1 + G*a*X2 = 0
# n = 2 
# L*X1 - (L + G*a)*X2 + G*a*X3 = 0
# n = 3
# L*X2 - (L + G*a)*X3 + G*a*X4 = 0
# n = 4
# L*X3 - (L + G*a)*X4 + G*a*X5 = 0
# n = 5
# L*X4 - (L + G*a)*X5 + G*a*X6 = 0
# n = 6
# L*X5 - (L + G*a)*X6 + G*a*X7 = 0
# n = 7
# L*X6 - (L + G*a)*X7 + G*a*X8 = 0
# n = 8
# L*X7 - (L + G*a)*X8 + G*a*X9 = 0
# n = 9
# L*X8 - (L + G*a)*X9 + G*a*X10 = 0
# n = 10
# L*X9 - (L + G*a)*X10 + G*a*X11 = 0
# n = 11
# L*X10 - (L + G*a)*X11 + G*a*X12 = 0
# n = 12
# L*X11 - (L + G*a)*X12 = - G*yin

A12 = np.array([
    [-(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
    [L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a), G*a],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, L, -(L + G*a)]
])

B12 = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -G*yin])

es12 = linalg.solve(A12, B12)

# Definição do eixo X para cada caso 
es2x = np.arange(1, 3, 1)
es3x = np.arange(1, 4, 1)
es6x = np.arange(1, 7, 1)
es8x = np.arange(1, 9, 1)
es12x = np.arange(1, 13, 1)

# Plotando o gráfico 
plt.plot(es2x, es2, 'o-', label='2 estágios')
plt.plot(es3x, es3, 'o-', label='3 estágios')
plt.plot(es6x, es6, 'o-', label='6 estágios')
plt.plot(es8x, es8, 'o-', label='8 estágios')
plt.plot(es12x, es12, 'o-', label='12 estágios')
plt.xlabel("Número de estágios")
plt.ylabel("Fração molar em cada estágio")
plt.legend(loc="lower right")
plt.show()
