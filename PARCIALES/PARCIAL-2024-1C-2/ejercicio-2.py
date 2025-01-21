from grafo_ff import Grafo
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

            if (w not in padres) and (grafo.peso_arista(v, w) > 0):
                padres[w] = v

                if (w == destino):
                    camino = []

                    while w is not None:
                        camino.append(w)
                        w = padres[w]

                    return camino[::-1]

                cola.append(w)

    return None

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

def flujo(grafo, s, t):
    pedidos = 0

    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)

    while camino is not None:

        for i in range(1, len(camino)):
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], 1)

        pedidos += 1
        camino = obtener_camino(grafo_residual, s, t)

    return pedidos

def crear_red(ambulancias, pedidos, k):
    grafo = Grafo(True)

    fuente = "S"
    grafo.agregar_vertice(fuente)
    
    sumidero = "T"
    grafo.agregar_vertice(sumidero)

    for i, ambulancia in enumerate(ambulancias):
        grafo.agregar_vertice(f"A{i}")
        grafo.agregar_arista(fuente, f"A{i}", 1)

    for i, pedido in enumerate(pedidos):
        grafo.agregar_vertice(f"P{i}")
        grafo.agregar_arista(f"P{i}", sumidero, 1)

    for i, ambulancia in enumerate(ambulancias):
        for j, pedido in enumerate(pedidos):
            distancia = ((ambulancia[0] - pedido[0])**2 + (ambulancia[1] - pedido[1])**2)
            if distancia <= k:
                grafo.agregar_arista(f"A{i}", f"P{j}", 1)

    return grafo

def asignar_ambulancias(ambulancias, pedidos, k):
    grafo = crear_red(ambulancias, pedidos, k)
    return flujo(grafo, "S", "T") == len(pedidos)

ambulancias = [(0,0), (2,2), (5,5)]
pedidos = [(1,1), (3,3), (6,6)]
k = 3

assert asignar_ambulancias(ambulancias, pedidos, k) == True