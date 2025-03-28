# Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 

# Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

from grafo import Grafo

def es_compatible(grafo, conjunto):

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):

            if v == w:
                continue

            # Validamos que al menos un vertice de la arista (v,w) se encuentre en el conjunto (Vertex Cover) ya que todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto
            if (not v in conjunto) and (not w in conjunto):
                return False

    return True

def _vertex_cover_min(grafo, vertices, actual, conjunto_parcial, conjunto_optimo):
    
    # print(f"\nConjunto parcial: {conjunto_parcial}")
    # print(f"Conjunto optimo: {conjunto_optimo}")

    if len(vertices) == actual:
        return set(conjunto_parcial) if len(conjunto_parcial) < len(conjunto_optimo) else set(conjunto_optimo)
    
    vertice = vertices[actual]
    conjunto_parcial.remove(vertice)

    # Poda: Validamos si al sacar un vertice el conjunto continua siendo Vertex Cover
    if es_compatible(grafo, conjunto_parcial):
        conjunto_optimo = _vertex_cover_min(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

    conjunto_parcial.add(vertice)
    return _vertex_cover_min(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

def vertex_cover_min(grafo):
    return _vertex_cover_min(grafo, grafo.obtener_vertices(), 0, set(grafo.obtener_vertices()), set(grafo.obtener_vertices()))

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