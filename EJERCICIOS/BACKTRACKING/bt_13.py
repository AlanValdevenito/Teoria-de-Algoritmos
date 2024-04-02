# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen 
# un mínimo Vertex Cover del mismo.

# Un minimo Vertex Cover es un conjunto minimo de vertices tal que "cubre" todas las aristas del grafo.

from grafo import Grafo

def es_compatible(grafo, resultado):

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):

            if v not in resultado and w not in resultado:
                return False
            
    return True

def _vertex_cover_min(grafo, conjunto_actual, conjunto_solucion, indice_actual = 0):

    if (len(conjunto_actual) >= len(conjunto_solucion)) and conjunto_solucion != []:
        return False

    if es_compatible(grafo, conjunto_actual):

        if (len(conjunto_actual) < len(conjunto_solucion)) or conjunto_solucion == []:
            conjunto_solucion.clear()
            conjunto_solucion.extend(conjunto_actual)
            return False

    if indice_actual >= len(grafo.obtener_vertices()):
        return False

    vertice_actual = grafo.obtener_vertices()[indice_actual]

    conjunto_actual.append(vertice_actual)
    if _vertex_cover_min(grafo, conjunto_actual, conjunto_solucion, indice_actual + 1):
        return True

    conjunto_actual.remove(vertice_actual)
    return _vertex_cover_min(grafo, conjunto_actual, conjunto_solucion, indice_actual + 1)

def vertex_cover_min(grafo):
    conjunto = []

    _vertex_cover_min(grafo, [], conjunto)

    return conjunto

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