# Implementar un algoritmo que dado un grafo, obtenga el clique de mayor tamaño del mismo.

from grafo import Grafo

def es_compatible(grafo, conjunto, w):

    for v in conjunto:

        if not grafo.estan_unidos(v,w):
            return False

    return True

def insuficientes_vertices(vertices, actual, conjunto_parcial, conjunto_optimo):
    vertices_restantes = len(vertices) - actual
    return len(conjunto_parcial) + vertices_restantes < len(conjunto_optimo)

def insuficientes_adyacentes(grafo, v, conjunto_optimo):
    return len(grafo.adyacentes(v)) < len(conjunto_optimo)

def _clique(grafo, vertices, actual, conjunto_parcial, conjunto_optimo):

    if actual >= len(vertices):
        return set(conjunto_parcial) if len(conjunto_parcial) > len(conjunto_optimo) else set(conjunto_optimo)
    
    # Poda: Validar si el tamaño del conjunto parcial sumado al numero de vertices restantes es menor al conjunto optimo
    if insuficientes_vertices(vertices, actual, conjunto_parcial, conjunto_optimo):
        return set(conjunto_optimo)

    # Poda: El conjunto parcial supera al optimo
    if len(conjunto_parcial) > len(conjunto_optimo):
        conjunto_optimo = set(conjunto_parcial)

    vertice = vertices[actual]

    # Poda: Consideramos vertices que si o si tengan al menos mas adyacentes que el tamaño del conjunto optimo
    if insuficientes_adyacentes(grafo, vertice, conjunto_optimo):
        return conjunto_optimo

    # Poda: Validamos si al agregar un vertice el conjunto continua siendo Clique
    # Poda: Validamos unicamente para el ultimo vertice agregado
    if es_compatible(grafo, conjunto_parcial, vertice):
        conjunto_parcial.add(vertice)
        conjunto_optimo = _clique(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)
        conjunto_parcial.remove(vertice)

    return _clique(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

def clique(grafo):
    return _clique(grafo, grafo.obtener_vertices(), 0, set(), set())

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