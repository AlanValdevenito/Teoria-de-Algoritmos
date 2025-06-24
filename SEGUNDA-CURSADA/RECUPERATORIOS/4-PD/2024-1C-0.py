# Sea G un grafo dirigido “camino” (las aristas son de la forma (v_i, v_i−1)). Cada vertice tiene un valor (positivo).

# Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima dentro de un grafo de dichas características. 

# Dar la ecuación de recurrencia correspondiente al problema. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# Indicar y justificar la complejidad espacial del algoritmo implementado, y si hay una optimización que permita consumir menos espacio.

# Nota: En un grafo dirigido, un vertice v se domina a si mismo y a sus vecinos salientes (los vertices w tales que hay una arista v -> w)

# ¿Que tipo de problema es?. Es un problema de minimizacion ya que nos piden obtener el Dominating Set de suma minima.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de vertices.

# Casos:
# 1) Incluir el vertice i que se domina a si mismo
# 2) Incluir el vertice i-1 que se domina a si mismo y al vertice i

# Ejemplo: Consideremos el grafo dirigido "camino" con los siguientes vertices [100, 20, 30, 70, 50].

# OPT[0] = 100
# OPT[1] = 100
# OPT[2] = min(30 + 100, 20 + 10) = min(130, 120) = 120
# OPT[3] = min(70 + OPT[2], 30 + OPT[1]) = min(70 + 120, 30 + 100) = min(190, 130) = 130
# OPT[4] = min(50 + OPT[3], 70 + OPT[2]) = min(50 + 130, 70 + 120) = min(180, 190) = 180

# [100, 100, 120, 130, 180]

# ¿Como se componen estos subproblemas para solucionar subproblemas mas grandes?.

# Ecuacion de recurrencia: OPT[i] = min(vertice[i] + OPT[i-1], vertice[i-1] + OPT[i-2]) con i > 1

# Casos base:
# 1) Si tenemos 1 vertice elegimos ese
# 2) Si tenemos 2 vertices elegimos el vertice i ya que se domina a si mismo y al vertice i+1

from grafo import Grafo
from orden_topologico import orden_topologico

def dominating_set_min_dinamico(vertices, n):
    mem = [0] * (n)

    # Caso base 1
    mem[0] = vertices[0]

    # Caso base 2
    mem[1] = vertices[0]

    for i in range(2, n):
        incluir_actual = vertices[i] + mem[i-1]
        incluir_anterior = vertices[i-1] + mem[i-2]

        mem[i] = min(incluir_actual, incluir_anterior)

    return mem

def dominating_set_min_solucion(vertices, mem, i):
    solucion = []

    while i >= 2:
        # Caso 2: Incluir al vertice i-1 que se domina a si mismo y al vertice i
        if mem[i] == vertices[i - 1] + mem[i - 2]:
            solucion.append(vertices[i - 1])
            i -= 2
        # Caso 1: Incluir el vertice i que se domina a si mismo
        else:
            solucion.append(vertices[i])
            i -= 1

    # Caso base 2
    solucion.append(vertices[0])

    solucion.reverse()
    return solucion

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    n = len(vertices)

    vertices = orden_topologico(grafo, vertices[n-1], vertices[0])

    mem = dominating_set_min_dinamico(vertices, n)
    solucion = dominating_set_min_solucion(vertices, mem, n-1)

    return mem[n-1], solucion

grafo = Grafo(True, [50, 70, 30, 20, 100])

grafo.agregar_arista(100,20)
grafo.agregar_arista(20,30)
grafo.agregar_arista(30,70)
grafo.agregar_arista(70,50)

assert dominating_set_min(grafo) == (180, [100, 30, 50])


# Complejidad

# Matriz de memorizacion: La complejidad resulta ser O(V) con V la cantidad de vertices.

# Reconstruccion de la solucion: La complejidad resulta ser O(V) con V la cantidad de vertices.

# Luego, la complejidad total resulta resulta ser O(V) con V la cantidad de vertices.


# Complejidad espacial

# Dado que se almacenan los resultados de la memorizacion en un arreglo la complejidad espacial resulta ser O(V) con V la cantidad de vertices.

# La ecuacion de recurencia solo depende de los dos ultimos valores de la matriz de memorizacion, con lo cual podriamos reemplazar todo el arreglo
# por solo dos variables lo cual la complejidad espacial resultaria ser O(1). Sin embargo, esto solo podria hacerse si no buscamos reconstruir la solucion.