# Dado un arreglo de enteros ordenado, un elemento y un valor entero k, implementar una función que, usando división
# y conquista, encuentre los k valores del arreglo más cercanos al elemento en cuestión (que bien podría estar en el
# arreglo, o no).

# La complejidad de la función implementada debe ser menor a O(n), suponiendo que k < n. 

# Justificar adecuadamente la complejidad del algoritmo implementado.

def _k_mas_cercanos(arreglo, elemento, k, indice):
    n = len(arreglo)
    cercanos = []

    izq, der = indice, indice + 1

    # Caso borde: El elemento no se encuentra en el arreglo
    if (arreglo[indice] == elemento):
        izq -= 1

    while len(cercanos) < k:

        if izq < 0:  # No quedan elementos a la izquierda, entonces guardamos los de la derecha
            cercanos.append(arreglo[der])
            der += 1

        elif der >= n:  # No quedan elementos a la derecha, entonces guardamos los de la izquireda
            cercanos.append(arreglo[izq])
            izq -= 1

        else:  # Hay elementos tanto a izquierda como a derecha, entonces comparamos cuál está más cerca del elemento

            if abs(arreglo[izq] - elemento) <= abs(arreglo[der] - elemento):
                cercanos.append(arreglo[izq])
                izq -= 1

            else:
                cercanos.append(arreglo[der])
                der += 1

    return cercanos

def busqueda_binaria(arreglo, inicio, fin, elemento):
    
    if (inicio > fin):
        return fin
    
    medio = (inicio + fin) // 2

    if (elemento == arreglo[medio]):
        return medio

    if (elemento < arreglo[medio]):
        return busqueda_binaria(arreglo, inicio, medio-1, elemento)
    
    return busqueda_binaria(arreglo, medio+1, fin, elemento)

def k_mas_cercanos(arreglo, elemento, k):
    n = len(arreglo) - 1

    indice = busqueda_binaria(arreglo, 0, n, elemento)

    return _k_mas_cercanos(arreglo, elemento, k, indice)

# Notamos que la funcion para buscar los k mas cercanos tiene una complejidad de O(k) debido a que hacemos como maximo k operaciones
# Luego, como por enunciado tenemos que k < n la complejidad de esta funcion resulta ser constante y el algoritmo depende de la busqueda binaria

# Complejidad

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0 (Operaciones adicionales)

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C log (n)) = O(n^0 log (n)) = O(log (n))
#    B         2                               B                2

assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 2) == [3, 5]
assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 3) == [5, 7, 4]

assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 9, 10], 8, 2) == [7, 9]
assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 9, 10], 5, 3) == [4, 6, 3]

assert k_mas_cercanos([1, 2, 3, 4, 20, 21, 22, 23, 24], 20, 3) == [21, 22, 23]