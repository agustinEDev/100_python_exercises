# Ejercicio 59
# Programa con una función que recibiendo 3 listas, las une, elimina duplicados 
# y la devuelve ordenada

def unionLista (L1, L2, L3):
    L1 = L1 + L2 + L3
    return sorted(list(set(L1)))

print(unionLista([3,6,9,3], [1,0,3], [12,6,0]))
print(unionLista([7,44,-3], [], [7,2,7]))