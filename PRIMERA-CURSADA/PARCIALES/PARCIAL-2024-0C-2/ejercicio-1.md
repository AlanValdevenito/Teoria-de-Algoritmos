# Enunciado

Un algoritmo sencillo para multiplicar matrices de n x n demora O($n^3$). 

El algoritmo de Strassen (que utiliza División y Conquista) lo hace en O(n^($log_2 (7)$)).

La profesora Manterola quiere implementar un algoritmo de División y Conquista que sea aún más veloz, donde divida al problema en 
A subproblemas de tamaño de $n/8$, y que juntar las soluciones parciales sea O($n^2$).

¿Cuál es el máximo A para que el orden del algoritmo sea menor que el del algoritmo de Strassen?. Justificar.

# Solucion

## Complejidad del algoritmo de Strassen

A: 7 (Hay escritos siete llamados recursivos)

B: 2 (Se divide al problema en dos)

C: 0 (Operaciones)

$T(n) = A . T(n/B) + O(n^C) = 7 . T(n/2) + O(n^0) = 7 . T(n/2) + O(1)$

$log_B (A) = log_2 (7) = 2,8 > C = 0 → T(n) = O(n^{log_B (A)}) = O(n^{log_2 (7)}) = O(n^{2,8})$

## Complejidad del algoritmo de la profesora Manterola

A: A (Hay escritos A llamados recursivos)

B: 8 (Se divide al problema en ocho)

C: 2 (Operaciones)

$T(n) = A.T(n/B) + O(n^C) = A.T(n/8) + O(n^2) = A.T(n/8) + O(n^2)$

Buscamos hallar el valor de A de tal forma que el orden del algoritmo sea menor que el del algoritmo de Strassen.

Se nos presentan los sigientes casos:

1. $log_B (A) = log_8 (A) < 2 → T(n) = O(n^C) = O(n^2)$

2. $log_B (A) = log_8 (A) = 2 → T(n) = O(n^C log (n)) = O(n^2 log(n))$

3. $log_B (A) = log_8 (A) > 2 → T(n) = O(n^{log_B (A)}) = O(n^{log_8 (A)})$

Descartamos el caso 2 ya que no maximiza A.

Caso 1: $log_8 (A) < 2 → A < 8^2 → A < 64$

Caso 3: $log_8 (A) > 2 → A > $8^2 → A > 64$

Luego, necesitamos que se cumpla $log_8 (A) < log_2 (7) = 2,8 → A < 8^{2,8} < 337,8$.

De esta forma, tenemos que A debe valer $337$. Con $A = 337$ tenemos que $log_8 (337) = 2,79$. Es decir, la complejidad de algoritmo resulta ser O($n^{2,79}$).

Por lo tanto, la profesora Manterola debe implementar su algoritmo de forma que divida al problema en $337$ subproblemas de 
tamaño $n/8$, y que juntar las soluciones parcuales sea O($n^2$).