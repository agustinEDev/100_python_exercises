# Ejercicio 58
# Programa que devuelve una lista de tuplas con los elementos de la lista
# y el número de apariciones en ella

def numeroOcurrencias(L):
    occ = []
    for elmt in L:
        cnt = L.count(elmt)
        occ.append((elmt, cnt))
    return list(set(occ))

# Llamada a la función
print(numeroOcurrencias([-4,8,-3,2,1,2,7,9,-3,8,1]))
print(numeroOcurrencias(['a', 3, 4, 'b', 'a', 3]))