# Implementar un algoritmo que dado un grafo no dirigido y conexo, un vértice v y otro w, determine la cantidad
# máxima de caminos disjuntos, y cómo son, que conectan a v con w. 

# Indicar y justificar la complejidad del algoritmo implementado.

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

def ford_fulkerson(grafo, fuente, sumidero):
    cantidad = 0
    caminos = []

    grafo_residual = copiar(grafo)
    camino = obtener_camino(grafo_residual, fuente, sumidero)

    while camino is not None:

        for i in range(1, len(camino)):
            actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], 1)

        cantidad += 1
        caminos.append(camino)

        camino = obtener_camino(grafo_residual, fuente, sumidero)

    return cantidad, caminos

def crear_grafo_ff(grafo, v, w):
    # Creamos un nuevo grafo dirigido
    grafo_ff = Grafo(True)

    i = 0
    # Para cada arista original...
    for a in grafo.obtener_vertices():
        for b in grafo.adyacentes(a):

            # ...ponemos la arista de salida (para la fuente)
            if (a == v):
                grafo_ff.agregar_arista(a, b, 1)

            elif (b == v):
                grafo_ff.agregar_arista(b, a, 1)

            # ...ponemos la arista de entrada (para el sumidero)
            elif (a == w):
                grafo_ff.agregar_arista(b, a, 1)

            elif (b == w):
                grafo_ff.agregar_arista(a, b, 1)

            # ...ponemos la arista de ida y de vuelta, con un vertice intermedio para evitar aristas antiparalelas
            else: 
                i += 1
                grafo_ff.agregar_arista(a, f"I{i}", 1)
                grafo_ff.agregar_arista(f"I{i}", b, 1)

    return grafo_ff
    
def cantidad_caminos_disjuntos(grafo, v, w):
    grafo_ff = crear_grafo_ff(grafo, v, w)
    return ford_fulkerson(grafo_ff, v, w)

grafo = Grafo(False)

grafo.agregar_arista("S", "A", 0)
grafo.agregar_arista("S", "B", 0)
grafo.agregar_arista("A", "T", 0)
grafo.agregar_arista("B", "T", 0)

assert cantidad_caminos_disjuntos(grafo, "S", "T") == (2, [['S', 'A', 'T'], ['S', 'B', 'T']])

grafo = Grafo(False)

grafo.agregar_arista("S", "A", 0)
grafo.agregar_arista("S", "B", 0)
grafo.agregar_arista("A", "C", 0)
grafo.agregar_arista("B", "C", 0)
grafo.agregar_arista("C", "T", 0)

assert cantidad_caminos_disjuntos(grafo, "S", "T") == (1, [['S', 'A', 'I1', 'C', 'T']])