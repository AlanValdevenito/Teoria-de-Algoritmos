# Dado un Grafo dirigido, acíclico y pesado, y dos vértices s y t, implementar un algoritmo que, por programación
# dinámica, permita encontrar el camino de peso máximo.

# Indicar y justificar la complejidad del algoritmo implementado.

# Escribir y describir la ecuación de recurrencia de la solución, y la complejidad del algoritmo implementado. 

# Implementar el algoritmo de reconstrucción de la solución, indicando su complejidad.

# Ecuacion de recurrencia: OPT(i) = max{P(i,j) + OPT(j)} para todo vertice j que sea predecesor al vertice i

# Orden topologico: Un orden topologico es un ordenamiento parcial (no total) donde los elementos deben quedar ordenados por relaciones 
# de precedencia. Podemos pensarlo como tareas que deben realizarse antes que otras.

from grafo import Grafo
from collections import deque

def _dfs(grafo, v, destino, visitados, pila):
    visitados.add(v)

    if v == destino:
        pila.appendleft(v)
        return

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _dfs(grafo, w, destino, visitados, pila)

    pila.appendleft(v)

def orden_topologico(grafo, origen, destino):
    visitados = set()
    pila = deque()

    _dfs(grafo, origen, destino, visitados, pila)

    return [pila.popleft() for _ in range(0, len(pila))]

def camino_maximo_dinamico(grafo, vertices):
    mem = [0] * len(vertices)

    for i in range(0, len(vertices)):
        caminos = []

        for j in range(0, i):
            
            if grafo.estan_unidos(vertices[j], vertices[i]):
                peso = grafo.peso_arista(vertices[j], vertices[i])
                caminos.append(peso + mem[j])

        mem[i] = max(caminos) if len(caminos) > 0 else 0

    return mem

def camino_maximo_solucion(grafo, vertices, mem):
    
    i = max(range(len(mem)), key = lambda v: mem[v])
    solucion = [vertices[i]]

    while mem[i] > 0:

        for j in range(0, i):
            if (grafo.estan_unidos(vertices[j], vertices[i])) and (mem[j] == mem[i] - grafo.peso_arista(vertices[j], vertices[i])):
                solucion.append(vertices[j])
                i = j
                break

    solucion.reverse()
    return solucion

def camino_maximo(grafo, s, t):
    orden = orden_topologico(grafo, s, t)

    mem = camino_maximo_dinamico(grafo, orden)

    solucion = camino_maximo_solucion(grafo, orden, mem)

    return solucion

# Complejidad

# Orden topologico: Para construir el orden topologico se utiliza un recorrido DFS. ES decir, se iteran los vertices y sus adyacentes, con 
# lo cual tiene una complejidad de O(V+E).

# Construccion de la matriz de memorizacion: Se iteran los vertices y en cada iteracion los
# predecedores de cada vertice. En el peor caso, los predecedores serian todos los vertices
# con lo cual la complejidad resulta ser O(V²) donde V es la cantidad de vertices. 

# Re-construccion de la solucion: Encontrar el indice i con el camino mas largo tiene
# una complejidad de O(V) ya que recorremos toda la matriz de memorizacion buscando el
# maximo valor. Por otro lado, tenemos dos bucles anidados donde en el peor caso si
# el camino mas largo recorre todos los vertices la complejidad resulta ser O(V²).

# Luego, la complejidad total resulta ser O(V²).

grafo = Grafo(True, ["1", "2", "3", "4", "5", "6", "7"])

grafo.agregar_arista("1", "2", 100)
grafo.agregar_arista("1", "3", 1)

grafo.agregar_arista("2", "7", 100)

grafo.agregar_arista("3", "4", 1)
grafo.agregar_arista("3", "5", 1)

grafo.agregar_arista("4", "6", 1)
grafo.agregar_arista("5", "6", 1)

grafo.agregar_arista("6", "7", 1)

assert camino_maximo(grafo, "1", "7") == ["1", "2", "7"]

grafo = Grafo(True, ["1", "2", "3", "4", "5", "6", "7"])

grafo.agregar_arista("1", "2", 100)
grafo.agregar_arista("1", "3", 1)

grafo.agregar_arista("2", "7", 1)

grafo.agregar_arista("3", "4", 1)
grafo.agregar_arista("3", "5", 1)

grafo.agregar_arista("4", "6", 50)
grafo.agregar_arista("5", "6", 1)

grafo.agregar_arista("6", "7", 1)

assert camino_maximo(grafo, "3", "7") == ["3", "4", "6", "7"]