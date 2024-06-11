# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar cada vértice 
# con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

from grafo import Grafo

def es_compatible(grafo, vertices, actual, coloreados):

    for w in grafo.adyacentes(vertices[actual]):
        if (w in coloreados) and (coloreados[w] == coloreados[vertices[actual]]):
            return False

    return True

def _colorear(grafo, vertices, actual, coloreados, colores):

    print(f"Conjunto actual: {coloreados}\n")

    # 1) Si todos los paises estan coloreados, devolvemos True
    if len(coloreados) == len(vertices):
       return True

    # 2) Probamos colorear con un color el siguiente pais
    actual = actual + 1 
    for c in colores:
        coloreados[vertices[actual]] = c
        
        # 3) Verificamos si la solucion parcial es valida
        if not es_compatible(grafo, vertices, actual, coloreados):
            # Si no lo es, retrocedemos y volvemos a (2) a probar con otro color
            del coloreados[vertices[actual]]
            continue

        # Si lo es, llamamos recursivamente y volvemos a (1)
        if _colorear(grafo, vertices, actual, coloreados, colores):
            return True

    # 4) Si llegamos hasta aca, ya probamos con todo y no encontramos una solucion
    if vertices[actual] in coloreados:
        del coloreados[vertices[actual]]

    return False

def colorear(grafo, n):

    vertices = grafo.obtener_vertices()
    coloreados = {}
    colores = set()

    for i in range(0, n):
        colores.add(i)
    
    return _colorear(grafo, vertices, -1, coloreados, colores)

paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador",
          "Guyana", "Paraguay", "Perú", "Surinam", "Uruguay", "Venezuela"]

grafo = Grafo(False, paises)

grafo.agregar_arista("Argentina", "Bolivia")
grafo.agregar_arista("Argentina", "Brasil")
grafo.agregar_arista("Argentina", "Chile")
grafo.agregar_arista("Argentina", "Paraguay")
grafo.agregar_arista("Argentina", "Uruguay")
grafo.agregar_arista("Bolivia", "Brasil")
grafo.agregar_arista("Bolivia", "Chile")
grafo.agregar_arista("Bolivia", "Paraguay")
grafo.agregar_arista("Bolivia", "Perú")
grafo.agregar_arista("Brasil", "Colombia")
grafo.agregar_arista("Brasil", "Guyana")
grafo.agregar_arista("Brasil", "Paraguay")
grafo.agregar_arista("Brasil", "Perú")
grafo.agregar_arista("Brasil", "Surinam")
grafo.agregar_arista("Brasil", "Uruguay")
grafo.agregar_arista("Brasil", "Venezuela")
grafo.agregar_arista("Chile", "Perú")
grafo.agregar_arista("Colombia", "Ecuador")
grafo.agregar_arista("Colombia", "Perú")
grafo.agregar_arista("Colombia", "Venezuela")
grafo.agregar_arista("Ecuador", "Perú")
grafo.agregar_arista("Guyana", "Surinam")
grafo.agregar_arista("Guyana", "Venezuela")
grafo.agregar_arista("Perú", "Ecuador")

assert colorear(grafo, 3) == False
assert colorear(grafo, 4) == True