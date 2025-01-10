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

def celda_vigilada(castillo, celda):

    adyacencias = [
        (-1,-1), (-1,0), (-1,1),
        (0,-1), (0,1),
        (1,-1), (1,0), (1,1),
    ]

    for adyacencia in adyacencias:

        celda_adyacente = (adyacencia[0] + celda[0], adyacencia[1] + celda[1])

        # Validamos que no accedemos a posiciones invalidas del castillo
        if (celda_adyacente[0] < 0) or (celda_adyacente[1] < 0):
            continue

        # Validamos que no accedemos a posiciones invalidas del castillo
        if (celda_adyacente[0] >= len(castillo)) or (celda_adyacente[1] >= len(castillo[0])):
            continue

        if castillo[celda_adyacente[0]][celda_adyacente[1]]:
            return True
        
    return False

def torneo(castillo):
    
    guardias = []

    for i in range (0, len(castillo)):
        for j in range (0, len(castillo[i])):
            
            # Validamos que no haya un guardia en la posicion actual (i,j)
            if castillo[i][j]:
                continue

            celda = (i,j)

            # Validamos si la posicion actual (i,j) esta vigilada
            # En caso de que ningun guardia la este vigilando, colocamos un guardia en la posicion actual (i,j)
            if not celda_vigilada(castillo, celda):
                castillo[i][j] = True
                guardias.append(celda)

    return guardias

# Complejidad

# El algoritmo recorre todas las celdas del castillo, con lo cual por esto tenemos una complejidad de O(n x m) siendo n la cantidad de filas
# y m la cantidad de columnas. En cada iteracion:
# 1) Validamos si en la posicion actual hay un guardia, lo cual tiene una complejidad de O(1).
# 2) Validams si la posicion actual esta vigilada, lo cual tiene una complejidad de O(A) siendo A la cantidad de celdas adyacentes de la celda actual.

# Notamos que cada celda tiene 8 celdas adyacentes que deben ser validadas.

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