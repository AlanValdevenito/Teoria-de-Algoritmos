# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
# Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo que, por programación dinámica, reciba 
# los valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total.

# Indicar y justificar la complejidad del algoritmo implementado.

# Ecuacion de recurrencia: OPT(n,W) = max{no usar el elemento, usar el elemento} = 
#                                   = max{OPT(n-1, W), OPT(n-1, W-Pi) + Vi}

VALOR = 0
PESO = 1

def mochila_dinamico(elementos, n, W):
    mem = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        elem = elementos[i-1]
        for j in range(1, W+1):

            if elem[PESO] > j:
                mem[i][j] = mem[i-1][j]

            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j - elem[PESO]] + elem[VALOR])

    return mem

def mochila_solucion(mem, elementos, n, W):
    solucion = []

    while n > 0 and W >= 0:

        if mem[n][W] != mem[n-1][W]:
            solucion.append(elementos[n-1])
            W -= elementos[n-1][PESO]

        n -= 1

    solucion.reverse()
    return solucion

# Cada elemento i es de la forma (valor, peso)
def mochila(elementos, W):
    n = len(elementos)
    mem = mochila_dinamico(elementos, n, W)
    return mochila_solucion(mem, elementos, n, W)

# Complejidad: Tenemos O(n x W) por calcular la matriz de memorizacion, donde n es el numero de elementos y W es la capacidad
# de la mochila, y O(n) por recuperar la solucion ya que en el peor de los casos recorre los elementos una vez. Luego, la
# complejidad total es O(n x W).

assert mochila([(10,6), (1,1), (8,3), (100,100), (6,4), (11,2), (7,8), (2,7), (11,9)], 20) == [(10, 6), (8, 3), (11, 2), (11, 9)]
assert mochila([(5, 6)], 12) == [(5, 6)]

# Tests RPL

assert mochila([(5, 10)], 10) == [(5, 10)]
assert mochila([(5, 5), (3, 3), (7, 7)], 10) == [(3, 3), (7, 7)]
assert mochila([(1, 1), (2, 1), (3, 1)], 2) == [(2, 1), (3, 1)]
assert mochila([(15, 7), (8, 4), (8, 4)], 8) == [(8, 4), (8, 4)]
assert mochila([(3, 2), (4, 3), (5, 4), (6, 5)], 5) == [(3, 2), (4, 3)]
assert mochila([(10, 1), (15, 2), (40, 3)], 6) == [(10, 1), (15, 2), (40, 3)]
assert mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11) == [(2, 3), (9, 8)]