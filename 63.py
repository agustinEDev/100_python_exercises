# Ejercicio 63
# Programa que suprime un caracter dado en todas sus ocurrencias de un fichero
from pathlib import Path

def eliminarCaracter(rutaFichero, caracter):
    fichero = Path(rutaFichero)
    contenido = fichero.read_text()
    contenido = contenido.replace(caracter, '')
    fichero.write_text(contenido)
    return contenido

# Llamada a la función
print(eliminarCaracter('./files/fichero.txt', 'o'))