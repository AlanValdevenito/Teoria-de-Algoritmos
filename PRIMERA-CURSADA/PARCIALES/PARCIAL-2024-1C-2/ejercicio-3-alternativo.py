# Implementar un algoritmo greedy que permita obtener el Independent Set máximo (es decir, que contenga la mayor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). 

# Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

# Indicar si el algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.

# Independent Set: Conjunto maximo de vertices tal que no hay dos vértices en el conjunto que sean adyacentes entre sí.

from grafo import Grafo

def independent_set(grafo):
    resultado = set()

    while len(grafo.obtener_vertices()) > 0:

        vertice = min(grafo.obtener_vertices(), key=lambda v: len(grafo.adyacentes(v)))

        resultado.add(vertice)

        for w in grafo.adyacentes(vertice):
            grafo.borrar_vertice(w)

        grafo.borrar_vertice(vertice)
    
    return resultado

# Complejidad

# Encontrar el vertice con menor grado tiene una complejdiad O(V).
# Eliminar vertices y actualizar el grafo tiene complejidad O(E).

# Luego, la complejidad resultante es O(V x (V + E)).

# Algoritmo Greedy

# Tenemos como regla sencilla quedarnos con los vertices que menor cantidad de vertices tiene ya que aquellos vertices con menor grado 
# cubriran menos vertices del grafo. Luego, se aplica iterativamente esta regla  con el objetivo de maximizar la cantidad de vertices.
 
# ¿La solucion es optima?. ¿Existe algun contraejemplo?. La solucion es optima al eliminar los vertices que son solucion con sus 
# adyacentes y priorzar los vertices con menor cantidad de adyacentes.

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

assert independent_set(grafo) == {"7","8","9","10","11","12","13","14","1", "2"}