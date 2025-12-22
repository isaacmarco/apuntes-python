import numpy as np
# generamos una matriz de prueba
M = np.array([i*2 for i in range(0, 16)]).reshape(4, 4)
# obtener una matriz de booleanos indicando True donde los valores son > 7
# Lo que obtenemos es una matriz de máscara
matriz_booleanos = M > 7
# al usar la expresión M > 7 entre corchetes: [M > 7], lo que hacemos
# es seleccionar aquellos elementos de la matriz que cumplen la condición
matriz_booleanos = M[M > 7]
# o incluso actualizar la matriz usando estos indices
M[M > 7] = -1

# ejercicio de ejemplo: extraer todos los numeros pares de esta matriz
M = np.array(range(10, 22)).reshape(3, 4)
solucion = M[M % 2 == 0]


# obtener indices de la matriz que cumplen determinada condicion
# se puede hacer mediente where(). Esto
indices = np.where(M > 7)
# ahora, para ver el valor almacenado en esos indices
valores = M[indices]

# operaciones de conjunto sobre matrices de np
x = np.array([1, 2, 3])
y = np.array([2, 5, 6])
np.union1d(x, y) # union
np.intersect1d(x, y) # interseccion
np.setdiff1d(x, y) # diferencia

# operaciones de ordenadcion y conteo
np.sort(x)
np.unique(x) # contar valores unicos
np.unique(x, return_counts=True) # contar valores unicos y sus frecuencias
np.count_nonzero(x) # valores distintos de cero

# operaciones aritmeticas con la misma dimension
x+y
x-y
x*y
x/y
# operaciones con diferentes dimensiones (siempre que sean posibles)
'''
Cuando operamos entre arrays con dimensiones diferentes, 
siempre y cuando se cumplan ciertas restricciones en tamaños de filas y/o columnas, 
lo que se produce es un «broadcasting» (o difusión) de los valores.
(ver los ejemplos de la documentación)
'''

# funciones estadisticas
np.mean(x) # media
np.std(x) # desviacion standart
np.median(x) # mediana





