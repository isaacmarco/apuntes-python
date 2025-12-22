# pip install pandas
import pandas as pd
# si en numpy la clase principal es el array,
# en pandas las clases principales seran Series y Dataframes
# Podríamos pensar en una serie como un ndarray en el que cada valor
# tiene asignado una etiqueta (índice) y además admite un título (nombre).

# crear una serie desde una lista
pd.Series([1, 2, 3])
# utilizando indices (etiquetas) especificadas
serie = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
# utilizando un diccionario
items = {'a': 1, 'b': 2, 'c': 3}
# se puede asignar un nombre a la serie
pd.Series([1, 2, 3], name='Numeros enteros')

# atributos de las series
indices = serie.index
valores = serie.values
tipo_datos = serie.dtype
nombre = serie.name
numero_registros = serie.size


# seleccion de registros dentro de la serie
# se puede acceder por su posicion
reg = serie[0]
reg = serie[0:2] # etc
# mediante etiquetas
reg = serie['a']
reg = serie['a':'c'] # etc

# tambien se puede acceder directamete al comienzo o final
comienzo = serie.head(2) # dame los dos primeros
fin = serie.tail(2) # dame los dos ultimos

# operaciones con series
# filtrado de registros
matriz_booleana = serie > 2
reg = serie[serie > 2] # aplicamos la matriz booleana a la serie para obtener los valores

# ordenacion
serie.sort_values()

# conteno de valores
serie.count() # numero de registros no nulos
serie.value_counts() # frecuencias de la serie
serie.unique() # cuantos unicos

# operaciones aritmeticas
serie * 2 # multiplica por 2 todos los valores de la serie
# cuando operamos entre dos series,
# las operaciones aritmeticas se realizan entre los registros con la misma etiqueta
serieA = pd.Series([1, 2, 3])
serieB = pd.Series([2, 3, 4])
operacion = serieA + serieB # se aplica al resto de operaciones aritmeticas

# funciones estadisticas
serie.mean() # media
serie.std() # desviación standart
serie.min() # minimo valor
serie.max() # maximo valor
serie.argmin() # minimo indice
serie.margmax() # maximo indice
serie.idmix() # minimo etiqueta
serie.idmax() # maximo etiqueta

# exportar o convertir las series
lista = serie.tolist()
diccionario = serie.to_dict()
csv = serie.to_csv()
json = serie.to_json()
dataframe = serie.to_frame()
# hay muchos otros tipos de exportacion/conversión



