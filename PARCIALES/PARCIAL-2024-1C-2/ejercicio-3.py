# Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). 

# Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

# Indicar si el algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.

# Independent Set: Conjunto maximo de vertices tal que no hay dos vértices en el conjunto que sean adyacentes entre sí.

from grafo import Grafo

VERTICE = 0
GRADO = 1

def calcular_grado(grafo):
    grados = {}

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados[v] = grados.get(v, 0) + 1

    return grados

def es_compatible(grafo, resultado, v):

    for w in grafo.adyacentes(v):

        if w in resultado:
            return False

    return True

def independent_set(grafo):
    grados = [(v,g) for v,g in calcular_grado(grafo).items()]

    grados_ordenado = sorted(grados, key=lambda e: e[GRADO], reverse = False)

    resultado = set()

    for (v,_) in grados_ordenado:

        if (v not in resultado) and (es_compatible(grafo, resultado, v)):
            resultado.add(v)
    
    print(resultado)
    return resultado

# Complejidad

# Notemos que en principio calculamos el grado de entrada y salida para cada vertice, lo cual tiene una complejidad
# de O(E) siendo E la cantidad de adyacentes de cada vertice. Luego tenemos un ordenamiento con complejidad O(V log(V)) siendo V la 
# cantidad de vertices e iteramos la lista de vertices ordenados por su grado de entrada y salida lo cual tiene una complejidad de 
# O(V). En cada iteracion se valida que los adyacentes del vertice actual no se encuentren en el resultado parcial, lo cual
# tiene una complejidad de O(E) ya que ver si un elemento se encuentra en un conjunto es O(1). Todas las operaciones restantes son 
# O(1).

# Luego, la complejidad resultante es O(V x E).

# Algoritmo Greedy

# Tenemos como regla sencilla quedarnos con el elemento que menor grado de entrada y salida tenga ya que
# aquellos vertices con menor grado cubriran menos vertices del grafo. Luego, se aplica iterativamente esta regla  con el objetivo de 
# maximizar la cantidad de vertices.
# 
# ¿La solucion es optima?. ¿Existe algun contraejemplo?. La solucion no es optima. Un contraejemplo seria un arbol completo de nivel 4.

# Si consideramos un arbol completo de nivel 4, nuestro algoritmo guardara en el Independent Set el primer nodo, los nodos del nivel 1 y 
# todos los nodos del nivel 4 (hojas). El resultado es un Independent Set valido pero el optimo serìa no guardar los nosos del nivel 1, sino
# guardar los nodos del nivel 2.

grafo = Grafo(False, ["0","1","2","3","4","5","6"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("0","2")

grafo.agregar_arista("1","3")
grafo.agregar_arista("1","4")

grafo.agregar_arista("2","5")
grafo.agregar_arista("2","6")

assert independent_set(grafo) == {"0","3","4","5","6"}

grafo = Grafo(False, ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14"])

grafo.agregar_arista("0","1")
grafo.agregar_arista("0","2")

grafo.agregar_arista("1","3")
grafo.agregar_arista("1","4")

grafo.agregar_arista("2","5")
grafo.agregar_arista("2","6")

grafo.agregar_arista("3","7")
grafo.agregar_arista("3","8")
grafo.agregar_arista("4","9")
grafo.agregar_arista("4","10")

grafo.agregar_arista("5","11")
grafo.agregar_arista("5","12")
grafo.agregar_arista("6","13")
grafo.agregar_arista("6","14")

assert independent_set(grafo) == {"7","8","9","10","11","12","13","14","0"}