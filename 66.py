# Ejercicio 66
# Programa que escribe un texto dado en un fichero
from pathlib import Path

def escribirFichero (nomFichero, texto):
    ruta = './files/' + nomFichero
    fichero = Path(ruta)
    fichero.write_text(texto)


# Llamada a la función
escribirFichero('ejercicio_66.txt', 'Prueba de escritura en fichero. Ejer. 66')