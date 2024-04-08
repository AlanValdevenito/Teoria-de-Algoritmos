# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen 
# un mínimo Vertex Cover del mismo.

# Minimum Vertex Cover: Conjunto minimo de vertices tal que "cubre" todas las aristas del grafo.

from grafo import Grafo

def es_compatible(grafo, resultado):

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):

            if v not in resultado and w not in resultado:
                return False
            
    return True

def _vertex_cover_min(grafo, solucion_parcial, mejor_solucion, indice_actual = 0):

    print(f"Conjunto parcial: {solucion_parcial}")

    # Si el tamaño de nuestro set parcial supera el tamaño del mejor set encontrado hasta el momento, podamos.
    if (len(solucion_parcial) >= len(mejor_solucion)) and mejor_solucion != []:
        return

    # Si el set parcial es compatible con la definicion de Vertex Cover...
    if es_compatible(grafo, solucion_parcial):

        # ... y el set parcial tiene un tamaño menor que el mejor set, actualizamos nuestro mejor set.
        if (len(solucion_parcial) < len(mejor_solucion)) or mejor_solucion == []:
            mejor_solucion.clear()
            mejor_solucion.extend(solucion_parcial)
            return

    # Caso base: Visitamos todos los vertices.
    if indice_actual >= len(grafo.obtener_vertices()):
        return

    vertice_actual = grafo.obtener_vertices()[indice_actual]

    solucion_parcial.append(vertice_actual)
    _vertex_cover_min(grafo, solucion_parcial, mejor_solucion, indice_actual + 1)

    solucion_parcial.remove(vertice_actual)
    _vertex_cover_min(grafo, solucion_parcial, mejor_solucion, indice_actual + 1)

def vertex_cover_min(grafo):
    solucion = []

    _vertex_cover_min(grafo, [], solucion)

    return solucion

grafo1 = Grafo(False, ["A","B","C","D","E"])
grafo1.agregar_arista("A","B")
grafo1.agregar_arista("A","C")
grafo1.agregar_arista("B","C")
grafo1.agregar_arista("B","D")
grafo1.agregar_arista("C","D")
grafo1.agregar_arista("D","E")
resultado1 = vertex_cover_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['A', 'B', 'D'],  ['A', 'C', 'D'] o ['B', 'C', 'E']\n")

grafo2 = Grafo(False, ["A","B","C","D","E"])
grafo2.agregar_arista("A","C")
grafo2.agregar_arista("C","E")
grafo2.agregar_arista("E","B")
grafo2.agregar_arista("E","D")
resultado2 = vertex_cover_min(grafo2)
print(f"El conjunto minimo de vertices es: {resultado2} y se esperaba ['E', 'C'] o ['E', 'A']\n")

grafo3 = Grafo(False, ["A","B","C","D"])
grafo3.agregar_arista("A","D")
grafo3.agregar_arista("B","D")
grafo3.agregar_arista("C","D")
resultado3 = vertex_cover_min(grafo3)
print(f"El conjunto minimo de vertices es: {resultado3} y se esperaba ['D']\n")

grafo4 = Grafo(False, ["A","B"])
resultado4 = vertex_cover_min(grafo4)
print(f"El conjunto minimo de vertices es: {resultado4} y se esperaba []\n")

grafo5 = Grafo(False, ["0","1","2","3","4","5","6","7"])
grafo5.agregar_arista("0","1")
grafo5.agregar_arista("1","2")
grafo5.agregar_arista("1","5")
grafo5.agregar_arista("2","3")
grafo5.agregar_arista("3","4")
grafo5.agregar_arista("5","6")
grafo5.agregar_arista("6","7")
grafo5.agregar_arista("7","4")
grafo5.agregar_arista("5","4")
grafo5.agregar_arista("5","3")
resultado5 = vertex_cover_min(grafo5)
print(f"El conjunto minimo de vertices es: {resultado5} y se esperaba ['1', '3', '4', '6'] o ['1', '3', '5', '7']")