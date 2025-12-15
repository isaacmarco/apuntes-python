# tipos de diccionarios
diccionario = {
    'isaac': 12,
    'ana': 33
}
otro_tipo = {
    1: 'A',
    2: 'B'
}
vacio = {}

# funcion dict() -> persona = {'nombre':'isaac', 'edad':33}
persona = dict(
    nombre='isaac',
    edad=33
)

# uso
edad = diccionario['isaac']
edad = diccionario.get('isaac', 'No disponible') # devuelve None por defecto si no le especificamos
diccionario['isaac'] = 46

# comprobar si existe la llave con 'in'
existe = 'isaac' in diccionario

# obtener todos los elementos
diccionario.keys()
diccionario.values()
diccionario.items() # keys y valores

# podemos iterar simultaneamente por llaves y valores
for llave, valor in diccionario.items():
    pass

# borrar elementos
del diccionario['isaac'] # por la clave
edad = diccionario.pop('isaac') # borrado con extraccion

# completo
diccionario.clear()

# combinar diccionarios:
# si la clave no existe se añade
# si la clave ya existia, su valor se actualiza
dic1 = {}
dic2 = {}
diccionario_combinado = dic1 | dic2
# si queremos podemos actualizar los diccionarios, modificandolos
dic1.update(dic2)




