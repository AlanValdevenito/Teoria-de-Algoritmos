# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible) a n reinas de tal manera que 
# ninguna pueda comerse con ninguna.

# Nota: El ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible.

from grafo import Grafo

def crear_tablero(n):
    casillero = lambda i, j: (i, j)
    grafo = Grafo(False)

    # Agrego los vertices
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice(casillero(i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                grafo.agregar_arista(casillero(i, j), casillero(i, k))
    
    # Agrego adyacencia por columnas
    for j in range(n):
        for i in range(n):
            for k in range(i+1, n):
                grafo.agregar_arista(casillero(i, j), casillero(k, j))

    # Agrego adyacencia por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if k < j:
                    grafo.agregar_arista(casillero(i, j), casillero(i - k - 1, j - k - 1))
                if k + j + 1 < n:
                    grafo.agregar_arista(casillero(i, j), casillero(i - k - 1, j + k + 1))
    
    return grafo

def es_compatible(grafo, puestos):

    for v in puestos:
        for w in puestos:

            if v == w:
                continue
            
            if grafo.estan_unidos(v, w):
                return False
            
    return True

def _nreinas(grafo, vertices, actual, puestos, n):

    print(f"Conjunto parcial: {puestos}")

    if len(puestos) == n:
        return es_compatible(grafo, puestos)
    
    if len(vertices) == actual:
        return False

    if not es_compatible(grafo, puestos):
        return False
    
    vertice_actual = vertices[actual]
    puestos.add(vertice_actual)
    if _nreinas(grafo, vertices, actual + 1, puestos, n):
        return True
    
    puestos.remove(vertice_actual)
    return _nreinas(grafo, vertices, actual + 1, puestos, n)

def nreinas(n):
    grafo = crear_tablero(n)

    puestos = set()
    vertices = grafo.obtener_vertices()

    _nreinas(grafo, vertices, 0, puestos, n)

    return list(puestos)

assert nreinas(0) == []
assert nreinas(1) == [(0, 0)]
assert nreinas(2) == []
assert nreinas(3) == []
assert sorted(nreinas(4)) == sorted([(1, 3), (0, 1), (2, 0), (3, 2)])
assert sorted(nreinas(8)) == sorted([(7, 3), (4, 2), (1, 4), (2, 7), (5, 6), (0, 0), (6, 1), (3, 5)])