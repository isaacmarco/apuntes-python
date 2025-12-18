# definicion
from functools import reduce


def suma(a, b):
    return a+b

# retornar multiples valores
def funcion():
    return 0, 1, 2

# argumentos posicionales y nominales, valores por defecto
def mi_funcion(p1, p2, p3 = 0.1):
    pass
mi_funcion(1, p2='nominal')

# por defecto, si pasamos una lista y operamos sobre ella,
# será modificada
lista = [1, 2, 3]
def modificar(lista):
    for i in range(len(lista)):
        lista[i] += 1
    return lista
modificar(lista) # esto modifica mi lista original

# numero variable de parametros con el operador '*'
def ejemplo(*parametros):
    for p in parametros:
        pass
ejemplo(1, 2, 3, 4, 5)

# parametros variables nominales con el operador '**'
# por convención usamos *args y **kwargs como nombre para los parametros de las funciones en python
def ejemplo2(**parametros):
    for p in parametros:
        print(p)
ejemplo2(cosa='x', coche='p')

# funciones como parametros
def ejemplo3(funcion):
    funcion()

# pasando funciones y sus parametros
def ejemplo4(funcion, args):
    funcion(args)

# anotacion de tipos en funciones, por ejemplo, indicamos
# que la funcion toma un entero, un string y devuelve una tupla
def anotacion(numero:int, texto:str) -> tuple:
    return (numero, texto)
# algunos ejemplos de anotaciones de tipos:
# -> list[str]          [1, 2, 3]
# -> set[int]           {6, 1, 2}
# -> dict[str, int]     {'x':1, 'p':2, 'w':6}
# -> tuple[str, str]    ('a', 'b')

# funciones anónimas o lambda
# son anónimas y tienen un return implícito
contar_palabras = lambda t: len(t.split()) # devuelve el numero de palabras en un texto 't'
numero = contar_palabras('teo va al zoo')

# funciones map(), filter() y reduce()
# map: aplicar una función a una lista
mapa = map(lambda n: n*2, [1, 2, 3])
print(list(mapa)) # mapa es un 'generador' hay que convertirlo en una lista
# filter: seleccionar elementos de un iterable
filtro = filter(lambda n: n>2, [1, 2, 3])
print(list(filtro))
# reduce: va aplicando el resultado de la función al elemento siguiente sucesivamente
reducir = reduce(lambda x, y: x+y, [1, 2, 3]) # devuelve la suma 1+2=3, 3+3=6
print(reducir)

# generadores (generar valores, no de forma explícita, se van generando
# según los necesitemos consumir)
# ejemplo de una función generadora de números pares
def generar_pares(limite: int):
    for num in range(0, limite + 1, 2):
        yield num # la generacion se congela hasta la siguiente llamada a la funcion
# para obtener todos los numeros generados a la vez
list(generar_pares(30))
# una vez generados todos los números, el generador se 'agota', ya no generará más

# funciones dentro de una funcion (funciones interiores)
def funcion_padre():
    def funcion_interna():
        pass
    pass

# decoradores de funciones: permiten cambiar su comportamiento
# pero sin alterar su código. Un decorador es una función que recibe como parámetro
# una función y devuelve otra función
def mi_decorador(funcion):
    def wrapper(*arg, **kwargs):
        pass
        return funcion(*arg, **kwargs)
        pass
    return wrapper
# ejemplo de un decorador que convierte el resultado de una función
# a numeración binaria
def binarize(funcion):
    def wrapper(*args, **kwargs):
        resultado = funcion(*args, **kwargs)
        return bin(resultado)
    return wrapper
@binarize
def sumar_bin(a, b):
    return a+b
print(sumar_bin(1, 1))
