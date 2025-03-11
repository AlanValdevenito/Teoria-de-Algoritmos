# El K-core de un grafo es el subgrafo del mismo en el cuál todos los vértices tienen grados mayor o igual a K. 

# Implementar un algoritmo greedy que dado un grafo y un valor K devuelva el K-core del grafo (es decir, el subgrafo en 
# el cuál todos los vértices involucrados tienen grado mayor o igual a K, en dicho subgrafo). 

# Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué se trata de un algoritmo greedy.

from grafo import Grafo

def k_core(grafo, k):
    vertices_a_eliminar = [v for v in grafo.obtener_vertices() if len(grafo.adyacentes(v)) < k]

    while len(vertices_a_eliminar) > 0:

        for v in vertices_a_eliminar:
            grafo.borrar_vertice(v)

        vertices_a_eliminar = [v for v in grafo.obtener_vertices() if len(grafo.adyacentes(v)) < k]

    return grafo

# Complejidad

# Inicialmente iteramos los vertices del grafo para encontrar los vertices con grado menor a k que debemos eliminar lo cual tiene una 
# complejidad de O(V + E) donde V es la cantidad de vertices y E la cantidad de adyacentes.

# Luego, iteramos hasta que no haya mas vertices que borrar y en cada iteracion actualizamos la lista de vertices a eliminar lo cual
# tiene un costo de O(V + E) donde V es la cantidad de vertices y E la cantidad de adyacentes.

# La complejidad resulta ser O(V + E) donde V es la cantidad de vertices y E la cantidad de adyacentes.

# Algoritmo Greedy

# El algoritmo tiene como regla sencilla eliminar los vertices con grado menor a k en el estado actual para obtener el optimo local.

# Luego, se aplica de forma iterativa esta regla hasta conseguir el optimo global de forma que obtengamos un grafo con vertices con grado
# mayor o igual a k.

# Luego, dado que el algoritmo tiene una regla sencillla que se aplica de forma iterativa es un algoritmo Greedy.

grafo1 = Grafo(False, [0, 1, 2, 3, 4, 5])

grafo1.agregar_arista(0, 1)
grafo1.agregar_arista(1, 2)
grafo1.agregar_arista(2, 5)
grafo1.agregar_arista(1, 4)
grafo1.agregar_arista(4, 3)
grafo1.agregar_arista(3, 0)
grafo1.agregar_arista(4, 5)
grafo1.agregar_arista(0, 4)
grafo1.agregar_arista(1, 3)

assert len(k_core(grafo1, 3).obtener_vertices()) == 4

grafo2 = Grafo(False, [0, 1, 2, 3, 4, 5])

grafo2.agregar_arista(0, 1)
grafo2.agregar_arista(1, 2)
grafo2.agregar_arista(2, 3)
grafo2.agregar_arista(3, 4)
grafo2.agregar_arista(4, 5)
grafo2.agregar_arista(5, 3)
grafo2.agregar_arista(1, 4)

assert len(k_core(grafo2, 2).obtener_vertices()) == 5