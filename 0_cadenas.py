# conversiones
str(True)
str(33)
str(10.2)

int('10')
int(20.2)

float(10)
float('10.2')

# teclado
cadena = input('cadena:')
print(cadena)

# concatenar cadenas
cadena = 'mi ' + 'cadena'
print(cadena)

# repetir cadenas
cadena = 'gato'
print(cadena * 3) # gatogatogato

# acceso a caracteres mediante indice positivo o negativo
cadena = 'hola mundo cruel'
# cadena[0] -> primer caracter 1, 2, 3 ... ultimo caracter
# cadena[-1] -> ultimo caracter -2, -3, -4 ... primer caracter

# rebanadas
# [inicio:fin:paso] # el paso es = 1 por defecto
trozo = cadena[0:3]
# del 0 al 10 de 2 en 2
trozo = cadena[0:10:2]
# comienzo sin fin (hasta el final)
trozo = cadena[10:]
# fin sin comienzo (desde el comienzo por defecto)
trozo = cadena[:10]

# longitud de la cadena
len(cadena)

# pertenencia/no pertenencia a la cadena
cadena = 'mi galgo corre veloz'
resultado = 'galgo' in cadena
resultado = 'galgo' not in cadena

# limpiar cadenas
cadena.strip()

# busquedas en cadena
resultado = cadena.startswith('mi')
resultado = cadena.endswith('veloz')
resultado = cadena.find('galgo') # ademas, esta funcion soporta dos parametros para los intervalos de busqueda

# contar apariciones
cuenta = cadena.count('m')

# remplazar
cadena = 'mi cadena es bonita'
cadena.replace('bonita', 'fea') # un ultimo parametro indica el numero de veces que se cambiara

# mayusculas/minusculas
cadena.capitalize()
cadena.title()
cadena.upper()
cadena.lower()



