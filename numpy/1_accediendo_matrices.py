import numpy as np
# se accede a las matrices por los llamados ejes
# 1D se usa el eje X(0)
# 2D se usa el eje X(0) para las filas y Y(1) para las columnas


# operaciones
a = np.array(range(1, 10))
# acceso y modificacion
a[0] = 99
# eliminacion de uno o varios elementos
np.delete(a, 2)
np.delete(a, (1, 2, 3))
# insercion de uno o varios elementos
np.append(a, 3) # al final
np.insert(a, 0, 66) # en el indice 0, insertamos el valor 66

# apilando matrices
M = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
)
M2 = np.ones((3,2)).astype('int')
apilada = np.stack((M, M2))


