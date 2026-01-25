import sympy as sy

# simplificando expresiones
x = sy.Symbol('x')
exp = 2 * (x**2 - x) - x * (x + 1)
simplificado = sy.simplify(exp)
print(f'sin simplificar: {exp}')
print(f'simplificada: {simplificado}')

# tambien se puede expandir: quitar los parentesis y desarrollarlo,
# en este caso, aplicar la propiedad distributiva
(x, y, z) = sy.symbols('x, y, z')
exp = (x + 1) * (x + 2)
expandido = sy.expand(exp)
print(expandido)

# factorizaciones: para expresar como factores, como el clasico sumas o
# diferencias de cuadrados a^2 - b^2 = (a - b)(a + b)
x, y, z = sy.symbols('x y z')
factor = sy.factor(x**2 - 1)
print(factor)





