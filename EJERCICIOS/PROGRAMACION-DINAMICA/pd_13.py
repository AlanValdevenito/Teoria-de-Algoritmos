# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y 
# la cantidad de integrantes que conforma a cada uno.

# Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo 
# en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su 
# grupo pueden sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor 
# cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos).

# Indicar y justificar la complejidad del algoritmo.

# Similar al problema de la mochila:
# - Capacidad de la mochila ⇾ Capacidad de la mesa
# - Peso del objeto n ⇾ Cantidad de personas que integran el grupo n

# Ecuacion de recurrencia: OPT(n,W) = max{no sentar el grupo, sentar el elemento} = 
#                                   = max{OPT(n-1, W), OPT(n-1, W-Pi) + Pi}

def memorizacion(P, n, W):
    mem = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        elem = P[i-1]
        for j in range(1, W+1):

            if elem > j:
                mem[i][j] = mem[i-1][j]

            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j - elem] + elem)

    return mem

def bodegon_solucion(mem, elementos, n, W):
    solucion = []

    while n > 0 and W >= 0:

        if mem[n][W] != mem[n-1][W]:
            solucion.append(elementos[n-1])
            W -= elementos[n-1]

        n -= 1

    solucion.reverse()
    return solucion

def bodegon_dinamico(P, W):
    n = len(P)
    mem = memorizacion(P, n, W)
    return bodegon_solucion(mem, P, n, W)

# Complejidad: Tenemos O(n x W) por calcular la matriz de memorizacion, donde n es el numero de grupos y W es la capacidad
# de la mesa, y O(n) por recuperar la solucion ya que en el peor de los casos recorre los elementos una vez. Luego, la
# complejidad total es O(n x W).

# Tests RPL

assert bodegon_dinamico([6], 12) == [6]
assert bodegon_dinamico([5, 6], 12) == [5, 6]
assert bodegon_dinamico([1, 3], 4) == [1, 3]
assert bodegon_dinamico([10, 7, 5, 13], 16) == [10, 5]