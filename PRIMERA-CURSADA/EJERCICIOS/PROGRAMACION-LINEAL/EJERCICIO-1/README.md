# Enunciado

Implementar un modelo de programación lineal que resuelva el Problema de la Mochila de valor máximo (ejercicio 7 de PD).

Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. 

# Solucion

Objetivo: Maximizar el valor de lo que llevamos sin exceder la capacidad W.

Variables:
- W: Capacidad
- $w_i$: Peso del elemento i
- $v_i$: Valor del elmento i
- $Y_i$: Variable booleana que indica si el elemento i es guardado o no

Buscamos maximizar 

$$
\sum_{i=1}^{n} v_i Y_i
$$

cumpliendose la restriccion tal que

$$
\sum_{i=1}^{n} w_i Y_i \leq W 
$$