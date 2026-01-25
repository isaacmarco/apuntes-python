import sympy as sy
from sympy import cos

'''
    derivadas e integrales
'''

# derivar
x = sy.Symbol('x')
derivada = sy.diff(cos(x), x)
print(derivada)

# integrar
integral = sy.integrate(cos(x), x)
print(integral)

# representacion simbolica de derivadas e integrales
exp1 = sy.Derivative(cos(x), x, 1)  # el ultimo parametro indica que es la primera derivada (1)
exp2 = sy.Integral(cos(x), x)
print(exp2)