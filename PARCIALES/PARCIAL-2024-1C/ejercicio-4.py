# Implementar un algoritmo que (por backtracking) dado un grafo no dirigido en el que sus vértices tienen valores positivos, permita obtener 
# el Dominating Set de suma mínima. Es decir, aquel dominating set en el cual la suma de todos los valores de los vértices sea 
# mínima (no es importante que la cantidad de vértices del set sea mínima). Por simplicidad, considerar que el grafo es conexo.

from grafo import Grafo

def es_dominating_set(grafo, d):
    
    for v in grafo.obtener_vertices():

        if v in d:
            continue

        tiene_adyacente_a_un_vertice_en_d = False
        for w in grafo.adyacentes(v):
            if w in d:
                tiene_adyacente_a_un_vertice_en_d = True
                break
        
        if not tiene_adyacente_a_un_vertice_en_d:
            return False

    return True

def _dominating_set_min(grafo, vertices, conjunto_parcial, conjunto, actual):
    
    if (actual >= len(vertices)):
        return set(conjunto_parcial) if (sum(conjunto_parcial) < sum(conjunto)) else set(conjunto)
    
    vertice_actual = vertices[actual]

    conjunto_parcial.remove(vertice_actual)
    if es_dominating_set(grafo, conjunto_parcial):
        conjunto = _dominating_set_min(grafo, vertices, conjunto_parcial, conjunto, actual + 1)

    conjunto_parcial.add(vertice_actual)
    return _dominating_set_min(grafo, vertices, conjunto_parcial, conjunto, actual + 1)

def dominating_set_min(grafo):
    return _dominating_set_min(grafo, grafo.obtener_vertices(), set(grafo.obtener_vertices()), set(grafo.obtener_vertices()), 0)

grafo1 = Grafo(False, [1,2,3,4,5,6])

grafo1.agregar_arista(1,2)
grafo1.agregar_arista(1,3)
grafo1.agregar_arista(2,3)
grafo1.agregar_arista(2,4)
grafo1.agregar_arista(3,5)
grafo1.agregar_arista(4,5)
grafo1.agregar_arista(4,6)

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['1', '4']\n")

grafo1 = Grafo(False, [1,2,3,4,5,6])

grafo1.agregar_arista(1,2)
grafo1.agregar_arista(2,3)
grafo1.agregar_arista(3,4)
grafo1.agregar_arista(4,5)
grafo1.agregar_arista(5,6)

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['2', '5']\n")