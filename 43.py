# Ejercicio 43
# Recreación de la función min

def minimo (L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

print(minimo([-9,2,4,1,8]))
print(minimo([-3,1,7,6,2,3]))