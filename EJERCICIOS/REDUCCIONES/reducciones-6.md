# Enunciado

Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Independent Set es un problema NP-Completo.

# Solucion

N-Reinas: El problema de las N-Reinas es un problema de decisión que pregunta si es posible colocar N reinas en un tablero de ajedrez N×N de tal manera que ninguna reina ataque a otra. En términos de ataque, una reina puede atacar a otra si están en la misma fila, columna o diagonal.

Independent Set: Dado un grafo G = (V,E) y un entero k, el problema de Independent Set pregunta si existe un subconjunto de vertices de tamaño k tal que no haya dos vértices en este conjunto que sean adyacentes en G.

El problema de las N-Reinas por enunciado es NP-Completo. Esto significa que no solo está en NP (es decir, una solución puede verificarse en tiempo polinomial), sino que también cualquier problema en NP puede reducirse en tiempo polinomial al problema de las N-Reinas.

Vamos a demostrar que el problema de Independent Set es NP-Completo usando una reducción desde N-Reinas.

1) Transformación del tablero de ajedrez a un grafo: 
- Cada casillero del tablero de ajedrez N×N se convierte en un vértice del grafo.
- Dos vértices están conectados por una arista si y solo si las casillas correspondientes pueden ser atacadas por una reina en una sola jugada. Es decir, si están en la misma fila, columna o diagonal.

2) Construcción del grafo para el problema de N-Reinas:
- Construimos un grafo G donde cada vértice representa un casillero del tablero N×N.
- Añadimos una arista entre dos vértices si las casillas correspondientes están en la misma fila, columna o diagonal.
- Esto garantiza que cualquier conjunto independiente de tamaño N en este grafo corresponde a una disposición de N reinas en el tablero donde ninguna reina puede atacar a otra.

3) Reducción al problema de Independent Set:
- Para determinar si existe una solución al problema de las N-Reinas, necesitamos encontrar un conjunto independiente de tamaño N en el grafo G.
- Si encontramos tal conjunto independiente, significa que es posible colocar N reinas en el tablero de manera que ninguna ataque a otra.

Luego, transformamos el problema de las N-Reinas en el problema de encontrar un conjunto independiente de tamaño N en un grafo G construido de acuerdo a la transformacion mencionada.

Dado que el problema de las N-Reinas es NP-Completo y hemos mostrado cómo se puede reducir el problema de las N-Reinas al problema de Independent Set en tiempo polinomial, concluimos que Independent Set es NP-Completo.