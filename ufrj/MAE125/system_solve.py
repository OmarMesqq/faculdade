import numpy as np 

coef = np.array([
        [1, 2, -1, -2],
        [2, 6, 0, -3],
        [1, 0, 0, -1],
        [1, 6, 9, 8],
        [-1, 2, 2, 6]
        ])

k_values = [4, -2, -1, 3, 1, 5, 2, 0]

for k in k_values:
    
    rhs = np.array([
        [-2],
        [-3],
        [-1],
        [6],
        [4]
        ])

    x, residuals, rank, s = np.linalg.lstsq(coef, rhs, rcond=None) 

    if np.allclose(np.dot(coef, x), rhs):
        print("Solution:")
        print("x =", x[:-1])
        print("k =", x[-1])
