# Implementar por backtracking un algoritmo que, dado un grafo no dirigido y un numero n menor a la cantidad de vertices, devuelva si es 
# posible obtener un subconjunto de n vertices tal que ningun par de vertices sea adyacente entre si.

from grafo import Grafo

def es_compatible(grafo, puestos):

    for v in puestos:
        for w in puestos:

            if v == w:
                continue

            if grafo.estan_unidos(v, w):
                return False

    return True

def ya_no_llego(n, vertices, puestos, actual):
    """
    Verifica si es posible seleccionar suficientes vertices restantes en el grafo para llegar a n vertices que forman
    un conjunto solucion. Es decir, verifica si es posible alcanzar una solucion valida a partir del estado actual.
    """

    restantes = len(vertices) - actual
    necesarios = n - len(puestos)
    return restantes < necesarios

def _no_adyacentes(grafo, n, vertices, conjunto_actual, actual = 0):
    
    print(f"Conjunto actual: {conjunto_actual}")

    if (len(conjunto_actual) == n) and es_compatible(grafo, conjunto_actual):
        return conjunto_actual
    
    if (len(vertices) == actual):
        return None

    # Poda
    if not es_compatible(grafo, conjunto_actual) or ya_no_llego(n, vertices, conjunto_actual, actual):
        return None
        
    vertice_actual = vertices[actual]

    conjunto_actual.add(vertice_actual)
    if _no_adyacentes(grafo, n, vertices, conjunto_actual, actual + 1):
        return conjunto_actual

    conjunto_actual.remove(vertice_actual)
    return _no_adyacentes(grafo, n, vertices, conjunto_actual, actual + 1)

def no_adyacentes(grafo, n):
    return _no_adyacentes(grafo, n, grafo.obtener_vertices(), set())

grafo = Grafo(False, ["0","1","2","3","4","5","6","7"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("1","2")
grafo.agregar_arista("1","5")
grafo.agregar_arista("2","3")
grafo.agregar_arista("5","3")
grafo.agregar_arista("6","5")
grafo.agregar_arista("6","7")
grafo.agregar_arista("7","4")
grafo.agregar_arista("5","4")
grafo.agregar_arista("3","4")

assert no_adyacentes(grafo, 4) == {"0","2","4","6"}