import sympy as sy
'''
    Las matrices que construyen como en numpy, por filas
    |1   2|
    |3   4|
'''
m = sy.Matrix([[1,2], [3, 4]])

# crear una matriz con lambda generador
# la matriz creada es de 3x4
# la funcion generadora da un valor para la fila m, columna n
# cada elemento es 10 * fila + columna
m = sy.Matrix(3, 4, lambda m, n: 10 * m + n)

# otras formas de definir matrices
a, b, c, d = sy.symbols('a b c d')
M = sy.Matrix([[a,b], [c,d]])

# operar con matrices

operacion = M * M

x = sy.Symbol('x')
operacion = M * x
print(operacion)

'''
    Si creo una matriz con dos simbolos (una sola tupla) los organizara como
    una columna, en vertical (porque los vectores se representan así)
    
    x = |x1|
        |x2|
'''
x = sy.Matrix(sy.symbols('x_1, x_2'))
operacion = M * x   # producto matricial
print(operacion)
