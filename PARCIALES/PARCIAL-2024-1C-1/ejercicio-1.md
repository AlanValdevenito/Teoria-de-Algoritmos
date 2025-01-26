# Enunciado

Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar
tres días seguidos. Se tiene la información de la ganancia del día i (Gi), para cada día. Implementar un modelo de
programación lineal que maximice el monto a ganar por Juan, sabiendo que no aceptará trabajar tres días seguidos.

# Solucion

Objetivo: Maximizar el monto a ganar por Juan, sabiendo que no aceptará trabajar tres días seguidos.

Variables:
- $Y_i$: Variable booleana que indica si trabajamos el dia i o no
- $g_i$: Variable entera que indica la ganancia del dia i

Buscamos maximizar 

$$
\sum_{i=1}^{n} Y_i * g_i
$$

cumpliendose la restriccion tal que

$$
Y_i + Y_{i+1} + Y_{i+2} \leq 2 \, para \, i \, \in [1,2,3...,n-2] 
$$