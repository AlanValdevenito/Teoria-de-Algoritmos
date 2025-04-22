# Dado un arreglo de enteros ordenado, un elemento y un valor entero k, implementar una función que, usando división
# y conquista, encuentre los k valores del arreglo más cercanos al elemento en cuestión (que bien podría estar en el
# arreglo, o no). 

# La complejidad de la función implementada debe ser menor a O(n), suponiendo que k < n. 

# Justificar adecuadamente la complejidad del algoritmo implementado.

def mas_cercanos(arreglo, elemento, indice, k):
    n = len(arreglo)
    cercanos = []

    izq = indice - 1
    der = indice + 1

    # Caso borde: El elemento no se encontraba en el arreglo con lo cual debemos ajustar el indice derecho
    if elemento != arreglo[indice]:
        der -= 1

    while len(cercanos) < k:

        if izq < 0:  # No quedan elementos a la izquierda, entonces guardamos los de la derecha
            cercanos.append(arreglo[der])
            der += 1

        elif der >= n:  # No quedan elementos a la derecha, entonces guardamos los de la izquireda
            cercanos.append(arreglo[izq])
            izq -= 1

        else:  # Hay elementos tanto a izquierda como a derecha, entonces comparamos cuál está más cerca del elemento

            if abs(elemento - arreglo[izq]) <= abs(elemento - arreglo[der]):
                cercanos.append(arreglo[izq])
                izq -= 1

            else:
                cercanos.append(arreglo[der])
                der += 1

    return cercanos

def busqueda_binaria(arreglo, elemento, inicio, fin):

    if inicio >= fin:
        return inicio
    
    medio = (inicio + fin) // 2

    if elemento == arreglo[medio]:
        return medio
    
    if elemento < arreglo[medio]:
        return busqueda_binaria(arreglo, elemento, inicio, medio)
    
    return busqueda_binaria(arreglo, elemento, medio+1, fin)

def k_mas_cercanos(arreglo, elemento, k):
    indice = busqueda_binaria(arreglo, elemento, 0, len(arreglo))
    return mas_cercanos(arreglo, elemento, indice, k)

# Complejidad

# A: 1 (Cantidad de llamados recursivos realizados en cada iteracion) 
# B: 2 (Proporcion de cada subproblema)
# C: 0 (Costo de partir y juntar)

# T(n) = A T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C log (n)) = O(n^0 log (n)) = O(log(n))
#    B         2                              B

# Por otro lado, la complejidad de buscar los puntos mas cercanos es O(K) con K la cantidad de puntos cercanos a buscar

# Luego, la complejidad total resulta ser O(log(n)) con n la cantidad de elementos del arreglo

assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 2) == [3, 5]
assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4, 4) == [3, 5, 2, 6]
assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 3) == [5, 7, 4]

assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 9, 10], 8, 2) == [7, 9]
assert k_mas_cercanos([1, 2, 3, 4, 5, 6, 7, 9, 10], 5, 3) == [4, 6, 3]

assert k_mas_cercanos([1, 2, 3, 4, 20, 21, 22, 23, 24], 20, 3) == [21, 22, 23]

assert k_mas_cercanos([1, 2, 3, 4], 4, 3) == [3, 2, 1]
assert k_mas_cercanos([1, 2, 3, 4], 1, 3) == [2, 3, 4]