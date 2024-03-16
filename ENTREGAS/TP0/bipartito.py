# Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. 
# Es decir, la función es_bipartito debe devolver True si el grafo recibido por parámetro es efectivamente 
# bipartito, False en caso contrario. Que un grafo sea Bipartito implica que puede separarse los vértices en dos 
# grupos S y T, tal que para cada par de vértices de S no exista arista entre sí (lo mismo para T), que la 
# intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

# El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de 
# diccionarios), a considerar para la complejidad. 

from grafo import Grafo
from cola import Cola

ROJO = 1
AZUL = 2

def coloreo(grafo, origen, visitados, color):
    """
    Tecnica de coloreo para determinar si un grafo es bipartito o no.
    """

    visitados.add(origen)

    color[origen] = ROJO

    q = Cola()
    q.encolar(origen)

    while not q.esta_vacia():
        v = q.desencolar()

        for w in grafo.adyacentes(v):

            if color[v] == color[w]:
                return False

            if color[w] is None:
                color[w] = AZUL if color[v] == ROJO else ROJO

                visitados.add(w)
                q.encolar(w)
    
    return True

def es_bipartito(grafo):
    """
    Dado un grafo, determina si el mismo es un grafo bipartito o no mediante la tecnica de coloreo.
    """

    if len(grafo.obtener_vertices()) == 0:
        return True

    color = {}
    for v in grafo.obtener_vertices():
        color[v] = None

    visitados = set()

    for v in grafo.obtener_vertices():
        if v not in visitados:
            if (not coloreo(grafo, v, visitados, color)):
                return False

    return True

# Complejidad: La complejidad es O(V+E) ya que visitamos todos los vertices y por cada vertice visitamos
# tambien sus adyacentes.

grafo = Grafo(False, ["A","B","C","D","E","F","G","H","I","J","K","L"])

grafo.agregar_arista("A","F")
grafo.agregar_arista("B","F")
grafo.agregar_arista("B","G")
grafo.agregar_arista("C","H")
grafo.agregar_arista("C","I")
grafo.agregar_arista("D","G")
grafo.agregar_arista("E","F")
grafo.agregar_arista("E","I")

grafo.agregar_arista("J","K")
grafo.agregar_arista("K","L")
grafo.agregar_arista("L","J")

resultado = es_bipartito(grafo)
print(resultado)