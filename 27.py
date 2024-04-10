# Ejercicio 27
# Programa que permite recuperar la extensión de este archivo.

import os

# Obtenemos el nombre del archivo
nombre = os.path.basename(__file__)

# Obtenemos la extensión (Valdría 1(segunda posición) o -1(última posición))
extension = nombre.split(".")[-1]

print(f"La extensión del archivo es: {extension}")