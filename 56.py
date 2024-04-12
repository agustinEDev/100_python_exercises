# Ejercicio 56
# Programa que mediante una función filtra palabras por longitud mínima.

def filtrarPalabras (frase, longitud):
    frase = frase.split()
    cadena = []
    for palabra in frase:
        if len(palabra) >= longitud:
            cadena.append(palabra)
    return " ".join(cadena)

# Llamada a la función
print(filtrarPalabras("Hola a todos", 4))
print(filtrarPalabras("¿Cuál es tu origen?", 3))