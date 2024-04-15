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

def es_compatible(g, d):

    for v in g.obtener_vertices():

        if v not in d:
            tiene_adyacente_a_un_vertice_en_d = False

            for w in g.adyacentes(v):

                if w in d:
                    tiene_adyacente_a_un_vertice_en_d = True
                    break

            if not tiene_adyacente_a_un_vertice_en_d:
                return False
            
    return True

def _dominating_set_min(grafo, solucion_parcial, mejor_solucion, indice_actual = 0):
    
    print(f"Conjunto parcial: {solucion_parcial}")

    # Si el tamaño de nuestro set parcial supera el tamaño del mejor set encontrado hasta el momento, podamos.
    if (len(solucion_parcial) >= len(mejor_solucion)) and mejor_solucion != []:
        return

    # Si el set parcial es compatible con la definicion de Dominating Set...
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
    _dominating_set_min(grafo, solucion_parcial, mejor_solucion, indice_actual + 1)

    solucion_parcial.remove(vertice_actual)
    _dominating_set_min(grafo, solucion_parcial, mejor_solucion, indice_actual + 1)

def dominating_set_min(grafo):
    solucion = []

    _dominating_set_min(grafo, [], solucion)

    return solucion

grafo1 = Grafo(False, ["1","2","3","4","5", "6"])

grafo1.agregar_arista("1","2")
grafo1.agregar_arista("1","3")
grafo1.agregar_arista("2","3")
grafo1.agregar_arista("2","4")
grafo1.agregar_arista("3","5")
grafo1.agregar_arista("4","5")
grafo1.agregar_arista("4","6")

resultado1 = dominating_set_min(grafo1)
print(f"El conjunto minimo de vertices es: {resultado1} y se esperaba ['1', '4'], ['3', '4'] o ['2', '4']\n")