# Ejercicio 58
# Programa que devuelve una lista de tuplas con los elementos de la lista
# y el número de apariciones en ella

def numeroOcurrencias(L):
    occ = []
    cnt = 0
    for elmt in L:
        for i in range (len(L)):
            if L[i] == elmt:
                cnt += 1
        occ.append((elmt, cnt))
        cnt = 0
    return list(set(occ))

# Llamada a la función
print(numeroOcurrencias([-4,8,-3,2,1,2,7,9,-3,8,1]))
print(numeroOcurrencias(['a', 3, 4, 'b', 'a', 3]))