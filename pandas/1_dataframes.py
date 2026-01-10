import pandas as pd
# un data frame es una suma de series, donde cada serie es una columna

# crear un dataframe desde un diccionario de listas,
# donde cada elemento del diccionario se convierte en una columna
# del dataframe
data = {'A': [1, 2, 3], 'B': [9, 1, 3]}
df = pd.DataFrame(data)

# crearlo desde una lista de diccionarios, donde cada elemento
# de la lista se convierte en una fila
data = [{'A': 1, 'B': 2, 'C': 3}, {'A': 4, 'B': 5, 'C': 6}]
df = pd.DataFrame(data)


# desde una lista de listas, cada elemento de la lista se convierte
# en una fila, y sus valores se despliegan en horizontal, hay que pasar
# los nombres de las columnas como un parametro opcional
data = [[1, 2], [3, 4], [5, 6]]
df = pd.DataFrame(data, columns=['A', 'B'])

# lo normal es construir el dataframe mediante las series de Panda
serieA = pd.Series(data=[1, 2, 3], name='serie A')
serieB = pd.Series(data=[4, 5, 6], name='serie B')
df = pd.DataFrame({'serieA': serieA, 'serieB': serieB})

# crear un dataframe de las islas canarias
islas = pd.Series(['Hierro', 'Fuerteventura', 'GC', 'Gomera', 'Lanzarote', 'Palma', 'TNF'])
poblacion = pd.Series([11423, 120021, 853262, 21798, 156112, 83439, 931646])
area = pd.Series([268.71, 1665.74, 1560.10, 369.76, 888.07, 708.32, 2034.38])
provincia = pd.Series(['TF', 'LP', 'LP', 'TF', 'LP', 'TF', 'TF'])
democan = pd.DataFrame({'Island': islas, 'Population': poblacion, 'Area': area, 'Province': provincia})

# panda asigna automaticamente un indice. Se puede convertir una columna
# en indice con set_index. El metodo no cambia la tabla original, hay que asignarle un destino
dataframe_indice_cambiado = democan.set_index('Population')
