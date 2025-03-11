# Implementar un algoritmo que, por backtracking, obtenga la cantidad total de posibles ordenamientos topológicos de un grafo dirigido y 
# acíclico.

from grafo import Grafo

def _contar_ordenamientos(grafo, vertices, visitados, grado_entrada, ordenamientos_posibles, ordenamiento_parcial):

    if len(ordenamiento_parcial) == len(vertices):
        ordenamientos_posibles.append(ordenamiento_parcial.copy())
        return
    
    for v in vertices:
        if (v not in visitados) and (grado_entrada[v] == 0):

            visitados.add(v)
            ordenamiento_parcial.append(v)
            
            for w in grafo.adyacentes(v):
                grado_entrada[w] -= 1
            
            _contar_ordenamientos(grafo, vertices, visitados, grado_entrada, ordenamientos_posibles, ordenamiento_parcial)
            
            visitados.remove(v)
            ordenamiento_parcial.pop()

            for w in grafo.adyacentes(v):
                grado_entrada[w] += 1

def contar_ordenamientos(grafo):
    visitados = set()
    
    grado_entrada = {v: 0 for v in grafo.obtener_vertices()}

    ordenamientos_posibles = []
   
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grado_entrada[w] += 1
   
    _contar_ordenamientos(grafo, grafo.obtener_vertices(), visitados, grado_entrada, ordenamientos_posibles, [])
    
    return len(ordenamientos_posibles)

grafo = Grafo(True, [1,2,3,4,5])
grafo.agregar_arista(1,2)
grafo.agregar_arista(2,3)
grafo.agregar_arista(2,4)
grafo.agregar_arista(3,5)

assert contar_ordenamientos(grafo) == 3