# Enunciado

Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover mínimo (ejercicio 13 de BT).

Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen 
un mínimo Vertex Cover del mismo.

Minimum Vertex Cover: Conjunto minimo de vertices tal que cubre todas las aristas del grafo.

# Solucion

Objetivo: Minimizar la cantidad de vertices que cubran todas las aristas del grafo.

Variables:
- $Y_i$: Variable booleana que indica si incluimos el vertice i o no

Buscamos minimizar 

$$
\sum_{i=1}^{n} Y_i
$$

cumpliendose la restriccion tal que

$$
Y_v + Y_w \geq 1
$$

Es decir, para cada arista (v,w) en el grafo, al menos uno de los extremos debe estar en el conjunto solucion.