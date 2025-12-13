edad = 30

# if, elif, else
if edad < 20:
    pass
elif edad < 30:
    pass
else:
    pass

# obtener la posicion en memoria
id(edad)

# 'is' comprueba si dos objetos tienen la misma direccion
otroObjeto = None
if edad is otroObjeto:
    pass

# match-case (switch): no se pueden usar variables en el case, tienen que ser literales
nombre = 'luis'
match nombre:
    case 'ana':
        pass
    case 'luis':
        pass
    case _:
        print('por defecto')

# tuplas
punto = (2, 3)
match punto:
    case (x, y):
        print('dos puntos')
    case (x, y, z):
        print('tres puntos')


# operador morsa := permite asignar valor a una variable dentro de una expresion
if (linea := input('Escribe algo: ')) != '':
    print(f'Has escrito: {linea}')


