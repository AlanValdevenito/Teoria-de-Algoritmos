# Enunciado

Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago (ejercicio 4 de PD).

Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. 
Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que 
no aceptará trabajar dos días seguidos. 

# Solucion

Objetivo: Maximizar la ganancia de los dias trabajados, sabiendo que Juan no aceptara trabajar dos dias seguidos.

Variables:
- $g_i$: Ganancia del dia i
- $Y_i$: Variable booleana que indica si Juan trabaja el dia i o no

Buscamos maximizar 

$$
\sum_{i=1}^{n} g_i Y_i
$$

cumpliendose la restriccion tal que

$$
Y_i + Y_{i+1} \leq 1 \, para \, i \, \in [1,2,3...,n-1] 
$$