# QUESTÃO 4
import numpy as np

u = np.array([3, 4, 12, 8, 6])  # Criação
v = np.array([22, 14, 8, 12, 7, 9, 11])  # dos
w = np.array([1.1, 2.4, 3.8, 5.4, 8.3])  # arrays

# Item A
print("Multiplicação de u por w:", u * w)

# Item B
# Não é possível calcular u*v, visto que os arrays apresentam quantidades de elementos diferentes

# Item C
print("Divisão de u por w:", u / w)

# Item D
print("Soma do 3o elemento de v e o 2o elemento de w:", v[2] + w[1])

# Item E
# Não é possível fazer a soma de u[2] com w[5], pois esse último array apresenta no máximo índice 4.
# Portanto, tentar fazer tal operação resulta em um erro do tipo "out of bounds" (fora do domínio)

# Item F
print("Soma de todos os elementos de v:", v.sum())

# Item G
print("Potência de 3.3 em todos os elementos de w:", pow(w[::], 3.3))

