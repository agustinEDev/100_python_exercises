# Ejercicio 62
# Programa que busca el número de ocurrencias de una palabra en un fichero
from pathlib import Path

def numOccFichero (rutaFichero, palabra):
    fichero = Path(rutaFichero)
    contenido = fichero.read_text()
    return contenido.count(palabra)

# Llamada a la función
print(numOccFichero('./files/fichero.txt', 'mundo'))