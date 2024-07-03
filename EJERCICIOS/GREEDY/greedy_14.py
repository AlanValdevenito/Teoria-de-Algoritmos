# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos. 

# Implementar un algoritmo Greedy que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden 
# iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las directamente 
# adyacentes a estas (es decir, un “radio de 2 celdas”). 

# Indicar y justificar la complejidad del algoritmo implementado.
#  
# ¿El algoritmo implementado da siempre la solución óptima?. Justificar.

import math

RADIO = 2

def esta_dentro(matriz, i, j):
    n = len(matriz)
    m = len(matriz[0])
    return (0 <= i < n) and (0 <= j < m)

def submarinos_alcanzados(matriz, i, j):
    cantidad = 0
    alcanzados = []

    # Movimientos en el radio de distancia menor o igual a 2
    movimientos = [
        (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2),
        (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2),
        (0, -2), (0, -1), (0, 1), (0, 2),
        (1, -2), (1, -1), (1, 0), (1, 1), (1, 2),
        (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (0, 0)
    ]

    for di, dj in movimientos:
        ni, nj = i + di, j + dj
        distancia = math.sqrt(di**2 + dj**2)
        if esta_dentro(matriz, ni, nj) and (matriz[ni][nj]) and (int(distancia) <= RADIO):
            cantidad += 1
            alcanzados.append((ni, nj))

    return cantidad, alcanzados

# Devolver una lista de faros. Cada faro debe ser una tupla con su posición en (x,y) matriz booleana, indica True en las posiciones 
# con submarinos
def submarinos(matriz):
    faros = []

    while True:

        maximo = 0
        alcanzados = []
        casillero = (0,0)
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):

                # Para todos los casilleros vemos cuantos submarinos son alcanzados
                maximo_parcial, alcanzados_parcial = submarinos_alcanzados(matriz, i, j)

                # Buscamos el casillero que alcanza mas submarinos
                if maximo_parcial > maximo:
                    maximo = maximo_parcial
                    alcanzados = alcanzados_parcial
                    casillero = (i,j)

        # Si ningun casillero alcanzo un submarino, terminamos
        if len(alcanzados) == 0:
            break

        # Colocamos el faro en el casillero que alcanza mas submarinos
        faros.append(casillero)

        # Quitamos los submarinos iluminados
        for submarino in alcanzados:
            i, j = submarino
            matriz[i][j] = False

    return faros

# Justificacion

# 1) Complejidad: Notemos que conocer los submarinos alcanzados por un casillero tiene una complejidad de O(1) ya que el 
#                 numero de posiciones a verificar es fijo. Iterar sobre todos los casilleros de la matriz tiene una 
#                 complejidad de O(NxM). Se itera sobre todos los casilleros de la matriz hasta que no queden submarinos
#                 alcanzables, con lo cual en el peor de los casos esto se repetira S veces Luego, la complejidad
#                 resultante es O(NxMxS).

# 2) Algoritmo Greedy: Tenemos como regla sencilla ver para cada casillero cuantos submarinos alcanza y quedarnos con el casillero
#                      que alcanza la mayor cantidad de submarinos para colocar un faro en este. 
#                      Luego, se actualizan los valores y se aplica iterativamente esta regla para iluminar todos los submarinos
#                      con la menor cantidad de faros posibles.
                      
#                      La solucion no es siempre optima. Veamos un contrajemeplo.

#                      [True,  False, False, False, False, False, False, False, False, True ],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [False, False, False, False, True,  True,  False, False, False, False],
#                      [False, False, False, False, True,  True,  False, False, False, False],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [False, False, False, False, False, False, False, False, False, False],
#                      [True,  False, False, False, False, False, False, False, False, True ]

#                      En este ejemplo, nuestro algoritmo Greedy nos daria como solucion 5 faros, pero la solucion optima serian 4 faros.

assert submarinos([
    [True, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, True, False, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, True]
]) == [(0, 0), (4, 3)]

assert submarinos([
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, True, False, False, False],
    [False, False, False, True, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False]
]) == [(2, 1)]

assert submarinos([
    [True, False, False, False, False, False, False, False, False, True],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, True, True, False, False, False, False],
    [False, False, False, False, True, True, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False, False],
    [True, False, False, False, False, False, False, False, False, True]
]) == [(3, 3), (0, 0), (0, 7), (7, 0), (7, 7)]

assert submarinos([
    [False, False, False, False, False, False],
    [False, False, False, False, False, False],
    [False, False, True, True, False, False],
    [False, False, True, True, False, False],
    [False, False, False, False, False, False],
    [False, False, False, False, False, False]
]) == [(1, 1)]

assert submarinos([
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True],
    [True, True, True, True]
]) == [(1, 1)]
