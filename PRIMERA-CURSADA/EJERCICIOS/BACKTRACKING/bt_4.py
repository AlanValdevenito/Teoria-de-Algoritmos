# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un máximo Independent Set 
# del mismo.

# Maximum Independent Set: Conjunto maximo de vertices tal que no hay dos vértices en el conjunto que sean adyacentes entre sí.

from grafo import Grafo

def es_compatible(grafo, puestos):

    for v in puestos:
        for w in puestos:

            if v == w:
                continue

            if grafo.estan_unidos(v, w):
                return False
            
    return True

def _independent_set(grafo, vertices, puestos_parcial, puestos_optimo, actual):
    
    print(f"Conjunto parcial: {puestos_parcial} - Conjunto optimo: {puestos_optimo}")

    if (len(vertices) == actual):
        return set(puestos_parcial) if (len(puestos_parcial) > len(puestos_optimo)) else set(puestos_optimo)
    
    vertice_actual = vertices[actual]
    
    puestos_parcial.add(vertice_actual)
    if es_compatible(grafo, puestos_parcial):
        puestos_optimo = _independent_set(grafo, vertices, puestos_parcial, puestos_optimo, actual + 1)
    
    puestos_parcial.remove(vertice_actual)
    return _independent_set(grafo, vertices, puestos_parcial, puestos_optimo, actual + 1)

def independent_set(grafo):
    return _independent_set(grafo, grafo.obtener_vertices(), set(), set(), 0)

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