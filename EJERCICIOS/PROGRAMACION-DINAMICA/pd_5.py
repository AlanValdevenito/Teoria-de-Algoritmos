# Dado un laberinto representado por una grilla, queremos calcular la ganancia máxima que existe desde la posición (0,0) hasta la 
# posición NxM. Los movimientos permitidos son, desde la esquina superior izquierda (el (0,0)), nos podemos mover hacia abajo o hacia 
# la derecha. Pasar por un casillero determinado (i, j) nos da una ganancia de V_{i,j}. 

# Implementar un algoritmo que, por programación dinámica, obtenga la máxima ganancia a través del laberinto. Hacer una reconstrucción 
# del camino que se debe transitar.

# Indicar y justificar la complejidad del algoritmo implementado. 

# Si hay algunos lugares por los que no podemos pasar (obstáculos), ¿cómo se debe modificar para resolver el mismo problema?.

# Aclaración: Solamente por simplicidad de las pruebas automáticas, devolver en este caso la ganancia máxima obtenible. Tener en cuenta 
# que en un examen se pediría la reconstrucción de cómo se obtiene la ganancia.

# Ecuacion de recurrencia: OPT[i][j] = max{llegar desde la izquierda, llegar desde arriba} + V[i][j] =
#                                    = max{OPT[i][j-1], OPT[i-1][j]} + V[i][j]

def laberinto_dinamico(matriz,n, m):
    mem = [[0 for i in range(m)] for j in range(n)]

    for i in range(n):
        for j in range(m):

            # Podemos llegar desde arriba o desde la izquierda
            if (i > 0) and (j > 0):
                mem[i][j] = max(mem[i][j-1], mem[i-1][j]) + matriz[i][j]

            # Podemos llegar solo desde arriba
            elif (i > 0) and (j < 1):
                mem[i][j] = mem[i-1][j] + matriz[i][j]

            # Podemos llegar solo desde la izquierda
            elif (i < 1) and (j > 0):
                mem[i][j] = mem[i][j-1] + matriz[i][j]

            else:
                mem[i][j] = matriz[i][j]

    return mem

def laberinto(matriz):
    n = len(matriz)

    if (n < 1):
        return 0

    m = len(matriz[0])

    mem = laberinto_dinamico(matriz, n, m)
    return mem[n-1][m-1]

# Complejidad: Tenemos O(nxm) por calcular la matriz de memorizacion. Luego, la complejidad total es O(nxm).

assert laberinto([]) == 0
assert laberinto([[10]]) == 10
assert laberinto([[10, 0, 20]]) == 30
assert laberinto([[10, 0, 20], [10, 30, 5]]) == 55
assert laberinto([[10, 0, 20], [10, 50, 20], [10, 0, 20]]) == 110
assert laberinto([[10, 20, 20], [10, 0, 5], [50, 5, 0]]) == 75
assert laberinto([[10, 0, 50], [10, 0, 0], [10, 0, 20]]) == 80