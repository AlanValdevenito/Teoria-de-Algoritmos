# Enunciado

Implementar un modelo de programación lineal que permita determinar el clique de tamaño máximo dentro de un
grafo. Indicar la cantidad de restricciones generadas en función de la cantidad de vértices y aristas.

# Solucion

Objetivo: Maximizar la cantidad de vertices que esten conectados entre si.

Variables:
- $Y_i$: Variable booleana que indica si incluimos el vertice i o no

Buscamos maximizar 

$$
\sum_{i=1}^{n} Y_i
$$

cumpliendose la restriccion tal que

$$
Y_i + Y_j \leq 1
$$

para cada vertice i, j no adyacente en el grafo.

Esta restriccion nos indica que para cada par de vertices (v,w) no adyacentes, debe estar uno u otro en el conjunto solucion, pero no ambos ya que esto implicaria que el conjunto solucion no es un clique debido a que no estan conectados.

La cantidad de restriciones generadas es $V²-E$ o si queremos ser mas exactos $(V(V-1)/2) - E$.

¿Por que?. Porque el numero de pares de vertices es $(V(V-1)/2)$ y de estos $E$ son aristas, las cuales no generan restricciones porque los vertices conectados pueden formar parte del mismo clique.

Notamos que $(V(V-1)/2)$ incluye tanto los vertices conectados, como los vertices no conectados.

# Solucion alternativa

Buscamos maximizar 

$$
R = \sum_{i=1}^{n} Y_i
$$

cumpliendose la restriccion tal que

$$
Y_i + \sum_{i=1}^{n} Y_j \geq R
$$

para cada vertice j adyacente a el vertice i.

Notamos que si $Y_i$ vale 1, entonces quiere decir que es un vertice que se encuentra en el conjunto solucion, con lo cual todos sus adyacentes estaran en el conjunto solucion. Debido a esto, la suma de $Y_i$ con sus adyacentes debe ser necesariamente igual a $R$.

Por otro lado, si $Y_i$ vale 0, entonces no queremos ponerle una restriccion a los adyacentes.

Para esto utilizamos el truco de la Big-M. Luego, debe cumplirse la restriccion tal que

$$
Y_i + \sum_{i=1}^{n} Y_j \geq R - M(1-Y_i)
$$

donde $M$ es igual a la cantidad de vertices, la cual no es una entrada del problema.

La ventaja de esta solucion se ve en la cantidad de restriciones generadas ya que resulta ser $V$.