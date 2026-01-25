import sympy as sy

'''
    La ecuacion cuadratica
    x^2 - x = 0 
    
    factorizando
    x^2 - x = x(x - 1)
    
    regla del producto 0
    x(x - 1 ) = 0
    
    x = 0 ó x - 1 = 0 -> x = 1
    
    sympy devuelve la lista de soluciones [0, 1]
    
'''
x, y, z = sy.symbols('x y z')
solucion = sy.solve(x**2 - x, x)
print(solucion)

'''
    otro ejemplo: resolviendo el sistema de ecuaciones
    x - y + 2 = 0
    x + y - 3 = 0
    (x, y) = (1/2, 5/2)
'''

solucion = sy.solve([x - y + 2, x + y - 3], [x, y])
print(solucion)

'''
    otro sistema mas de ecuaciones
'''
eq1 = x + 2 * y - 1
eq2 = x - y + 1
solucion = sy.solve([eq1, eq2], [x, y])
print(solucion)
