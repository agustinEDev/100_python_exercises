# Ejercicio 44
# Recreación de la función len()

# Función que calcula la longitud de una lista
def longitud (L):
    cont = 0
    for i in L:
        cont += 1
    return cont

print(longitud([3,6,7,"abde", [1,3,57], True]))
print(longitud([]))