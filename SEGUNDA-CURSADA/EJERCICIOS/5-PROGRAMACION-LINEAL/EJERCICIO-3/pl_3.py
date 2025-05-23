# Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 

# Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

# Implementar un modelo de programación lineal que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

import pulp

from grafo import Grafo

def vertex_cover_min(grafo):
    y = {v: pulp.LpVariable(f"y_{v}", cat="Binary") for v in grafo.obtener_vertices()}

    problem = pulp.LpProblem("VC", pulp.LpMinimize)
    
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v < w:
                problem += y[v] + y[w] >= 1

    problem += pulp.lpSum(y[v] for v in grafo.obtener_vertices())

    problem.solve()
    return {v for v in grafo.obtener_vertices() if y[v].varValue == 1}

grafo = Grafo(False, ["A","B","C","D","E"])
grafo.agregar_arista("A","B")
grafo.agregar_arista("A","C")
grafo.agregar_arista("B","C")
grafo.agregar_arista("B","D")
grafo.agregar_arista("C","D")
grafo.agregar_arista("D","E")
assert vertex_cover_min(grafo) in [{'A', 'B', 'D'},  {'A', 'C', 'D'}, {'B', 'C', 'E'}]

grafo = Grafo(False, ["A","B","C","D","E"])
grafo.agregar_arista("A","C")
grafo.agregar_arista("C","E")
grafo.agregar_arista("E","B")
grafo.agregar_arista("E","D")
assert vertex_cover_min(grafo) in [{'E', 'C'}, {'E', 'A'}]

grafo = Grafo(False, ["A","B","C","D"])
grafo.agregar_arista("A","D")
grafo.agregar_arista("B","D")
grafo.agregar_arista("C","D")
assert vertex_cover_min(grafo) == {'D'}

grafo = Grafo(False, ["A","B","C","D"])
grafo.agregar_arista("D","A")
grafo.agregar_arista("B","A")
grafo.agregar_arista("C","A")
assert vertex_cover_min(grafo) == {'A'}

grafo = Grafo(False, ["A","B"])
assert vertex_cover_min(grafo) == set()

grafo = Grafo(False, ["0","1","2","3","4","5","6","7"])
grafo.agregar_arista("0","1")
grafo.agregar_arista("1","2")
grafo.agregar_arista("1","5")
grafo.agregar_arista("2","3")
grafo.agregar_arista("3","4")
grafo.agregar_arista("5","6")
grafo.agregar_arista("6","7")
grafo.agregar_arista("7","4")
grafo.agregar_arista("5","4")
grafo.agregar_arista("5","3")
assert vertex_cover_min(grafo) in [{'1', '3', '4', '6'}, {'1', '3', '5', '7'}]