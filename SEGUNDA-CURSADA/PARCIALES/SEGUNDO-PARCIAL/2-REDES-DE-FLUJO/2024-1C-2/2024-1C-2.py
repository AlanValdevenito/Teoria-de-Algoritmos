# La Cruz Roja cuenta con n ambulancias, de las cuáles conoce la ubicación de cada una. En un momento dado llegan p pedidos de ambulancias 
# para socorrer personas. Debido a diferentes reglas que tienen, una ambulancia no debe trasladarse más de k kilómetros. Se quiere saber si 
# se puede hacer una asignación de ambulancias a los pedidos, asignando cada una a como máximo 1 pedido. 

# Implementar un algoritmo que resuelva este problema, utilizando redes de flujo. 

# Indicar y justificar la complejidad del algoritmo implementado para el problema planteado.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import math

from grafo import Grafo
from ford_fulkerson import ford_fulkerson

TIPO = 0
POSICION = 1

FUENTE = 'S'
SUMIDERO = 'T'

def distancia(a, b):
    return math.sqrt((a[0] - b[0])**2 + (b[1] - a[1])**2)

def crear_red(ambulancias, pedidos, k):
    grafo = Grafo(True)

    grafo.agregar_vertice(FUENTE)
    grafo.agregar_vertice(SUMIDERO)

    for ambulancia in ambulancias:
        grafo.agregar_arista(FUENTE, ambulancia, 1)

    for pedido in pedidos:
        grafo.agregar_arista(pedido, SUMIDERO, 1)

    for ambulancia in ambulancias:
        for pedido in pedidos:

            if distancia(ambulancia[POSICION], pedido[POSICION]) <= k:
                grafo.agregar_arista(ambulancia, pedido, 1)

    return grafo

def asignar_ambulancias(ambulancias, pedidos, k):
    red = crear_red(ambulancias, pedidos, k)
    flujo = ford_fulkerson(red, FUENTE, SUMIDERO)

    asignacion = []

    for arista, valor in flujo.items():

        if arista[0][0] in (FUENTE, SUMIDERO) or arista[1][0] in (FUENTE, SUMIDERO): continue

        if valor > 0:
            ambulancia = arista[0][0]
            pedido = arista[1][0]
            asignacion.append((ambulancia, pedido))

    return asignacion

ambulancias = [("A1", (3,3)), ("A2", (1,1)), ("A3", (7,7))]
pedidos = [("P1", (1,1)), ("P2", (3,3)), ("P3", (5,5))]
k = 3

assert asignar_ambulancias(ambulancias, pedidos, k) == [("A1", "P1"), ("A2", "P2"), ("A3", "P3")]