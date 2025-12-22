# listas
lista = []
lista = [0, 1, 2, '0', 'a']

# conversion de cadena a lista
list('mi cadena')

# conversion de rango de numeros a lista
list(range(10))

# generando listas de diferentes maneras
lista = [3] * 4 # [3, 3, 3, 3]
lista = ['hola'] * 3 # ['hola', 'hola', 'hola']
# lista por comprensión simple
lista = [i for i in range(10)]
# lista por comprensión operando sobre el número generado
lista = [i * 2 for i in range(10)]
# a partir de otra lista
lista_aux = [i for i in range(10)]
lista = [i * 2 for i in lista_aux]


# acceso a elementos
elemento = lista[0]
ultimo = lista[-1] # ultimo elemento

# trocear una lista
lista = [0, 1, 2, 3, 4, 5]

# 0 1 2
lista[:3]

# 2 3
lista[2:4]

# 5 4 3 (del final al -4 hacia atras)
lista[-1:-4:-1]

# 5 4 3 2 1 (recorrido hacia atras)
lista[::-1]

# invertir una lista
lista[::-1]
reversed(lista)

# introducir elementos al final
lista.append(9)

# añadir en cualquier posicion
lista.insert(3, 'elemento')

# repetir elementos (como en las cadenas)
lista = [1, 2]
repetida = lista * 2 # [1, 2, 1, 2]

# concatenar lista
concatenada = [1, 2] + [3, 4] # [1, 2, 3, 4]

# modificar listas mediante trozeado
lista = [0, 1, 2, 3, 4, 5]
lista[1:3] = [9, 9, 9] # [0, 9, 9, 9, 4, 5]

# tambien podemos utilizar un numero de elementos diferentes
lista[1:3] = [9, 9] # [0, 9, 9, 4, 5]

# borrar elementos
lista.clear() # []

# obtener el indice
lista = ['a', 'b', 'c']
indice = lista.index('b') # = 1

# pertenencia, no pertenencia y longitud de la lista
existe = 3 in [1, 2, 3]
no_existe = 3 not in [1, 2, 3]
len([1, 2, 3])

# contar apariciones
apariciones = [1, 3, 3, 2].count(3)

# convertir cadenas en listas con split()
cadena = 'esto es una cadena'
lista = cadena.split() # se puede usar como parametro el caracter ie: ';'

# crear una cadena desde una lista con join()
lista = ['a', 'b', 'c']
cadena = ','.join(lista) # 'a,b,c'

# ordenar lista
sorted(lista, reverse=True) # reverse de menor a mayor

# iterar la lista mediante for obteniendo tambien un indice
for indice, elemento in enumerate(lista):
    pass

# iterar en paralelo dos o mas listas
nombres = ['ana', 'luis', 'alberto']
edades = [33, 12, 41]
for nombre, edad in zip(nombres, edades): # si no tienen la misma longitud se acaba cuando lo haga la lista mas corta
    pass

# comparar listas
[1, 2, 3] < [1, 2, 4] # True, porque python compara las listas elemento a elemento

# copiando listas con copy()
a = [1, 2, 3]
b = a
b[0] = 9 # estamos alterando 'a'
a[2] = 3 # estamos alterando 'b'
# con copy() hacemos una copia a otro espacio de memoria
b = a.copy()

# veracidad multimple con all() y any()
condicion_a = 10 > 3
condicion_b = 3 != 6
expresion = all([condicion_a, condicion_b])
expresion = any([condicion_a, condicion_b])
# nota sobre estas funciones
all([]) # siempre True
any([]) # siempre False

# listas por comprension
# [ <nuevo valor generado para la lista> for <elemento iterado> in <lista> if <condicion/filtrado> ]
# version clasica, convertir una cadena en una lista de enteros
cadena = '1 2 3'
enteros = []
for valor in cadena.split():
    enteros.append(int(valor))
# version por comprension
enteros = [int(valor) for valor in cadena.split()]
# se puede poner una condicion
enteros = [int(valor) for valor in cadena.split() if valor != '3']

# algunas operaciones matematicas sobre listas
numeros = [1, 2, 3]
suma = sum(numeros) # 6
maximo = max(numeros)
minimo = min(numeros)


# lines de comandos sys.arg
# python main.py[0] parametro[1] parametro[2] ...
import sys
primer_parametro = sys.arg[1]
segundo_parametro = sys.arg[2]











