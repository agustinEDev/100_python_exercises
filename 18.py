# Ejercicio 18
# Ordenamos una lista de tuplas en orden ascendente por el segundo elemento de 
# cada tupla.

# Inicializamos la lista de tuplas
L = [("Manzana", 15), ("Banana", 8), ("Fresa", 12), ("Kiwi", 9), 
     ("Melocotón", 2)]

# Ordenamos la lista de tuplas
L.sort(key=lambda x: x[1])

# Imprimimos la lista de tuplas ordenada
print("Lista de tuplas ordenada: ", L)