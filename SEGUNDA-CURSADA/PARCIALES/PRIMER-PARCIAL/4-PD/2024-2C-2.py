# Dado un Grafo dirigido, acíclico y pesado, y dos vértices s y t, implementar un algoritmo que, por programación
# dinámica, permita encontrar el camino de peso máximo. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Escribir y describir la ecuación de recurrencia de la solución, y la complejidad del algoritmo implementado.

# Implementar el algoritmo de reconstrucción de la solución, indicando su complejidad.

# ¿Que tipo de problema es?. Es un problema de maximizacion ya que nos piden encontrar el camino de peso maximo.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de vertices.

# Ejemplo: Consideremos el listado ordenado (orden topologico) de vertices [1, 3, 5, 4, 6, 2, 7]

# OPT[0] = 0
# OPT[1] = OPT[0] + peso(1,3) = 0 + 1 = 1
# OPT[2] = OPT[1] + peso(3,5) = 1 + 1 = 2
# OPT[3] = OPT[1] + peso(3,4) = 1 + 1 = 2
# OPT[4] = max(OPT[3] + peso(4,6), OPT[2] + peso(5,6)) = max(2 + 1, 2 + 1) = max(3, 3) = 3
# OPT[5] = OPT[0] + peso(1,2) = 0 + 100 = 100
# OPT[6] = max(OPT[4] + peso(6,7), OPT[5] + peso(2,7)) = max(4 + 1, 100 + 100) = max(5, 200) = 200

# Ecuacion de recurrencia: OPT[i] = max(OPT[j] + peso(j, i)) para todo vertice j que sea predecesor del vertice i

from grafo import Grafo
from collections import deque

def dfs(grafo, v, destino, visitados, pila):
    visitados.add(v)

    if v == destino:
        pila.appendleft(v)
        return

    for w in grafo.adyacentes(v):
        if w not in visitados:
            dfs(grafo, w, destino, visitados, pila)

    pila.appendleft(v)

def orden_topologico(grafo, origen, destino):
    visitados = set()
    pila = deque()

    dfs(grafo, origen, destino, visitados, pila)

    return [pila.popleft() for _ in range(0, len(pila))]

def camino_maximo_dinamico(grafo, vertices, n):
    mem = [0] * (n)

    for i in range(0, n):
        v = vertices[i]
        caminos = []

        for j in range(0, i):
            w = vertices[j]

            if grafo.estan_unidos(w, v):
                caminos.append(mem[j] + grafo.peso_arista(w, v))

        mem[i] = max(caminos) if len(caminos) > 0 else 0

    return mem

def camino_maximo_solucion(grafo, vertices, mem):
    solucion = []

    i = len(vertices) - 1

    while i > 0:
        v = vertices[i]
        solucion.append(v)

        for j in range(0, i):
            w = vertices[j]

            if grafo.estan_unidos(w, v):
                
                if mem[j] + grafo.peso_arista(w, v) == mem[i]:
                    i = j

    solucion.append(vertices[i])

    solucion.reverse()
    return solucion

def camino_maximo(grafo, s, t):
    vertices = orden_topologico(grafo, s, t)
    n = len(vertices)

    mem = camino_maximo_dinamico(grafo, vertices, n)
    return camino_maximo_solucion(grafo, vertices, mem)

# Complejidad

# Orden topologico: Para obtener un orden topologico utilizamos un DFS lo cual tiene una complejidad de O(V+E) con V la cantidad de vertices y E la cantidad 
# de adyacentes.

# Matriz de memorizacion: Para construir la matriz de memorizacion recorremos todos los vertices y para cada vertice recorremos sus predecesores lo cual
# en el peor caso (un vertice tiene como predecesores a todos los otros vertices) tiene una complejidad de O(V^2) con V la cantidad de vertices.

# Reconstruccion de solucion: Para reconstruir la solucion recorremos todos los vertices y para cada vertice recorremos sus predecesores lo cual
# en el peor caso (un vertice tiene como predecesores a todos los otros vertices) tiene una complejidad de O(V^2) con V la cantidad de vertices.

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

grafo = Grafo(True, ["1", "2", "3", "4", "5", "6", "7"])

grafo.agregar_arista("1", "2", 100)
grafo.agregar_arista("1", "3", 1)

grafo.agregar_arista("2", "7", 1)

grafo.agregar_arista("3", "4", 1)
grafo.agregar_arista("3", "5", 1)

grafo.agregar_arista("4", "6", 50)
grafo.agregar_arista("5", "6", 1)

grafo.agregar_arista("6", "7", 1)

assert camino_maximo(grafo, "3", "6") == ["3", "4", "6"]