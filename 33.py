# Ejercicio 33
# Creamos una lista con los positivos de otra lista por comprensión

# Creamos la primera lista
L = [-6, 5, -3, -1, 2, 8, -3.6]

# Creamos la segunda por comprensión
L1 = [i for i in L if i>=0]

# Imprimimos la lista resultante
print(L1)