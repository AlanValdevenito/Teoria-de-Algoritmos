from grafo_ff import Grafo
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
    flujo = 0

    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, s, t)

    # Mientras haya un camino en la red residual...
    while camino is not None:
        # Calculamos el flujo minimo que puede fluir por el camino
        capacidad_residual_camino = min_peso(grafo_residual, camino)

        for i in range(1, len(camino)):
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)

        flujo += capacidad_residual_camino
        camino = obtener_camino(grafo_residual, s, t)

    return flujo

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

resultado = asignar_ambulancias(ambulancias, pedidos, k)

print(resultado)