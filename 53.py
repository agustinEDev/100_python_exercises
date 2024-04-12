# Ejercicio 53
# Programa que llama a una función para que nos diga si una vocal está 
# contenida en una cadena de texto.

def presenciaVocal(frase):
    vocales = "aeiou"
    for vocal in vocales:
        if vocal in frase:
            return True
    return False
    
# Llamamos a la función
print(presenciaVocal(input("Ingrese una frase: ")))