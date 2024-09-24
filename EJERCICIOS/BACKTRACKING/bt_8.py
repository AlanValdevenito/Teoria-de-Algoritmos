# Implementar un algoritmo de backtracking que, dados dos grafos, determine si existe un Isomorfismo entre ambos.

from grafo import Grafo

def es_compatible(g1, g2, mapeo):
    
    for v_g2 in g2.obtener_vertices():
        for w_g2 in g2.adyacentes(v_g2):

            if mapeo[w_g2] not in g1.adyacentes(mapeo[v_g2]):
                return False

    return True

def _hay_isomorfismo(g1, g2, vertices_g2, mapeo, visitados):

    print(f"Mapeo: {mapeo}\n")

    if len(mapeo) == len(g2.obtener_vertices()):
        return es_compatible(g1, g2, mapeo)

    actual = vertices_g2[len(mapeo)]

    for v in g1.obtener_vertices():

        if v not in visitados:
            mapeo[actual] = v
            visitados.add(v)

            if _hay_isomorfismo(g1, g2, g2.obtener_vertices(), mapeo, visitados):
                return True
            
            del mapeo[actual]
            visitados.remove(v)

    return False

def hay_isomorfismo(g1, g2):

    if not (len(g1.obtener_vertices()) == len(g2.obtener_vertices())):
        return False
    
    mapeo = {}
    visitados = set()
    
    return _hay_isomorfismo(g1, g2, g2.obtener_vertices(), mapeo, visitados)

grafo1 = Grafo(False, ["A", "B", "C", "D", "G", "H", "I", "J"])
grafo1.agregar_arista("A", "G")
grafo1.agregar_arista("A", "H")
grafo1.agregar_arista("A", "I")
grafo1.agregar_arista("G", "B")
grafo1.agregar_arista("G", "C")
grafo1.agregar_arista("B", "H")
grafo1.agregar_arista("B", "J")
grafo1.agregar_arista("H", "D")
grafo1.agregar_arista("C", "I")
grafo1.agregar_arista("C", "J")
grafo1.agregar_arista("I", "D")
grafo1.agregar_arista("J", "D")

grafo2 = Grafo(False, [1, 2, 3, 4, 5, 6, 7, 8])
grafo2.agregar_arista(1,2)
grafo2.agregar_arista(1,4)
grafo2.agregar_arista(4,3)
grafo2.agregar_arista(2,3)
grafo2.agregar_arista(1,5)
grafo2.agregar_arista(4,8)
grafo2.agregar_arista(3,7)
grafo2.agregar_arista(2,6)
grafo2.agregar_arista(5,6)
grafo2.agregar_arista(5,8)
grafo2.agregar_arista(8,7)
grafo2.agregar_arista(6,7)

assert hay_isomorfismo(grafo1, grafo2) == True