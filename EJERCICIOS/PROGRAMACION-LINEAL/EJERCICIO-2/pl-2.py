# Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria

def juan_el_vago_variable(g: List[int]):
    # Lista de variables de decision binarias
    y = []

    # Se crean las variables binarias y se guardan en la lista
    for i in range(len(g)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))

    # Se crea el problema de programacion lineal indicando que se trata de un problema de maximizacion
    problem = pulp.LpProblem("Juan", pulp.LpMaximize)
    # Se añade una restriccion al problema
    for i in range(len(y)-1):
        problem += y[i] + y[i+1] <= 1
    # Funcion objetivo del problema
    problem += Sumatoria([(y[i], g[i]) for i in range(len(y))])

    # Se resuelve el problema de PL
    problem.solve()
    return list(map(lambda yi: pulp.value(yi), y))

# Test 1

ganancia = [100,20,30,70,50]
y = juan_el_vago_variable(ganancia)

print(y)

print("Ganancia obtenida:", sum([ganancia[i] * y[i] for i in range(len(y))]))

# Test 2

ganancia = [100,20,30,70,20]
y = juan_el_vago_variable(ganancia)

print(y)

print("Ganancia obtenida:", sum([ganancia[i] * y[i] for i in range(len(y))]))