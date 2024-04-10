# Ejercicio 14
# Creamos una lista y le añadimos valores.

"""Forma 1"""
# Inicializamos la lista
L = []

# Añadimos valores a la lista
L.append(10)
L.append(25)
L.append(30)
L.append(45)
L.append(90)
L.append('ab')
L.append('cd')
L.append('ef')

# Imprimimos la lista
print("Lista L: ", L)

"""Forma 2"""
# Inicializamos la lista
L = []

# Añadimos valores a la lista
L += [10, 25, 30, 45, 90, 'ab', 'cd', 'ef']

# Imprimimos la lista
print("Lista L: ", L)

"""Forma 3"""
# Inicializamos la lista
L = []
valores = [10, 25, 30, 45, 90, 'ab', 'cd', 'ef']

for i in valores:
    L.append(i)

# Imprimimos la lista
print("Lista L: ", L)