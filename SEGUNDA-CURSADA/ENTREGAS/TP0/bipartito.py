# Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. 
# Es decir, la función es_bipartito debe devolver True si el grafo recibido por parámetro es efectivamente 
# bipartito, False en caso contrario. Que un grafo sea Bipartito implica que puede separarse los vértices en dos 
# grupos S y T, tal que para cada par de vértices de S no exista arista entre sí (lo mismo para T), que la 
# intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

# El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de 
# diccionarios), a considerar para la complejidad.

from grafo import Grafo
from queue import Queue

ROJO = 0
AZUL = 1

def _es_bipartito(grafo, origen, visitados, coloreados):
    cola = Queue()
    cola.put(origen) # O(1)

    visitados.add(origen) # O(1)

    coloreados[origen] = ROJO # O(1)

    while not cola.empty():
        v = cola.get()

        for w in grafo.adyacentes(v):

            if (w in visitados) and (coloreados[v] == coloreados[w]): # O(1)
                return False

            if w not in visitados: # O(1)
                coloreados[w] = ROJO if (coloreados[v] == AZUL) else AZUL # O(1)
                visitados.add(w) # O(1)
                cola.put(w) # O(1)
                
    return True

def es_bipartito(grafo):
    visitados = set()
    coloreados = {}
    
    for v in grafo.obtener_vertices(): # O(V)
        if v not in visitados:
            if not _es_bipartito(grafo, v, visitados, coloreados): # O(V+E)
                return False
    
    return True

# Complejidad

# El algoritmo utiliza un recorrido BFS con lo cual recorremos todos los vertices y para cada vertice recorremos sus adyacentes, por
# lo tanto la complejidad resulta ser O(V+E) con V la cantidad de vertices y E la cantidad de aristas.

grafo = Grafo(False, ["A","B","C","D","E","F","G","H","I","J","K","L"])

grafo.agregar_arista("A","F")
grafo.agregar_arista("B","F")
grafo.agregar_arista("B","G")
grafo.agregar_arista("C","H")
grafo.agregar_arista("C","I")
grafo.agregar_arista("D","G")
grafo.agregar_arista("E","F")
grafo.agregar_arista("E","I")

grafo.agregar_arista("J","K")
grafo.agregar_arista("K","L")
grafo.agregar_arista("L","J")

assert es_bipartito(grafo) == False

grafo = Grafo(False, ["A","B","C","D","E","F","G","H","I"])

grafo.agregar_arista("A","F")
grafo.agregar_arista("B","F")
grafo.agregar_arista("B","G")
grafo.agregar_arista("C","H")
grafo.agregar_arista("C","I")
grafo.agregar_arista("D","G")
grafo.agregar_arista("E","F")
grafo.agregar_arista("E","I")

assert es_bipartito(grafo) == True

grafo = Grafo(False, ["J","K","L"])

grafo.agregar_arista("J","K")
grafo.agregar_arista("K","L")
grafo.agregar_arista("L","J")

assert es_bipartito(grafo) == False