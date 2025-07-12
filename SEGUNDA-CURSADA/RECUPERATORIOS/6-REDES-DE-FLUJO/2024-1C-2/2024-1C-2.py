# La Cruz Roja cuenta con n ambulancias, de las cuáles conoce la ubicación de cada una. En un momento dado llegan p pedidos de ambulancias para socorrer 
# personas. Debido a diferentes reglas que tienen, una ambulancia no debe trasladarse más de k kilómetros. Se quiere saber si se puede hacer una asignación 
# de ambulancias a los pedidos, asignando cada una a como máximo 1 pedido. 

# Implementar un algoritmo que resuelva este problema, utilizando redes de flujo. 

# Indicar y justificar la complejidad del algoritmo implementado para el problema planteado.

# Notamos que este problema es similar al problema de Bipartite Matching con la particularidad de que tenemos ambulancias y pedidos, y una restricción de 
# distancia.

# ¿Como modelamos el problema?:
# 1. Tendremos una fuente S y un sumidero T.
# 2. Desde S, tendremos aristas hacia cada ambulancia que representaremos con vertices, con capacidad 1.
# 3. Desde cada ambulancia, tendremos aristas hacia los pedidos que representaremos con vertices, con capacidad 1. Las ambulancias y los pedidos se uniran
#    mediante aristas si la distnacia entre la ambulancia y el pedido es menor o igual a k.
# 4. Desde cada pedido, tendremos aristas hacia el sumidero T, con capacidad 1.

# Notamos que definimos el peso de cada arista con capacidad 1, ya que cada ambulancia puede atender a un solo pedido y cada pedido puede ser atendido por 
# una sola ambulancia. Es decir, de esta forma nos aseguramos de cumplir con la restriccion de que se asigna cada ambulancia a como maximo 1 pedido.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from grafo import Grafo
from ford_fulkerson import ford_fulkerson

import math

FUENTE = 'S'
SUMIDERO = 'T'

def puede_trasladarse(ambulancia, pedido, k):
    distancia = math.sqrt((ambulancia[0] - pedido[0]) ** 2 + (ambulancia[1] - pedido[1]) ** 2)
    return (distancia <= k)

def crear_red(ambulancias, pedidos, k):
    red = Grafo(True)

    red.agregar_vertice(FUENTE)
    red.agregar_vertice(SUMIDERO)

    for i in range(0, len(ambulancias)):
        vertice = f'A{i}'
        red.agregar_vertice(vertice)
        red.agregar_arista(FUENTE, vertice, 1)

    for i in range(0, len(pedidos)):
        vertice = f'P{i}'
        red.agregar_vertice(vertice)
        red.agregar_arista(vertice, SUMIDERO, 1)

    for i, ambulancia in enumerate(ambulancias):
        for j, pedido in enumerate(pedidos):
            vertice_ambulancia = f'A{i}'
            vertice_pedido = f'P{j}'
            
            if puede_trasladarse(ambulancia, pedido, k):
                red.agregar_arista(vertice_ambulancia, vertice_pedido, 1)

    return red

def asignacion_pedidos(ambulancias, pedidos, k):
    red = crear_red(ambulancias, pedidos, k)
    flujo = ford_fulkerson(red, 'S', 'T')

    flujo_maximo = sum(flujo[(FUENTE, f'A{i}')] for i in range(0, len(ambulancias)))
    p = len(pedidos)

    return (flujo_maximo == p)

# Complejidad

# Creacion de la red de flujo: La complejidad de la creacion de la red es O(n x p) donde n es el numero de ambulancias y p es el 
# numero de pedidos.

# Ford-Fulkerson: La complejidad del algoritmo de Ford-Fulkerson es O(V x E^2) en el peor de los casos, donde V es el número de 
# vértices y E es el número de aristas.

# Luego, la complejidad total resulta ser O(n x p + V x E^2) donde n es el numero de ambulancias, p es el numero de pedidos, V es 
# el número de vértices y E es el número de aristas.

ambulancias = [(4, 4), (3, 1), (6, 6)]
pedidos = [(3, 0), (3, 3), (5, 5)]
k = 2
assert asignacion_pedidos(ambulancias, pedidos, k) == True

ambulancias = [(4, 4), (3, 1), (6, 6)]
pedidos = [(0, 0), (3, 3), (5, 5)]
k = 2
assert asignacion_pedidos(ambulancias, pedidos, k) == False