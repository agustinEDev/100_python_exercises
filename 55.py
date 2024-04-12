# Ejercicio 55
# Programa que mediante una función nos dice los índices de las apariciones de
# un elemento en una lista.

def posisicionEltLista (L, x):
    posiciones = []
    for i in range(0, len(L)):
        if L[i] == x:
            posiciones.append(i)
    return posiciones

# Llamada a la función
pos = posisicionEltLista([1,2,3,6,8,7,3], 3)
# pos = posisicionEltLista([6,8,9,1,3,7], -1)

if pos == []:
    print("El elemento no se encuentra en la lista")
else:
    print("El elemento se encuentra en las posiciones: ", pos)