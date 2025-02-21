# Implementar un algoritmo que reciba un grafo no dirigido y un número k, y devuelva un ciclo de tamaño exactamente k
# del grafo, si es que existe.

from grafo import Grafo

def es_compatible(grafo, ciclo):

    for i in range(1, len(ciclo)):

        v = ciclo[i-1]
        w = ciclo[i]

        if not grafo.estan_unidos(v, w):
            return False

    primero = ciclo[0]
    ultimo = ciclo[-1]

    if not grafo.estan_unidos(ultimo, primero):
        return False

    return True

def _k_ciclo(grafo, k, vertices, actual, ciclo):
    
    if len(ciclo) == k:
        return es_compatible(grafo, ciclo)
    
    if actual >= len(grafo.obtener_vertices()):
        return False
    
    # Poda: Si ya no llegamos a los K vertices, entonces no existe un ciclo de exactamente K vertices
    if len(ciclo) + (len(vertices) - actual) < k:
        return False

    vertice = vertices[actual]

    # Poda: Si el vertice actual no tiene grado de entrada 2 o mayor no puede estar en un ciclo
    if len(grafo.adyacentes(vertice)) < 2:
        return _k_ciclo(grafo, k, vertices, actual + 1, ciclo)

    ciclo.append(vertice)

    if _k_ciclo(grafo, k, vertices, actual + 1, ciclo):
        return True

    ciclo.pop()
    return _k_ciclo(grafo, k, vertices, actual + 1, ciclo)

def k_ciclo(grafo, k):

    if len(grafo.obtener_vertices()) < k:
        return []

    ciclo = []

    # Poda: Ordenamos los vertices segun su grado de forma descendente para comenzar primero con los vertices que tengan mayor grado
    vertices = sorted(grafo.obtener_vertices(), key=lambda x: len(grafo.adyacentes(x)), reverse=True)

    if not _k_ciclo(grafo, k, vertices, 0, ciclo):
        return []

    return ciclo

grafo = Grafo(False, ["A", "B", "C", "D", "E"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("C", "A")
grafo.agregar_arista("C", "D")
grafo.agregar_arista("D", "E")
grafo.agregar_arista("E", "A")

assert k_ciclo(grafo, 3) == ['A', 'C', 'B']

grafo = Grafo(False, ["A", "B", "C", "D", "E"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("C", "D")
grafo.agregar_arista("D", "E")

assert k_ciclo(grafo, 4) == []

grafo = Grafo(False, ["A", "B", "C", "D", "E"])

grafo.agregar_arista("A", "B")
grafo.agregar_arista("B", "C")
grafo.agregar_arista("C", "D")
grafo.agregar_arista("D", "E")
grafo.agregar_arista("E", "A")

assert k_ciclo(grafo, 5) == ["A", "B", "C", "D", "E"]