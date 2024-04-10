# Ejercicio 29
# Programa que mezcla aleatoriamente elementos de una lista.

import random

# Creamos una lista con los elementos que queremos mezclar
L = [3, 6, 8, 7, 2, 's', 'ch', 'd']

# Mezclamos los elementos de la lista
random.shuffle(L)

# Mostramos la lista mezclada
print(L)