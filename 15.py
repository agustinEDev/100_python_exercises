# Ejercicio 15
# Inicializamos una lista y llenamos otra con 1 de cada 3 valores de la primera.

"""Forma 1"""
# Inicializamos la lista
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializamos la lista que contendrá 1 de cada 3 valores de la lista L
L2 = []

for i in range(0, len(L), 3):
    L2.append(L[i])

# Imprimimos la lista
print("Lista L2: ", L2)

"""Forma 2"""
# Inicializamos la lista
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializamos la lista que contendrá 1 de cada 3 valores de la lista L
L2 = []
i = 0
while i < len(L):
    L2.append(L[i])
    i += 3

# Imprimimos la lista
print("Lista L2: ", L2)