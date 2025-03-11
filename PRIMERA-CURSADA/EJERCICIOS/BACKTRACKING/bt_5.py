# Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez. 

# Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.

from grafo import Grafo

def _camino_hamiltoniano(grafo, vertice, visitados, camino):
    visitados.add(vertice)
    camino.append(vertice)

    if len(visitados) == len(grafo.obtener_vertices()):
        return True

    for w in grafo.adyacentes(vertice):
        if w not in visitados:
            if _camino_hamiltoniano(grafo, w, visitados, camino):
                return True
            
    visitados.remove(vertice)
    camino.pop()
    return False

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()

    for v in grafo.obtener_vertices():
        if _camino_hamiltoniano(grafo, v, visitados, camino):
            return camino
        
    return None
    
grafo = Grafo(False, [0,1,2,3,4,5,6,7])

grafo.agregar_arista(0,1)
grafo.agregar_arista(1,2)
grafo.agregar_arista(1,5)
grafo.agregar_arista(2,3)
grafo.agregar_arista(3,4)
grafo.agregar_arista(5,3)
grafo.agregar_arista(5,4)
grafo.agregar_arista(5,6)
grafo.agregar_arista(6,7)
grafo.agregar_arista(7,4)

assert camino_hamiltoniano(grafo) == [0, 1, 2, 3, 4, 5, 6, 7]