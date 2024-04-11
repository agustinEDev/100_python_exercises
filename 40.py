# Ejercicio 40
# Función que toma una lista y devuelve el valor máximo

# Función que toma una lista y devuelve el valor máximo
def maximo (L):
    max = L[0]
    for elmt in L:
        if elmt > max:
            max = elmt
    return max

# Lista
L = [-9, 2, 4, 1, 8]

# Llamada a la función
print(maximo(L))