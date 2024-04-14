# Ejercicio 65
# Programa que devuelve el número de archivos en una carpeta
import os

def numero_archivos(ruta):
    numero_archivos = 0
    for archivo in os.listdir(ruta):
        if os.path.isfile(os.path.join(ruta, archivo)):
            numero_archivos += 1
    return numero_archivos

# Llamada a la función
print(numero_archivos('./'))