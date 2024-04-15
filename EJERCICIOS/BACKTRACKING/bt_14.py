# Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice 
# de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D.

# Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima 
# cantidad de vértices.

# Dominating Set: Conjunto minimo de vertices tal que todos los demás vértices no seleccionados 
# estén "cubiertos" por los seleccionados. 

# Ideas de podas:
# 1) Poda por solución no óptima: Si en cualquier punto del proceso de backtracking el tamaño de 
# nuestro set dominante actual supera el tamaño del mejor set dominante encontrado hasta el momento, podemos 
# podar.
# 2) Poda por cobertura completa: Si todos los vértices del grafo están dominados (ya sea porque están en el 
# set dominante o son adyacentes a un vértice en el set), cualquier adición subsiguiente de vértices al set 
# actual es innecesaria y puede ser podada.
# 3) Poda por dominancia de vértices: Algunos vértices pueden ser más "valiosos" que otros en términos de 
# cuántos otros vértices pueden dominar. Si eliges un vértice que domina a menos vértices que otro que no ha 
# sido elegido todavía y ambos pueden ser añadidos al set dominante, es posible que la elección no sea óptima. 
# 4) Poda por vértices ya dominados: Si un vértice ya está dominado (porque es adyacente a algún vértice en 
# el set dominante actual), entonces agregar uno de sus vecinos al set dominante (a menos que ese vecino agregue 
# nuevos vértices no dominados al dominio) no es necesario y puede ser podado.

from grafo import Grafo

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

def _dominating_set_min(grafo, vertices, conjunto_actual, conjunto_optimo, actual = 0):
    
    print(f"Conjunto parcial: {conjunto_actual}")

    if actual == len(vertices):
        return set(conjunto_actual) if len(conjunto_actual) < len(conjunto_optimo) else set(conjunto_optimo)

    vertice_actual = vertices[actual]

    conjunto_actual.remove(vertice_actual)
    if es_dominating_set(grafo, conjunto_actual):
        conjunto_optimo = _dominating_set_min(grafo, vertices, conjunto_actual, conjunto_optimo, actual + 1)

    conjunto_actual.add(vertice_actual)
    return _dominating_set_min(grafo, vertices, conjunto_actual, conjunto_optimo, actual + 1)

def dominating_set_min(grafo):
    return _dominating_set_min(grafo, grafo.obtener_vertices(), set(grafo.obtener_vertices()), set(grafo.obtener_vertices()))

grafo1 = Grafo(False, ["1","2","3","4","5","6"])

grafo1.agregar_arista("1","2")
grafo1.agregar_arista("1","3")
grafo1.agregar_arista("2","3")
grafo1.agregar_arista("2","4")
grafo1.agregar_arista("3","5")
grafo1.agregar_arista("4","5")
grafo1.agregar_arista("4","6")

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['1', '4'], ['3', '4'], ['2', '4'] o ['3', '6']\n")