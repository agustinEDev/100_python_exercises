# Ejercicio 57
# Escribir una función que invierte el orden de las palabras de una frase

# Función que invierte una frase
def invertirFrase (frase):
    lista = frase.split()
    lista.reverse()
    return " ".join(lista)

# Llamada a la función
print(invertirFrase(input("Introduce una frase: ")))