# Implementar un algoritmo greedy que permita obtener el Dominating Set mínimo (es decir, que contenga la menor
# cantidad de vértices) para el caso de un árbol (en el contexto de teoría de grafos, no un árbol binario). 

# Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué se trata de un algoritmo greedy.
# Indicar si el algoritmo siempre da solución óptima. Si lo es, explicar detalladamente, sino dar un contraejemplo.

from grafo import Grafo

def ordenar_vertices(grafo):

    grados = {}

    for v in grafo.obtener_vertices():
        grados[v] = 0

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):
            grados[w] += 1

    return sorted(grafo.obtener_vertices(), key=lambda v: grados[v], reverse=True)

def es_dominating_set(g, d):
    for v in g.obtener_vertices():
        if v in d:
            continue

        tiene_adyacente_a_un_vertice_en_d = False
        for w in g.adyacentes(v):
            if w in d:
                tiene_adyacente_a_un_vertice_en_d = True
                break
        
        if not tiene_adyacente_a_un_vertice_en_d:
            return False
    
    return True

def dominating_set_min(grafo):
    vertices_ordenados = ordenar_vertices(grafo)
    dominating_set = []

    for v in vertices_ordenados:

        if es_dominating_set(grafo, dominating_set):
            break
        
        dominating_set.append(v)

    return dominating_set

# Justificacion

# 1) Complejidad: Ordenar los vertices segun su grado de entrada cuesta O(n log(n)). Ademàs, iterar la lista de vertices cuesta O(V) y calcular
#                 los grados de entrada cuesta O(V+E). Luego, la complejidad resulta ser O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla sencilla ordenar los vertices por su grado de entrada y quedarnos con los vertices cuyo grado de entrada
#                      sea mayor debido a que cubren mas cantidad de vertices. Luego,  se aplica iterativamente esta regla para obtener el Dominating Set mínimo.
                      
#                      La solucion no es siempre optima. Veamos un contrajemeplo.

#                      Consideremos como ejemplo el grafo utilizado en la prueba.

#                      En este ejemplo, nuestro algoritmo Greedy nos daria como solucion [6,1,5], pero la solucion optima serian [1,4].

grafo1 = Grafo(False, ["1","2","3","4","5","6"])

grafo1.agregar_arista("1","4")
grafo1.agregar_arista("2","4")
grafo1.agregar_arista("3","4")
grafo1.agregar_arista("4","5")
grafo1.agregar_arista("5","6")

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['4', '5'], ['4',  '6']\n")