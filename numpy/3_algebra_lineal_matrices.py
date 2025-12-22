import numpy as np
m1 = np.array([
    [1, 2],
    [3, 4]
    ]
)
m2 = np.array([
    [2, 3],
    [1, 2]
])

# producto de matrices
np.dot(m1, m2) # o m1 @ m2
# calculo del determinante
np.linalg.det(m1)
# inversa de la matriz
np.linalg.inv(m1)
# traspuesta de la matriz
matriz_traspuesta = m1.T
# elevar una matriz a una potencia
np.linalg.matrix_power(m1, 2) # elevar al cuadrado


# resolver sistemas de ecuaciones lineales
A = np.array([[1, 0, 2], [1, -1, 0], [0, 1, 1]])
B = np.array([1, -2, -1]).reshape(-1, 1)
np.linalg.solve(A, B)



