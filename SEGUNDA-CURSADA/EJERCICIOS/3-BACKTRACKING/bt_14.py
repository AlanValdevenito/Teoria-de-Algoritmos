# Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G:
# (i) pertenece a D
# (ii) es adyacente a un vértice en D.

# Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

from grafo import Grafo

def es_compatible(grafo, conjunto):

    # Validamos que para todo vertice de G...
    for v in grafo.obtener_vertices():

        # ... pertecenece al conjunto D...
        if (v in conjunto):
            continue

        es_adyacente = False
        for w in conjunto:

            # ... o es adyacente a un vertice en D
            if (grafo.estan_unidos(v, w)):
                es_adyacente = True
                break

        if not es_adyacente:
            return False
 
    return True

def _dominating_set_min(grafo, vertices, actual, conjunto_parcial, conjunto_optimo):
    
    # print(f"\nConjunto parcial: {conjunto_parcial}")
    # print(f"Conjunto optimo: {conjunto_optimo}")

    if actual == len(vertices):
        return set(conjunto_parcial) if len(conjunto_parcial) < len(conjunto_optimo) else set(conjunto_optimo)

    vertice = vertices[actual]
    conjunto_parcial.remove(vertice)

    # Poda: Validamos si al sacar un vertice el conjunto continua siendo Dominating Set
    if es_compatible(grafo, conjunto_parcial):
        conjunto_optimo = _dominating_set_min(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

    conjunto_parcial.add(vertice)
    return _dominating_set_min(grafo, vertices, actual + 1, conjunto_parcial, conjunto_optimo)

def dominating_set_min(grafo):
    return _dominating_set_min(grafo, grafo.obtener_vertices(), 0, set(grafo.obtener_vertices()), set(grafo.obtener_vertices()))

grafo = Grafo(False, ["1","2","3","4","5","6"])

grafo.agregar_arista("1","2")
grafo.agregar_arista("1","3")
grafo.agregar_arista("2","3")
grafo.agregar_arista("2","4")
grafo.agregar_arista("3","5")
grafo.agregar_arista("4","5")
grafo.agregar_arista("4","6")
assert dominating_set_min(grafo) in [{'1', '4'}, {'3', '4'}, {'2', '4'}, {'3', '6'}]