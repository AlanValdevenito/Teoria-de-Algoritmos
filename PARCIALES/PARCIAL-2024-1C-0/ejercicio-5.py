# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi−1)). Cada vertice tiene un valor (positivo).

# Implementar un algoritmo que, utilizando programación dinámica, obtenga el Dominating Set de suma mínima dentro de un grafo de dichas características.

# Dar la ecuación de recurrencia correspondiente al problema.

# Indicar y justificar la complejidad espacial del algoritmo implementado, y si hay una optimización que permita consumir menos espacio.

# Notamos que este problema es similar al problema de Juan el vago:
# - Vertices = Trabajos

# Ecuacion de recurrencia: OPT(i) = min{dominar vertice i, dominar vertice i-1} = min{OPT(i-2) + V_i, OPT(i-1) + V_(i-1)} para i >=2.

from grafo import Grafo

def dominating_set_min_dinamico(vertices, n):
    mem = [0] * (n)

    mem[0] = vertices[0]
    mem[1] = min(vertices[1], vertices[0])

    for i in range(2, n):
        dominar = mem[i-2] + vertices[i]
        no_dominar = mem[i-1] + vertices[i-1]

        mem[i] = min(dominar, no_dominar)

    print(mem)
    return mem

def dominating_set_min_solucion(vertices, mem, n):
    solucion = []

    while (n >= 0):
        dominar = (mem[n-2] if n > 1 else 0) + vertices[n]
        no_dominar = (mem[n-1] if n > 0 else 0) + vertices[n-1]

        if dominar >= no_dominar:
            solucion.append(vertices[n])
            n -= 2
        
        else:
            n -= 1
    
    solucion.reverse()
    return solucion

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    n = len(vertices)

    mem = dominating_set_min_dinamico(vertices, n)
    return dominating_set_min_solucion(vertices, mem, n-1)

grafo1 = Grafo(False, [1,2,3,4,5,6])

grafo1.agregar_arista(1,2)
grafo1.agregar_arista(2,3)
grafo1.agregar_arista(3,4)
grafo1.agregar_arista(4,5)
grafo1.agregar_arista(5,6)

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['2', '5']\n")

"""assert juan_el_vago([100,20,30,70,50]) == [0,2,4]
assert juan_el_vago([100,20,30,70,20]) == [0,3]"""

