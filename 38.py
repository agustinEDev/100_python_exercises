# Ejercicio 38
# Eliminar duplicados de una lista mediante una función

# Función para eliminar duplicados
def eliminarDuplicados (Lista):
    Lista = list(set(Lista))
    return Lista

# Llamada a la función
Lista = eliminarDuplicados([0,3,5,7,3,5,1,-1])

# Imprimir lista sin duplicados
print(sorted(Lista))