# Ejercicio 61
# Programa con una función que recibe la ruta de un fichero y lee su contenido
from pathlib import Path

def leerFichero (rutaFichero):
    fichero = Path(rutaFichero)
    return fichero.read_text()

# Llamada a la función
print(leerFichero('./files/fichero.txt'))
