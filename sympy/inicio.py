'''

    biblioteca para la representacion simbolica matematica
    pip install sympy. La salida por consola por defecto no es bonita,
    depende del entorno de desarrollo y de si se esta haciendo prettyprint
    - un simbolo representa, por ejemplo, un entero, mientras que una variable
        int representa el valor que tiene actualmente ese entero
    - sympy no tiene precision arbitraria, no tiene ni maximo ni minimo
'''

import sympy as sy
x = sy.Symbol('x')
z = sy.Symbol('variable1')
e = x + z
# el print se veria: variable1 + x

'''
    propiedades de un simbolo
    is real, is imaginary
    is positive, is negative
    is integer
    is odd, is even
    is prime
    is finite, is infinite
'''

# coseno de pi*n
n = sy.Symbol('n')
expresion = sy.cos(n * sy.pi)
print(expresion)

# numeros
x = sy.Integer(3)
y = sy.Float(12.3)

# nueros racionales (simplifica las operaciones automaticamente)
fraccion_1 = sy.Rational(2, 3)
fraccion_2 = sy.Rational(1, 2)
resultado = fraccion_1 * fraccion_2
print(f'{fraccion_1} * {fraccion_2} = {resultado}')

'''
    constantes de sympy
    pi
    E (e)
    EulerGamma (constante de euler)
    I (unidad de la parte imaginaria)
    oo (infinito)
'''

# funciones lambda (como parametro de este metodo siempre va una tupla
# y ademas los valores tienen que ser simbolos de sympy ya declarados
x = sy.Symbol('x', integer=True)
funcion = sy.Lambda(x, x + 1)
print(funcion(5))

# funciones
x, y, z = sy.symbols('x y z')
f = sy.Function('f')
f(x)    # f de x
g = sy.Function('g')(x, y, z) # g(x, y, z)


# expresiones
x = sy.symbols('x')
exp = 1 + 2 * x**2 + 3 * x**3   # 3x^3 + 2x^2 + 1
print(exp.args) # muestra la lista de argumentos (podemos acceder a ellos como en una lista)
# cada argumento es una lista de argumentos, así que podemos ir
# profundizando
exp.args[0] # '1'
exp.args[1] # '2x^2'
exp.args[1].args[0] # '2'
exp.args[1].args[1] # 'x^2'
exp.args[1].args[1].args[0] # 'x'
# etc.

# evaluaciones
x = sy.Symbol('x')
x = sy.sqrt(9)  # muestra simbolicamente
x.evalf()       # da el resultado

# evaluación numérica (deja de ser simbolico)
y, z = sy.symbols('y z')
z = sy.cos(2 * y)   # cos(2*y)
z.evalf(subs={y: 2.4})   # evaluar dando un valor a y

# evaluaciones simbolicas
x, y, z = sy.symbols('x y z')
exp = x**3 + 4*x*y - z
ev = exp.subs([(x, 2), (y, 4), (z, 0)]) # damos un valor a cada simbolo y calculamos
print(ev)



