# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que 
# ninguna pueda comerse con ninguna.

# Nota: El ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible.

def es_compatible(n, puestos, fila, columna):

    # Recorremos todas las reinas ya colocadas y verificamos tres condiciones:
    # - Si alguna reina está en la misma fila (i == fila).
    # - Si alguna reina está en la misma columna (j == columna).
    # - Si alguna reina está en la misma diagonal (diferencia absoluta de filas igual a diferencia absoluta de columnas abs(i - fila) == abs(j - columna)).

    # Si cualquiera de estas condiciones es verdadera, significa que la nueva reina sería atacada, por lo que la función retorna False. 
    # Si no se cumple ninguna, retorna True.

    for (i, j) in puestos:
        if (i == fila) or (j == columna) or (abs(i - fila) == abs(j - columna)):
            return False
    
    return True

def _nreinas(n, puestos, j):

    if len(puestos) == n:
        return True
    
    for i in range(n):
        if es_compatible(n, puestos, i, j):
    
            puestos.add((i, j))
            if _nreinas(n, puestos, j + 1):
                return True

            puestos.remove((i, j))
    
    return False

def nreinas(n):
    puestos = set()
    _nreinas(n, puestos, 0)
    return list(puestos)

assert nreinas(0) == []
assert nreinas(1) == [(0, 0)]
assert nreinas(2) == []
assert nreinas(3) == []
assert nreinas(4) == [(2, 3), (0, 2), (1, 0), (3, 1)]
assert nreinas(8) == [(2, 4), (6, 5), (0, 0), (4, 1), (3, 7), (7, 2), (5, 3), (1, 6)]