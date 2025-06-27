# Definimos a un grafo ordenado como un grafo dirigido con vértices 1, ... , vn en el que todos los vértices, salvo vn tienen al menos una arista que sale 
# del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es decir, las aristas tienen la forma (vi, vj ) con i < j). 

# Implementar un algoritmo de programación dinámica que dado un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) determine cuál 
# es la longitud del camino más largo. 

# Dar la ecuación de recurrencia correspondiente. 

# Dar también el algoritmo de recontrucción de la solución. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Nota: Este problema es similar al problema ...

# ¿Que tipo de problema es?. Es un problema de maximizacion ya que nos piden determinar la longitud del camino mas largo.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de vertices.

# Ejemplo: Consideremos los vertices ordenados [1, 2, 3, 4, 5] donde las aristas son (1,2), (1,4), (2,4), (2,5), (3,4), (4,5).

# OPT[0] = 0
# OPT[1] = 1 (1 → 2)
# OPT[2] = 0
# OPT[3] = 2 (1 → 2 → 4)
# OPT[4] = 3 (1 → 2 → 4 → 5)

# ¿Como se componen estos subproblemas para solucionar subproblemas mas grandes?.

# OPT[0] = 0
# OPT[1] = 1 + OPT[0] (1 → 2)
# OPT[2] = 0
# OPT[3] = max(1 + OPT[2], 1 + OPT[1], 1 + OPT[0]) = max(1 + 0, 1 + 1, 1 + 0) = max(1, 2, 1) = 2 (1 → 2 → 4)
# OPT[4] = max(1 + OPT[3], 1 + OPT[1]) = max(1 + 2, 1 + 1) = max(3, 2) = 3 (1 → 2 → 4 → 5)

# Ecuacion de recurrencia: OPT[i] = max(1 + OPT[j]) para todo vertice j predecesor al vertice i

from grafo import Grafo

def camino_mas_largo_dinamico(grafo, vertices, n):
    mem = [0] * n

    for i in range(0, n):
        v = vertices[i]
        opciones = []

        for j in range(0, i):
            w = vertices[j]

            if grafo.estan_unidos(w, v):
                opciones.append(1 + mem[j])

        mem[i] = max(opciones) if len(opciones) > 0 else 0

    return mem

def camino_mas_largo_solucion(grafo, vertices, mem, i):
    solucion = []
    
    solucion.append(vertices[i])

    while (i > 0):
        v = vertices[i]

        for j in range(0, i):
            w = vertices[j]

            if grafo.estan_unidos(w, v):
                if (mem[i] == 1 + mem[j]):
                    solucion.append(w)
                    i  = j
                    break    

    solucion.reverse()
    return solucion

def camino_mas_largo(grafo, vertices):
    n = len(vertices)

    mem = camino_mas_largo_dinamico(grafo, vertices, n)
    solucion = camino_mas_largo_solucion(grafo, vertices, mem, n-1)
    return mem[n-1], solucion

grafo = Grafo(True, ["1","2","3","4","5"])

grafo.agregar_arista("1","2")
grafo.agregar_arista("1","4")

grafo.agregar_arista("2","4")
grafo.agregar_arista("2","5")

grafo.agregar_arista("3","4")

grafo.agregar_arista("4","5")

assert camino_mas_largo(grafo, ["1","2","3","4","5"]) == (3, ["1","2","4","5"])

# Complejidad

# Matriz de memorizacion: La complejidad resulta ser O(V + E) con V la cantidad de vertices y E la cantidad de aristas.

# Reconstruccion de la solucion: La complejidad resulta ser O(V x V) con V la cantidad de vertices.

# Luego, la complejidad total resulta resulta ser O(V x V) con V la cantidad de vertices.