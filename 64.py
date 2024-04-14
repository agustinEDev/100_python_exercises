# Ejercicio 64
# Programa que busca la presencia de un número en un fichero
from pathlib import Path

def presenciaNumero (rutaFichero):
    fichero = Path(rutaFichero)
    contenido =  fichero.read_text()
    for caracter in contenido:
        if caracter.isdigit():
            return True
    return False

# Llamada a la función
print(presenciaNumero('./files/fichero.txt'))