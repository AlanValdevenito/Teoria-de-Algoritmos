# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set del mismo.

from grafo import Grafo

def insuficientes_vertices(vertices, actual, conjunto_parcial, conjunto_optimo):
    vertices_restantes = len(vertices) - actual
    return vertices_restantes + len(conjunto_parcial) < len(conjunto_optimo)

def es_compatible(grafo, conjunto, w):

    for v in conjunto:
        if (v == w):
            continue

        if grafo.estan_unidos(v, w):
            return False
    
    return True

def _independent_set(grafo, vertices, actual, conjunto_parcial, conjunto_optimo):
    
    if len(vertices) == actual:
        return set(conjunto_parcial) if len(conjunto_parcial) > len(conjunto_optimo) else set(conjunto_optimo)
    
    # Poda: Validar si el tamaño del conjunto parcial sumado al numero de vertices restantes es menor al conjunto optimo
    if insuficientes_vertices(vertices, actual, conjunto_parcial, conjunto_optimo):
        return set(conjunto_optimo)

    vertice = vertices[actual]
    conjunto_parcial.add(vertice)

    # Poda: Validamos si al agregar un vertice el conjunto continua siendo Independent Set
    # Poda: Validamos unicamente para el ultimo vertice agregado
    if es_compatible(grafo, conjunto_parcial, vertice):
        conjunto_optimo = _independent_set(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)
    
    conjunto_parcial.remove(vertice)
    return _independent_set(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

def independent_set(grafo):
    # Poda: Ordenamos los vertices por menor grado para priorizar los que tienen menos adyacentes y maximizar la cantidad de vertices en el conjunto
    vertices = sorted(grafo.obtener_vertices(), key=lambda v: len(grafo.adyacentes(v)))
    
    return _independent_set(grafo, vertices, 0, set(), set())

grafo = Grafo(False, ["0","1","2","3","4","5","6","7"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("1","2")
grafo.agregar_arista("1","5")
grafo.agregar_arista("2","3")
grafo.agregar_arista("5","3")
grafo.agregar_arista("6","5")
grafo.agregar_arista("6","7")
grafo.agregar_arista("7","4")
grafo.agregar_arista("5","4")
grafo.agregar_arista("3","4")

assert independent_set(grafo) == {"0","2","4","6"}

grafo = Grafo(False, ["0","1","2","3"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("0","3")
grafo.agregar_arista("0","2")
grafo.agregar_arista("2","3")

assert independent_set(grafo) == {"2","1"}