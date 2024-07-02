# Modificar el algoritmo anterior para que, dada una lista de enteros positivos L y un entero n, devuelva un subconjunto de L que sume 
# exactamente n, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de n.

def _sumatorias_n(lista, n, subconjunto_actual, subconjunto_optimo, actual):

    if (sum(subconjunto_actual) == n):
        subconjunto_optimo.clear()
        subconjunto_optimo.extend(subconjunto_actual)
        return
    
    if (sum(subconjunto_actual) > n) or (actual >= len(lista)):

        if (sum(subconjunto_actual) < n) and (sum(subconjunto_actual) > sum(subconjunto_optimo)):
            subconjunto_optimo.clear()
            subconjunto_optimo.extend(subconjunto_actual)

        return
    
    subconjunto_actual.append(lista[actual])
    _sumatorias_n(lista, n, subconjunto_actual, subconjunto_optimo, actual+1)

    subconjunto_actual.pop()
    _sumatorias_n(lista, n, subconjunto_actual, subconjunto_optimo, actual+1)

    return

def max_sumatoria_n(lista, n):
    subconjunto_optimo = []

    _sumatorias_n(lista, n, [], subconjunto_optimo, 0)

    return subconjunto_optimo

assert max_sumatoria_n([1,2,3,4,5,6,8,9], 12) == [4,8]
assert max_sumatoria_n([1,2,3], 12) == [1,2,3]