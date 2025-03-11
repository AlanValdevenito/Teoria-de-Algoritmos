# Enunciado

Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
es el de maximizar la ganancia dada por p[k] − p[j].

Implementar un modelo de programación lineal que determine el día de compra y el día de venta del inmueble.

Indicar la cantidad de restricciones implementadas para esto.

# Solucion

Objetivo: Maximizar la ganancia dada por $p[k] - p[j]$.

Variables:
- $C_i$: Variable booleana que indica si compro el dia i
- $V_i$: Variable booleana que indica si vendo el dia i
- $C_{dia}$: Variable entera que indica el dia de compra
- $V_{dia}$: Variable entera que indica el dia de venta

Dado que solo compramos y vendemos un dia, tenemos que

$$
\sum_{i=0}^{n} C_i = 1
$$

$$
\sum_{i=0}^{n} V_i = 1
$$

Dado que necesariamente se debe comprar antes que vender, se debe conocer que dia
compramos

$$
C_{dia} = \sum_{i=0}^{n} i * C_i
$$

$$
V_{dia} = \sum_{i=0}^{n} i * V_i
$$

Luego, se debe cumplir que $C_{dia} < V_{dia}$

Por ultimo, nuestro objetivo es

$$
max{ \sum_{i=0}^{n} (V_i * p[k]) - (C_i * p[j]) }
$$