import sympy as sy
x = sy.Symbol('x')
exp = sy.sin(x) / x
limite = sy.limit(exp, x, 0)    # el ultimo valor indica: cuando se acerca a 0, sy.oo para infinito o -sy.oo
print(limite)
