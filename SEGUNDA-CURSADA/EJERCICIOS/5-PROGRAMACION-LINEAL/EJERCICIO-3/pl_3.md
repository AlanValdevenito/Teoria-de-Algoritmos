# Enunciado

Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto. 

Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.

Implementar un modelo de programación lineal que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

# Solucion

¿Que tipo de problema es?. Es un problema de minimizacion ya que nos piden un minimo Vertex Cover.

Definimos variables:
1. $Y_i$: Variable booleana que indica si el vertice $i$ esta incluido en el Vertex Cover

¿Como hacemos para incluir todas las aristas?:

$$
Y_v + Y_w \geq 1
$$ 

Esta ultima inecuacion debe cumplirse para toda arista (v, w) en el grafo.

Luego, buscamos minimizar la cantidad de vertices incluidos:

$$
min \sum_{i=1}^{n} Y_i
$$

