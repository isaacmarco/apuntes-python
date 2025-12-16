conjunto = {1, 2, 3}

# no se puede definir así el conjunto vacío = {}!
# hay que usar set()
vacio = set()

# convertir
set('banana') # el conjunto elimina los repetidos, dejando: {b a n}

# no se puede extraer un elemento, para añadirlo:
conjunto.add(6)

# se pueden eliminar
conjunto.remove(2)

# se pueden interar normalmente
for elemento in conjunto:
    pass

# pertenencia y no pertenencia
existe = 3 in conjunto
existe = 0 not in conjunto

# operaciones con conjuntos
A = {1, 2}
B = {2, 3}

# interseccion (elementos en A y B)
A & B
# union (elementos en A y B o en A o B)
A | B
# diferencia (elementos de A que no están en B)
A - B
# diferencia simetrica (elementos no comunes de A y B)
A ^ B


