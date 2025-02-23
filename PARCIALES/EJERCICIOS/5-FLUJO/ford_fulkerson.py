from grafo import Grafo
from collections import deque

def copiar(grafo):
    nuevo_grafo = Grafo(grafo.dirigido)

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            nuevo_grafo.agregar_arista(v, w, grafo.peso_arista(v,w))

    return nuevo_grafo

def obtener_camino(grafo, origen, destino):
    padres = {origen: None}
    cola = deque([origen])

    while cola:
        v = cola.popleft()

        for w in grafo.adyacentes(v):

            # Si el nodo no ha sido visitado y la capacidad residual (peso de la arista) es mayor a 0...
            if (w not in padres) and (grafo.peso_arista(v, w) > 0):
                padres[w] = v

                # Si se alcanza el destino (sumidero), reconstruimos el camino y se retorna en el orden correcto
                if (w == destino):
                    camino = []

                    while w is not None:
                        camino.append(w)
                        w = padres[w]

                    return camino[::-1]

                cola.append(w)

    return None

def min_peso(grafo_residual, camino):
    return min(grafo_residual.peso_arista(camino[i], camino[i+1]) for i in range(len(camino)-1))

def actualizar_grafo_residual(grafo_residual, v, w, valor):
    peso_anterior = grafo_residual.peso_arista(v, w)

    if valor == peso_anterior:
        grafo_residual.borrar_arista(v, w)
    else:
        grafo_residual.cambiar_peso(v, w, peso_anterior - valor)

    if not grafo_residual.estan_unidos(w, v):
        grafo_residual.agregar_arista(w, v, valor)
    else:
        grafo_residual.cambiar_peso(w, v, grafo_residual.peso_arista(w, v) + valor)

def ford_fulkerson(grafo, s, t):
    flujo = {}

    # Inicializamos el flujo de cada arista en 0
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            flujo[(v, w)] = 0

    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)

    # Mientras exista un camino en la red residual...
    while camino is not None:
        # Obtenemos el flujo minimo que puede fluir por el camino
        capacidad_residual_camino = min_peso(grafo_residual, camino)

        # Recorremos el camino
        for i in range(1, len(camino)):

            # Si la arista existe en el grafo original, aumenta el flujo
            if grafo.estan_unidos(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)
            
            # Si la arista no eixste en el grafo original, reduce el flujo (camino inverso)
            else:
                flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)

        camino = obtener_camino(grafo_residual, s, t)

    return flujo
