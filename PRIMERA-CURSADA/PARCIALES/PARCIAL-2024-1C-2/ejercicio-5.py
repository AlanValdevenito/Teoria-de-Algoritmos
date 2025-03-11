# Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo.

# Clique: Subgrafo en el que cada vértice está conectado a todos los demás vértices del subgrafo.

from grafo import Grafo

def es_clique(grafo, clique):

    for v in clique:
        for w in clique:

            if v == w:
                continue

            if not grafo.estan_unidos(v,w):
                return False
    
    return True

def clique_bt(grafo, vertices, clique_actual, clique_optimo, actual = 0):
    
    # print(f"Conjunto parcial: {clique_actual}")
    # print(f"Conjunto optimo: {clique_optimo}\n")

    if actual == len(vertices):
        return set(clique_actual) if len(clique_actual) > len(clique_optimo) else set(clique_optimo)

    vertice_actual = vertices[actual]

    clique_actual.add(vertice_actual)
    if es_clique(grafo, clique_actual):
        clique_optimo = clique_bt(grafo, vertices, clique_actual, clique_optimo, actual + 1)

    clique_actual.remove(vertice_actual)
    return clique_bt(grafo, vertices, clique_actual, clique_optimo, actual + 1)

def clique(grafo):
    return clique_bt(grafo, grafo.obtener_vertices(), set(), set())

grafo = Grafo(False, ["0","1","2","3","4"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("0","2")
grafo.agregar_arista("1","2")
grafo.agregar_arista("1","3")
grafo.agregar_arista("2","3")
grafo.agregar_arista("3","4")

assert clique(grafo) == {"0","1","2"}

grafo = Grafo(False, ["A", "B", "C"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "C")

assert clique(grafo) == {"A","B","C"}

grafo = Grafo(False, ["A", "B", "C", "D", "E"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("A", "D")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "D")

grafo.agregar_arista("D", "E")

assert clique(grafo) == {"A","B","C","D"}

grafo = Grafo(False, ["A", "B", "C", "D"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("C", "D")

assert clique(grafo) == {"A","B"}