# Enunciado

Realizar un modelo de programación lineal que obtenga el mínimo Dominating Set de un Grafo no dirigido. En dicho
grafo, cada vértice tiene un valor (positivo), y se quiere que dicho Dominating Set sea el de mínima suma de dichos
valores.

# Solucion

Objetivo: Minimizar la suma del valor de los vertices que dominan todos los vertices del grafo.

Variables:
- $Y_i$: Variable booleana que indica si incluimos el vertice i o no
- $v_i$: Valor del vertice i

Buscamos minimizar 

$$
\sum_{i=1}^{n} Y_i * v_i
$$

cumpliendose la restriccion tal que

$$
Y_i + \sum_{i=1}^{n} Y_j \geq 1
$$

para cada vertice $j$ adyacente a el vertice $i$.

Esta restriccion nos indica que como minimo el conjunto solucion debe incluir al vertice $i$ o alguno de sus adyacentes. Esto con el objetivo de que todos los vertices del grafo sean dominados.

