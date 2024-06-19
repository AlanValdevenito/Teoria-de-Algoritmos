from grafo import Grafo
from collections import deque

def copiar(grafo):
    nuevo_grafo = Grafo(grafo.dirigido)
    for u in grafo.obtener_vertices():
        for v in grafo.adyacentes(u):
            nuevo_grafo.agregar_arista(u, v, grafo.peso_arista(u, v))
    return nuevo_grafo

def obtener_camino(grafo_residual, s, t):
    padre = {s: None}
    cola = deque([s])

    while cola:
        u = cola.popleft()
        for v in grafo_residual.adyacentes(u):
            if v not in padre and grafo_residual.peso_arista(u, v) > 0:
                padre[v] = u
                if v == t:
                    camino = []
                    while v is not None:
                        camino.append(v)
                        v = padre[v]
                    return camino[::-1]
                cola.append(v)
    return None

def min_peso(grafo_residual, camino):
    return min(grafo_residual.peso_arista(camino[i], camino[i+1]) for i in range(len(camino)-1))

def actualizar_grafo_residual(grafo_residual, u, v, valor):
    peso_anterior = grafo_residual.peso_arista(u, v)
    if peso_anterior == valor:
        grafo_residual.borrar_arista(u, v)
    else:
        grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
    if not grafo_residual.estan_unidos(v, u):
        grafo_residual.agregar_arista(v, u, valor)
    else:
        grafo_residual.cambiar_peso(v, u, grafo_residual.peso_arista(v, u) + valor)

def flujo(grafo, s, t):
    flujo = {}
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0
    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)
    while camino is not None:
        capacidad_residual_camino = min_peso(grafo_residual, camino)
        for i in range(1, len(camino)):
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
            else:
                flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
        camino = obtener_camino(grafo_residual, s, t)

    return flujo

# Ejemplo 1
grafo1 = Grafo(True, [0, 1, 2, 3, 4, 5])

grafo1.agregar_arista(0, 1, 11)
grafo1.agregar_arista(0, 2, 12)
grafo1.agregar_arista(1, 3, 12)
grafo1.agregar_arista(2, 1, 2)
grafo1.agregar_arista(2, 4, 11)
grafo1.agregar_arista(4, 3, 10)
grafo1.agregar_arista(3, 5, 19)
grafo1.agregar_arista(4, 5, 4)

print(flujo(grafo1, 0, 5))

# Ejemplo 2
grafo1 = Grafo(True, ["Fu","J","A","C","K","F","E","Su"])

grafo1.agregar_arista("Fu", "J", 1)
grafo1.agregar_arista("Fu", "A", 8)
grafo1.agregar_arista("A", "C", 10)
grafo1.agregar_arista("J", "K", 1)
grafo1.agregar_arista("A", "F", 1)
grafo1.agregar_arista("C", "E", 9)
grafo1.agregar_arista("K", "F", 1)
grafo1.agregar_arista("F", "Su", 1)
grafo1.agregar_arista("E", "Su", 13)

print(flujo(grafo1, "Fu", "Su"))

# Ejemplo 3
grafo1 = Grafo(True, ["A","S","X","V","U","N","Z","W","T"])

grafo1.agregar_arista("A", "S", 1000) # Representa flujo infinito
grafo1.agregar_arista("A", "X", 1000) # Representa flujo infinito
grafo1.agregar_arista("S", "V", 6)
grafo1.agregar_arista("S", "U", 3)
grafo1.agregar_arista("X", "Z", 3)
grafo1.agregar_arista("Z", "W", 1)
grafo1.agregar_arista("Z", "N", 4)
grafo1.agregar_arista("N", "U", 4)
grafo1.agregar_arista("U", "W", 6)
grafo1.agregar_arista("U", "Z", 2)
grafo1.agregar_arista("V", "T", 3)
grafo1.agregar_arista("V", "W", 1)
grafo1.agregar_arista("W", "T", 6)

print(flujo(grafo1, "A", "T"))

# Ejemplo 4
grafo1 = Grafo(True, [0,1,2,3,4,5,6,7])

grafo1.agregar_arista(0, 1, 2)
grafo1.agregar_arista(0, 2, 3)
grafo1.agregar_arista(0, 3, 4)
grafo1.agregar_arista(1, 4, 1)
grafo1.agregar_arista(1, 5, 10)
grafo1.agregar_arista(1, 6, 10)
grafo1.agregar_arista(2, 6, 10)
grafo1.agregar_arista(3, 6, 10)
grafo1.agregar_arista(6, 7, 5)
grafo1.agregar_arista(5, 7, 1)
grafo1.agregar_arista(4, 7, 7)

print(flujo(grafo1, 0, 7))