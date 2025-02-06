# Implementar un algoritmo Greedy que busque aproximar la solución óptima al problema del mínimo Vertex Cover:
# dado un grafo, obtener el mínimo Vertex Cover del mismo. 

# Indicar la complejidad del algoritmo implementado, dar un contraejemplo para el algoritmo implementado y justificar por 
# qué el algoritmo implementado es un algoritmo greedy.

from grafo import Grafo

def vertex_cover_min(grafo):
    vertices_ordenados = sorted(grafo.obtener_vertices(), key = lambda v: len(grafo.adyacentes(v)), reverse = True)
    print(vertices_ordenados)
    solucion = []

    for v in vertices_ordenados:
        adyacentes_cubiertos = True

        for w in grafo.adyacentes(v):

            if w not in solucion:
                adyacentes_cubiertos = False
                break

        if not adyacentes_cubiertos:
            solucion.append(v)

    return solucion

# Complejidad

# Ordenar los vertices de forma descendente por la cantidad de adyacentes tiene una complejidad de O(V log (V)) con V la cantidad de vertices.

# Iterar los vertices y en cada iteracion iterar sus adyacentes tiene una complejidad de O(V + E).

# Luego, la complejidad total resulta ser O(V log (V)).

# Algoritmo Greedy

# La regla sencilla de nuestro algoritmo Greedy es elegir en el estado actual el vertice con mas adyacentes, con el objetivo de que
# se cubra la mayor cantidad de aristas.

# Luego, se aplica iterativamente esta regla hasta que todas las aristas sean cubiertas con la menor cantidad de vertices.

# El algoritmo no es optimo. Por ejemplo, si consideramos el grafo numero 5 nuestro algoritmo da como resultado el conjunto ['5', '1', '3', '4', '6']
# mientras que el conjunto optimo es ['1', '3', '4', '6'] o ['1', '3', '5', '7']. ¿Por que sucede esto?. Porque nuestro algoritmo primero
# elige los vertices 4 y 6 debido al ordenamiento, cuando lo optimo seria elegir primero el vertice 7.

grafo1 = Grafo(False, ["A","B","C","D","E"])
grafo1.agregar_arista("A","B")
grafo1.agregar_arista("A","C")
grafo1.agregar_arista("B","C")
grafo1.agregar_arista("B","D")
grafo1.agregar_arista("C","D")
grafo1.agregar_arista("D","E")
resultado1 = vertex_cover_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['B', 'C', 'D']\n")

grafo2 = Grafo(False, ["A","B","C","D","E"])
grafo2.agregar_arista("A","C")
grafo2.agregar_arista("C","E")
grafo2.agregar_arista("E","B")
grafo2.agregar_arista("E","D")
resultado2 = vertex_cover_min(grafo2)
print(f"El conjunto minimo de vertices es: {resultado2} y se esperaba ['E', 'C']\n")

grafo3 = Grafo(False, ["A","B","C","D"])
grafo3.agregar_arista("A","D")
grafo3.agregar_arista("B","D")
grafo3.agregar_arista("C","D")
resultado3 = vertex_cover_min(grafo3)
print(f"El conjunto minimo de vertices es: {resultado3} y se esperaba ['D']\n")

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