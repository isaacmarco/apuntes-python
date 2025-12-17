# lectura de un fichero
manejador_fichero = open('fichero.txt', 'r')
manejador_fichero.read()

# por lineas
for linea in manejador_fichero:
    pass

# enumerando lineas
for numero_linea, linea in enumerate(manejador_fichero, start=1):
    print(f'{numero_linea}, {linea}')

# leer una linea: cada vez que ejecutamos el metodo, el puntero
# dentro del fichero apunta a la siguiente linea
manejador_fichero.readline()

# escritura de un fichero
manejador_fichero = open('fichero.txt', 'w')
for i in range(10):
    manejador_fichero.write(i)
manejador_fichero.close() # al escribir hay que cerrar el fihcero

# podemos utilizar contexto para automatizar el uso de ficheros
with open('fichero.txt', 'w') as manejador_fichero:
    for i in range(10):
        manejador_fichero.write(i)