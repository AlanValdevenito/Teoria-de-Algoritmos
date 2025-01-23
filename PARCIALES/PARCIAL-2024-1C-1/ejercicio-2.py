# Implementar un algoritmo greedy que permita obtener el mínimo del problema del viajante: dado un Grafo pesado G y
# un vértice de inicio v, obtener el camino de menor costo que lleve a un viajante desde v hacia cada uno de los vértices
# del grafo, pasando por cada uno de ellos una única vez, y volviendo nuevamente al origen. Se puede asumir que el grafo
# es completo. 

# Indicar y justificar la complejidad del algoritmo implementado.

# ¿El algoritmo obtiene siempre la solución óptima? Si es así, justificar detalladamente, sino dar un contraejemplo. Indicar
# y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

from grafo import Grafo

def obtener_camino(grafo, v, visitados, camino):

    if (len(visitados) == len(grafo.obtener_vertices())):
        return camino

    visitados.add(v)
    camino.append(v)

    w_min = None
    peso = float("inf")

    for w in grafo.adyacentes(v):

        if (w not in visitados) and (grafo.peso_arista(v, w) < peso):
            w_min = w
            peso = grafo.peso_arista(v, w)

    return obtener_camino(grafo, w_min, visitados, camino)

def min_tsp(grafo, inicio):
    visitados = set()

    camino = obtener_camino(grafo, inicio, visitados, [])
    camino.append(inicio)

    return camino

# Complejidad

# Recorremos todos los vertices exactamente una vez
# Para cada vertice, recorremos todos sus adyacentes ya que es necesario buscar la arista de menor peso
# El problema tiene la particularidad de que el grafo es completo, con lo cual cada vertice tiene V-1 adyacentes

# Luego, la complejidad resulta ser O(V²) con V la cantidad de vertices

# Algoritmo Greedy

# ¿Por qué se trata de un algoritmo Greedy?. El algoritmo tiene como regla sencilla elegir como vertice siguiente aquel que
# tenga el menor peso en su arista y que aun no haya sido visitado. Se aplica iterativamente esta regla esperando obtener
# el camino de menor costo que lleve a un viajante desde un vertice origen hacia cada uno de los vértices del grafo, pasando por cada uno 
# de ellos una única vez, y volviendo nuevamente al origen.

# ¿El algoritmo es optimo?. No es optimo. Un contraejemplo seria un grafo tal que sea necesario elegir como vertice siguiente aquel
# que no tenga el menor peso en su arista, pero que mas adelante permita minimizar el costo total del camino. Es decir, un grafo donde 
# el camino optimo requiera elegir una arista mas costosa inicialmente para obtener un menor costo total.

# Por ejemplo, si tenemos en cuenta el ejemplo 4 nuestro algoritmo da como resultado el camino [0, 1, 2, 3, 0] pero el optimo 
# seria [0, 1, 3, 2, 0].

grafo = Grafo(False, [0, 1, 2, 3])

grafo.agregar_arista(0, 1, 10)
grafo.agregar_arista(0, 2, 15)
grafo.agregar_arista(0, 3, 20)
grafo.agregar_arista(1, 2, 35)
grafo.agregar_arista(1, 3, 25)
grafo.agregar_arista(2, 3, 30)

assert min_tsp(grafo, 0) == [0, 1, 3, 2, 0]

grafo = Grafo(False, [0, 1, 2, 3, 4])

grafo.agregar_arista(0, 1, 10)
grafo.agregar_arista(0, 2, 20)
grafo.agregar_arista(0, 3, 30)
grafo.agregar_arista(0, 4, 40)
grafo.agregar_arista(1, 2, 15)
grafo.agregar_arista(1, 3, 35)
grafo.agregar_arista(1, 4, 25)
grafo.agregar_arista(2, 3, 10)
grafo.agregar_arista(2, 4, 20)
grafo.agregar_arista(3, 4, 5)

assert min_tsp(grafo, 0) == [0, 1, 2, 3, 4, 0]

grafo = Grafo(False, [0, 1, 2, 3, 4, 5])

grafo.agregar_arista(0, 1, 5)
grafo.agregar_arista(0, 2, 10)
grafo.agregar_arista(0, 3, 15)
grafo.agregar_arista(0, 4, 20)
grafo.agregar_arista(0, 5, 25)
grafo.agregar_arista(1, 2, 9)
grafo.agregar_arista(1, 3, 10)
grafo.agregar_arista(1, 4, 11)
grafo.agregar_arista(1, 5, 12)
grafo.agregar_arista(2, 3, 8)
grafo.agregar_arista(2, 4, 7)
grafo.agregar_arista(2, 5, 6)
grafo.agregar_arista(3, 4, 5)
grafo.agregar_arista(3, 5, 4)
grafo.agregar_arista(4, 5, 3)

assert min_tsp(grafo, 0) == [0, 1, 2, 5, 4, 3, 0]

grafo = Grafo(False, [0, 1, 2, 3])

grafo.agregar_arista(0, 1, 1)
grafo.agregar_arista(0, 2, 50)
grafo.agregar_arista(0, 3, 100)
grafo.agregar_arista(1, 2, 1)
grafo.agregar_arista(1, 3, 5)
grafo.agregar_arista(2, 3, 1)

assert min_tsp(grafo, 0) == [0, 1, 2, 3, 0]