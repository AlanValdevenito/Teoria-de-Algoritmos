# Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

from typing import List

import pulp
from pulp import LpAffineExpression as Sumatoria

def mochila_variable(v: List[int], w: List[int], W: int):
    # Lista de variables de decision binarias
    y = []

    # Se crean las variables binarias y se guardan en la lista
    for i in range(len(v)):
        y.append(pulp.LpVariable("y" + str(i), cat="Binary"))

    # Se crea el problema de programacion lineal indicando que se trata de un problema de maximizacion
    problem = pulp.LpProblem("Mochila", pulp.LpMaximize)
    # Se añade una restriccion al problema
    problem += Sumatoria([(y[i], w[i]) for i in range(len(y))]) <= W
    # Funcion objetivo del problema
    problem += Sumatoria([(y[i], v[i]) for i in range(len(y))])

    # Se resuelve el problema de PL
    problem.solve()
    return list(map(lambda yi: pulp.value(yi), y))

# Test 1

valores = [10,1,8,100,6,11,7,2,11]
pesos = [6,1,3,100,4,2,8,7,9]
W = 19
y = mochila_variable(valores, pesos, W)

print(y)

print("Peso usado:", sum([pesos[i] * y[i] for i in range(len(y))]))
print("Valor obtenido:", sum([valores[i] * y[i] for i in range(len(y))]))