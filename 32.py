# Ejercicio 32
# Programa que crea una lista por comprensión a partir de otra lista

# Creamos la primera lista
L = [3, 6, 9, 12, 15, 18, 21, 24]

# Creamos la segunda lista por comprensión con los elementos de la primera
# lista divididos entre 3.
L1 = [i/3 for i in L]

#Imprimimos la lista resultante
print(L1)