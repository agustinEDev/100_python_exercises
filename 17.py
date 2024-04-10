# Ejercicio 17
# Buscamos elementos en común entre dos listas.

"""Forma 1"""
# Inicializamos las listas
L1 = [9, 8, 7, 14, 3, 2, 'a', 'p', 'hola', 'b']
L2 = ['b', 1, 9.2, 6, 3, 9, 'p']

# Convertimos las listas en conjuntos
C1 = set(L1)
C2 = set(L2)

# Buscamos los elementos en común
comunes = C1.intersection(C2)

# Imprimimos los elementos en común
print("Elementos en común: ", comunes)

"""Forma 2"""
# Inicializamos las listas
L1 = [9, 8, 7, 14, 3, 2, 'a', 'p', 'hola', 'b']
L2 = ['b', 1, 9.2, 6, 3, 9, 'p']

# Inicializamos la lista que contendrá los elementos en común
comunes = set(L1).intersection(set(L2))

# Transformamos el conjunto en lista
comunes = list(comunes)

# Imprimimos los elementos en común
print("Elementos en común: ", comunes)