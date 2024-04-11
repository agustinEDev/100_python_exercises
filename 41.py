# Ejercicio 41
# Función que recibe una lista y dos índices para sumar los elementos entre 
# esos índices.

# Función que recibe una lista y dos índices para sumar los elementos entre
# esos índices.
def sumaSublista (L, i, f):
    suma = 0
    for j in range(i, f+1):
        suma += L[j]
    return suma

# Lista
L = [4,10,12,16,18]

# Llamada a la función
print(sumaSublista(L, 2, 4))