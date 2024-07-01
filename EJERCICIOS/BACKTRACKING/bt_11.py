# Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L y un entero n devuelva todos los subconjuntos 
# de L que suman exactamente n.

def _sumatorias_n(lista, n, subconjunto_parcial, subconjuntos, actual):

    if sum(subconjunto_parcial) == n:
        subconjuntos.append(subconjunto_parcial[:])
        return

    if (sum(subconjunto_parcial) > n) or (actual >= len(lista)):
        return
    
    subconjunto_parcial.append(lista[actual])
    _sumatorias_n(lista, n, subconjunto_parcial, subconjuntos, actual+1)

    subconjunto_parcial.pop()
    _sumatorias_n(lista, n, subconjunto_parcial, subconjuntos, actual+1)

    return

def sumatorias_n(lista, n):
    subconjuntos = []

    _sumatorias_n(lista, n, [], subconjuntos, 0)

    return subconjuntos

assert sumatorias_n([1,2,3,4,5,6,8,9], 12) == [[1, 2, 3, 6], [1, 2, 4, 5], [1, 2, 9], [1, 3, 8], [1, 5, 6], [2, 4, 6], [3, 4, 5], [3, 9], [4, 8]]