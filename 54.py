# Ejercicio 54
# Programa que llama a una función para eliminar los espacios de una cadena.

def eliminarEsp (frase):
    return frase.replace(" ", "")

frase = input("Introduce una frase: ")
print("Frase sin espacios: ", eliminarEsp(frase))