# Implementar un algoritmo que, por programación dinámica, resuelva el problema de la mochila con una variante:
# ahora se puede poner una cantidad ilimitada de un mismo elemento (es decir, se puede repetir), siempre y cuando
# aún haya lugar. Por ejemplo, si yo tengo un elemento de tamaño 3 y una mochila de tamaño 10, yo podría guardar
# 3 veces dicho elemento, si así lo quisiera (también menos cantidad). Escribir y describir la ecuación de recurrencia
# de la solución, y la complejidad del algoritmo implementado. 

# Implementar o explicar (la que prefieran) cómo sería el algoritmo de reconstrucción de la solución, indicando su complejidad.

# Ecuacion de recurrencia: OPT(n,W) = max(usar/repetir el elemento, no usar el elemento) =  max(OPT(n, W-Pi) + Vi, OPT(n-1, W))

VALOR = 0
PESO = 1

def mochila_dinamico(elementos, W, n):
    mem = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        elem = elementos[i-1]
        for j in range(1, W+1):

            if (elem[PESO] > j):
                mem[i][j] = mem[i-1][j]
                continue

            mem[i][j] = max(mem[i][j - elem[PESO]] + elem[VALOR], mem[i-1][j])

    return mem

def mochila_solucion(elementos, W, mem, n):
    solucion = []

    while (n > 0) and (W >= 0):

        if (mem[n][W] != mem[n-1][W]):
            solucion.append(elementos[n-1])
            W -= elementos[n-1][PESO]

        else: 
            n -= 1

    solucion.reverse()
    return solucion

def mochila(elementos, W):
    n = len(elementos)
    mem = mochila_dinamico(elementos, W, n)
    return mochila_solucion(elementos, W, mem, n)


# Complejidad

# Matriz de memorizacion: Iteramos para cada elemento todas las posibles capacidades de la mochila lo cual tiene una complejidad de O(n x W) donde
# n es la cantidad de elementos y W la capacidad de la mochila.

# Reconstruccion de solucion: Iteramos en el peor caso todos los elementos una vez lo cual tiene una complejidad de O(n) donde n es la cantidad de elementos.

# Luego, la complejidad total resulta ser O(n x W).


# Algoritmo de reconstruccion

# La matriz de memorizacion contiene los valores máximos que pueden lograrse para cada combinación de capacidad de la mochila (W) y cantidad de 
# elementos (n). La reconstrucción verifica si un elemento i fue incluido o no, observando cómo cambia el valor óptimo cuando se pasa de n a n−1 en la matriz.

# El algoritmo empieza desde el último elemento (n) y la capacidad total de la mochila (W). Luego, compara mem[n][W] (valor óptimo con 
# el elemento i disponible) con mem[n-1][W] (valor óptimo sin considerar el elemento i):
# - Si son iguales el elemento i no fue incluido y pasa al siguiente elemento sin modificar la capacidad.
# - Si son diferentes el elemento i fue incluido, por lo que lo agrega a la lista de solución y resta el peso del elemento a la 
# capacidad. No pasa al siguiente elemento ya que pueden repetirse.

# El algoritmo de reconstruccion termina cuando n = 0 o la capacidad restante de la mochila es W = 0.


assert mochila([(10,6), (1,1), (8,3), (100,100), (6,4), (11,2), (7,8), (2,7), (11,9)], 20) == [(11, 2), (11, 2), (11, 2), (11, 2), (11, 2), (11, 2), (11, 2), (11, 2), (11, 2), (11, 2)]
assert mochila([(5, 6)], 12) == [(5, 6), (5, 6)]

assert mochila([(5, 10)], 10) == [(5, 10)]
assert mochila([(5, 5), (3, 3), (7, 7)], 10) == [(5, 5), (5, 5)]
assert mochila([(1, 1), (2, 1), (3, 1)], 2) == [(3, 1), (3, 1)]
assert mochila([(15, 7), (8, 4), (8, 4)], 8) == [(8, 4), (8, 4)]
assert mochila([(3, 2), (4, 3), (5, 4), (6, 5)], 5) == [(3, 2), (4, 3)]
assert mochila([(10, 1), (15, 2), (40, 3)], 6) == [(40, 3), (40, 3)]
assert mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11) == [(2, 3), (9, 8)]