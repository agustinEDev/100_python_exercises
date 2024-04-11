# Ejercicio 45
# Calcular la media de una lista

# Función que calcula la media de una lista
def calular_media (L):
    suma = 0
    for elt in L:
        suma += elt
    return suma / len(L)

# Llamadas a la función
print(calular_media([1, 2, 3, 4, 5, 6, 7]))
print(calular_media([3,0,-1,5,6,9,17]))