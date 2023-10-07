import numpy as np

# Declaração de arrays

v = np.array([[3], [2], [4]])
u = np.array([[3], [4], [8], [6]])
A = np.array([[8, 4, 5, 2], [5, 3, 4, 6], [2, 9, 7, 4], [3, 7, 3, 3]])
B = np.array([[3, 1, 8], [1, 3, 2], [8, 2, 3]])

# Item A
# Não é possível fazer a operação. Causa erro do tipo ValueError: os elementos não podem ser
# multiplicados por diferença nos formatos: (3,3) e (4,)

# Item B
# Não é possível fazer a operação. Causa erro do tipo ValueError: os elementos não podem ser
# multiplicados por diferença nos formatos: (4,) e (3,3)

# Item C: multiplicação da matriz u pela matriz A
print(u*A, "\n")

# Item D
# Não é possível fazer a operação. Causa erro do tipo ValueError: os elementos não podem ser
# somados por diferença nos formatos: (4,4) e (3,3)

# Item E: soma do elemento A14 com B33
print(A[0][3] + B[2][2], "\n")

# Item F: multiplicação da segunda coluna inteira de B com a matriz v
print(B[2] * v)
