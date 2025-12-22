# para instalar:
# pip install numpy
# para importar el paquete
import numpy as np

# arrays ndimensionales en numpy con 'ndarray'
# donde los elementos tienen que ser del mismo tipo
# El metodo array utiliza una lista, asi que hay que usar corchetes[]
a = np.array([1, 2, 3, 4])

# informacion sobre el array
a.ndim # el numero de dimensiones (unidimensional en este caso)
a.size # el numero de elementos
a.shape # la forma de la matriz, en este caso: (4, )

# arrays vs listas: el rendiiento de los arrays es muy superior cuando
# trabajamos con grandes cantidades de datos
# De todas formas, para convertir un ndarray en una lista tenemos el metodo tolist()
lista = a.tolist()

# matrices en numpy: ojo, todas las filas se han metido como elementos de una lista []
M = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
# se puede cambiar la forma de una matriz mediante reshape()
# por ejemplo, para cambiar la matriz anterior de 2x3 a una de 3x2
# reshape no altera la matriz, tienes que asignar la nueva
# reshape(filas, columnas)
M = M.reshape(2, 3)

# guardar la matriz en un texto plano
np.savetxt('fichero.csv', M)
# cargar la matriz
M = np.loadtxt('fichero.csv').astype('int') # para que la cargue parseando a enteros

# funciones para crear matrices
M = np.zeros((3, 3)).astype('int') # con ceros
M = np.ones((3, 3)).astype('int') # con unos
M = np.full((3, 3), 9) # con nueves
M = np.eye(3) # matriz de identidad de 3x3
M = np.diag([1,2,3]) # matriz de 3x3 con [1,2,3] en la diagonal


# podemos crear arrays como con el metodo range() de python
a = np.range(10)
a = np.range(5, 10)
a = np.range(5, 10, 2) # de 5 a 9 contando de 2 en 2
a = np.range(5, 10, .1) # de 5 a 9 contando de 0.1 en 0.1

# podemos crear matrices aleatorias. Por ejemplo, crear una matriz de 10x10
# con numeros aleatorios de 0 a 100
matrix = np.random.randint(0, 100, size=(10, 10))
