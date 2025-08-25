# Imaginá que estamos organizando un torneo de guardias en un castillo. El castillo tiene un suelo dividido en una
# cuadrícula de tamaño n x m, y cada celda puede estar ocupada por un guardia o estar vacía. Los guardias tienen la
# habilidad de vigilar todas las celdas adyacentes a su posición, incluidas las diagonales, es decir, pueden ver las celdas
# vecinas que están justo al lado, arriba, abajo, a la izquierda, a la derecha o en las esquinas.
# Se nos pide colocar la mayor cantidad posible de guardias en el castillo sin que ninguno pueda vigilar a otro. Esto
# significa que no podemos colocar dos guardias en celdas adyacentes, ya que estarían vigilándose mutuamente.

# Implementar un algoritmo greedy que permita colocar el mayor número posible de guardias en el castillo sin que se
# vigilen entre sí. 

# Indicar y justificar la complejidad del algoritmo. 

# Indicar por qué se trata, en efecto, de un algoritmo greedy. 

# El algorimto, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.

def torneo(castillo):
    guardias = []

    for i in range(0, len(castillo), 2):
        for j in range(0, len(castillo[i]), 2):
            guardias.append((i, j))

    return guardias

# Complejidad

# Recorremos la mitad de las filas y la mitad de las columnas que conforman el castillo lo cual tiene una complejidad de O(n x m) con n la cantidad
# de filas y m la cantidad de columnas.

# Algoritmo Greedy 

# El algoritmo Greedy tiene como regla sencilla recorrer el castillo y colocar los guardias intercalando entre filas y columnas de tal forma que se coloquen
# los guardias en la posicion mas proxima que no este siendo vigilada.

# ¿El algoritmo es optimo?. Si, es optimo.

# Supongamos que nuestro algoritmo ya coloco k guardias en el castillo.

# Supongamos que es posible colocar k+1 guardias en el castillo. Esto no es posible porque colocamos cada guardia en la posicion mas proxima que no esta
# siendo vigilada de tal forma que dos guardias no se vigilen mutuamente. 

castillo = [[False, False, False, False],
            [False, False, False, False],
            [False, False, False, False],
            [False, False, False, False]]

assert torneo(castillo) == [(0,0),(0,2),(2,0),(2,2)]

castillo = [[False, False],
            [False, False]]

assert torneo(castillo) == [(0,0)]

castillo = [[False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False],
            [False, False, False, False, False, False]]

assert torneo(castillo) == [(0,0),(0,2),(0,4),(2,0),(2,2),(2,4),(4,0),(4,2),(4,4)]