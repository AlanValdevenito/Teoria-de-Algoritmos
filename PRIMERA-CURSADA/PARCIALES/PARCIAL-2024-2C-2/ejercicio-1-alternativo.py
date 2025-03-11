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

# El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.

def torneo(castillo):
    
    guardias = []

    for i in range (0, len(castillo), 2):
        for j in range (0, len(castillo[i]), 2):
            guardias.append((i,j))

    return guardias

# Complejidad

# El algoritmo recorre la mitad de las celdas del castillo, con lo cual por esto tenemos una complejidad de O(n/2 x m/2) siendo n la cantidad de filas
# y m la cantidad de columnas. ¿Por que recorremos la mitad de la celdas?. Debido a que recorremos la mitad de las filas y la mitad de las
# columnas debido al requisito de no adyacencia del problema.

# Luego, la complejidad resulta ser O(n x m).

# Algoritmo Greedy

# ¿Por que se trata de un algoritmo Greedy?. Se trata de un algoritmo Greedy ya que tiene una regla sencilla la cual se basa en colocar
# un guardia en la posicion mas proxima que no este siendo vigilada.

# ¿Es optimo?. El algoritmo es optimo ya que se colocan los guardias en todas las celdas posibles que no estan siendo vigiladas. Es
# decir que se coloca el mayor número posible de guardias en el castillo.

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