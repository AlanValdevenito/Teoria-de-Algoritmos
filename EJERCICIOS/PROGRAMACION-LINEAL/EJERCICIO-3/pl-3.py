# Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria

from grafo import Grafo

def vertex_cover_min_variable(grafo):
    # Se crean las variables binarias y se guardan en un diccionario de variables de decision binarias
    y = {v: pulp.LpVariable(f"y_{v}", cat="Binary") for v in grafo.obtener_vertices()}

    # Se crea el problema de programacion lineal indicando que se trata de un problema de minimizacion
    problem = pulp.LpProblem("VC", pulp.LpMinimize)
    # Se añade una restriccion al problema
    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            if v < w:
                problem += y[v] + y[w] >= 1
    # Funcion objetivo del problema
    problem += pulp.lpSum(y[v] for v in grafo.obtener_vertices())

    # Se resuelve el problema de PL
    problem.solve()

    return [v for v in grafo.obtener_vertices() if y[v].varValue == 1]

# Test 1

grafo = Grafo(False, ["A","B","C","D","E"])
grafo.agregar_arista("A","B")
grafo.agregar_arista("A","C")
grafo.agregar_arista("B","C")
grafo.agregar_arista("B","D")
grafo.agregar_arista("C","D")
grafo.agregar_arista("D","E")

y = vertex_cover_min_variable(grafo)

print(y)

# Test 2

grafo = Grafo(False, ["A","B","C","D","E"])
grafo.agregar_arista("A","C")
grafo.agregar_arista("C","E")
grafo.agregar_arista("E","B")
grafo.agregar_arista("E","D")

y = vertex_cover_min_variable(grafo)

print(y)

# Test 3

grafo = Grafo(False, ["A","B","C","D"])
grafo.agregar_arista("A","D")
grafo.agregar_arista("B","D")
grafo.agregar_arista("C","D")

y = vertex_cover_min_variable(grafo)

print(y)

# Test 4

grafo = Grafo(False, ["A","B"])

y = vertex_cover_min_variable(grafo)

print(y)

# Test 5

grafo = Grafo(False, ["0","1","2","3","4","5","6","7"])
grafo.agregar_arista("0","1")
grafo.agregar_arista("1","2")
grafo.agregar_arista("1","5")
grafo.agregar_arista("2","3")
grafo.agregar_arista("3","4")
grafo.agregar_arista("5","6")
grafo.agregar_arista("6","7")
grafo.agregar_arista("7","4")
grafo.agregar_arista("5","4")
grafo.agregar_arista("5","3")

y = vertex_cover_min_variable(grafo)

print(y)