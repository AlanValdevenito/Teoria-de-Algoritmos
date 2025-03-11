# Se tiene una matriz de n x m casilleros, en la cual empezamos en la posición (0, 0) (arriba a la izquierda) y queremos
# llegar a la posición (n - 1, m - 1) (abajo a la derecha), pero solamente nos podemos mover hacia abajo o hacia la
# derecha, y comenzamos con una vida inicial V. Cada casillero puede estar vacío, o tener una trampa. En los casilleros
# que hay trampas se nos reduce la vida en una cantidad T_i conocida (dependiente de cada casillero).

# Diseñar un algoritmo de programación dinámica que dados todos los datos necesarios, permita determinar la cantidad
# de vida máxima con la que podemos llegar a (n - 1, m - 1).
                                            
# Implementar también una forma de poder reconstruir dicho camino. 

# Indicar la complejidad del algoritmo propuesto, en tiempo y espacio.

# Idea 1: Maximizar la vida restante
# Idea 2: Minimizar el daño recibido

# Minimizar el daño recibido y maximizar la vida restante son estrategias equivalentes.

# Minimizar el daño acumulado tiene el mismo efecto que maximizar la vida restante, ya que una implica la otra. Por lo tanto, ambos 
# enfoques son válidos y no hay diferencia en el resultado final.

# La diferencia entre las dos formulaciones se encuentra únicamente en cómo expresamos la ecuación de recurrencia:
# - Si minimizamos el daño, la matriz almacena el costo total de daño hasta cada celda.
# - Si maximizamos la vida, la matriz almacena la vida restante al llegar a cada celda.

# Ambas estrategias llevan a la misma solución óptima

# Ecuacion de recurrencia OPT(i,j) = min{llegar por la izquierda, llegar por arriba} + V(i,j) = min{OPT(i,j-1), OPT(i-1,j)} + V(i,j)

def laberinto_dinamico(matriz, n, m):
    mem = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n): # Fila = arriba
        for j in range(m): # Columna = izquierda

            # Podemos llegar desde la izquierda o arriba
            if (i > 0 and j > 0):
                mem[i][j] = min(mem[i][j-1], mem[i-1][j]) + matriz[i][j]

            # Podemos llegar solo desde la izquierda
            elif (i < 1 and j > 0):
                mem[i][j] = mem[i][j-1] + matriz[i][j]

            # Podemos llegar solo desde arriba
            elif (i > 0 and j < 1):
                mem[i][j] = mem[i-1][j] + matriz[i][j]

            else:
                mem[i][j] = matriz[i][j]

    return mem

def laberinto_solucion(matriz, mem, n, m):
    solucion = []

    solucion.append((n,m))

    while (n > 0 or m > 0):

        trampa = matriz[n][m]
        anterior = mem[n][m] - trampa

        # Vinimos desde arriba
        if (n > 0) and (mem[n-1][m] == anterior):
            solucion.append((n-1,m))
            n -= 1

        # Vinimos desde la izquierda
        elif (m > 0) and (mem[n][m-1] == anterior):
            solucion.append((n,m-1))
            m -= 1

    solucion.reverse()
    return solucion

def laberinto(matriz, vida):

    n, m = len(matriz), len(matriz[0])
    
    mem = laberinto_dinamico(matriz, n, m)
    solucion = laberinto_solucion(matriz, mem, n-1, m-1)

    return vida - mem[n-1][m-1], solucion

# Complejidad

# La complejidad en tiempo es por un lado O(n x m) para la construccion de la matriz de memorizacion debido a que 
# recorremos toda la matriz y por otro lado O(n + m) para la reconstruccion de la solucion debido a que recorremos la matriz

# Luego, la complejidad resulta ser O(n x m) con n y m el tamaño de la matriz

# La complejidad en espacio es O(n x m) debido a la matriz de memorizacion ya que almacenamos el daño recibido en cada casillero

assert laberinto([[10]], 100) == (90, [(0, 0)])

assert laberinto([[10, 0, 20]], 100) == (70, [(0, 0), (0, 1), (0, 2)])

assert laberinto([[10, 0, 20], 
                  [10, 30, 5]], 100) == (65, [(0, 0), (0, 1), (0, 2), (1, 2)])

assert laberinto([[10, 0, 20], 
                  [10, 50, 20], 
                  [10, 0, 20]], 100) == (50, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

assert laberinto([[10, 20, 20], 
                  [10, 0, 5], 
                  [50, 5, 0]], 100) == (75, [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)])

assert laberinto([[10, 0, 50], 
                  [10, 0, 0], 
                  [10, 0, 20]], 100) == (70, [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)])
