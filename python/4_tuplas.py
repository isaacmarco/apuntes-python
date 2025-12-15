# las tuplas son inmutables
vacia = ()
pos = (23, 42)
multiples = ('a', 'b', 'c')

# tuplas de un solo elemento: hay que usar una , o de lo contrario será tratado como una string
elemento_unico = ('a', )

# también se pueden declarar sin parentesis
tupla = 2, 3

# conversion lista -> tupla
tuple([1, 2, 3])

# operaciones con tuplas:
# reverse, append, extend, remove, clear, sort

# desempaquetado de tuplas: asignar cada elemento de la tupla a una variable independiente
tupla = (1, 2, 3)
x, y, z = tupla

# intercambiando valores
a = 0
b = 1
a, b = b, a

# desempaquetado extendido
dias = ('L', 'M', 'X', 'J', 'V', 'S', 'D')
primero, *otros, ultimo = dias # indicado con *, otros será una lista con [M,X,J,V,S]
primero, *otros = dias # L, [M,X,J,V,S,D]
primero, segundo, *otros = dias # L, M, [X,J,V,S,D]
*otros, penultimo, ultimo = dias # [L,M,X,J,V], S, D



