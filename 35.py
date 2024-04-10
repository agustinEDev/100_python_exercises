# Ejercicio 35
# Programa que llama a una función para saber si una lista contiene un valor

# Inicializamos la lista
L = []
elem = ''

# Rellenamos la lista y pedimos el valor a buscar
while elem == '':
    valor = input("Introduce un elemento a la lista. Para salir introduce 00: ")

    if valor == '00':
        elem = input("Introduce el valor a buscar en la lista: ")
        break
    else:
        L.append(valor)

# Función q comprueba si el elemento está en la lista
def VerifPresencia (elem, L):
    if elem in L:
        return True
    else:
        return False
    
# Llamada a la función
print(VerifPresencia(elem, L))