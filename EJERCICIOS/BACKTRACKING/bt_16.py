# Para ayudar a personas con problemas visuales (por ejemplo, daltonismo) el gobierno de Agrabah decidió que en una misma parada de 
# colectivo nunca pararán dos colectivos que usen el mismo color. El problema es que ya saben que eso está sucediendo hoy en día, así que 
# van a repintar todas las líneas de colectivos. Por problemas presupuestarios, desean pintar los colectivos con la menor cantidad posible 
# k colores diferentes. Como no quieren parecer un grupo de improvisados que malgasta los fondos públicos, quieren hacer un análisis para 
# saber cuál es ese mínimo valor para cumplir con lo pedido (pintar cada línea con alguno de los k colores, de tal forma que no hayan dos 
# de mismo color coincidiendo en la misma parada).

# Considerando que se tiene la información de todas las paradas de colectivo y qué líneas paran allí, modelar el problema utilizando grafos 
# e implementar un algoritmo que determine el mínimo valor k para resolver el problema. 

# Indicar la complejidad del algoritmo implementado.

# Modelado: Los vertices representaran los colectivos y las aristas que unen los vertices representaran que colectivos paran en la misma 
# parada.

from grafo import Grafo

def crear_grafo(colectivos, paradas):
    grafo = Grafo(False, colectivos)

    for parada in paradas:
        for c1 in parada:
            for c2 in parada:

                if c1 == c2:
                    continue

                if not grafo.estan_unidos(c1, c2):
                    grafo.agregar_arista(c1, c2)

    return grafo

def es_compatible(grafo, vertices, actual, coloreados):

    for w in grafo.adyacentes(vertices[actual]):
        if (w in coloreados) and (coloreados[w] == coloreados[vertices[actual]]):
            return False

    return True

def _pintar_colectivos(grafo, vertices, actual, coloreados, k):

    # 1) Si todos los colectivos están coloreados, devolvemos True
    if len(coloreados) == len(vertices):
        return True

    # 2) Probamos colorear con un color el siguiente colectivo
    actual = actual + 1
    for color in range(k):
        coloreados[vertices[actual]] = color

        # 3) Verificamos si la solución parcial es válida
        if es_compatible(grafo, vertices, actual, coloreados):
            # Si es válida, llamamos recursivamente y volvemos a (1)
            if _pintar_colectivos(grafo, vertices, actual, coloreados, k):
                return True

        # Si no es válida, retrocedemos a (2) y probamos con otro color
        del coloreados[vertices[actual]]

    return False

def pintar_colectivos(colectivos, paradas):
    grafo = crear_grafo(colectivos, paradas)
    vertices = grafo.obtener_vertices()
    n = len(vertices)

    # Iniciamos con 1 color y vamos incrementando hasta encontrar una solución válida
    for k in range(1, n + 1):
        coloreados = {}
        if _pintar_colectivos(grafo, vertices, -1, coloreados, k):
            return k  # Retornamos el número mínimo de colores que funciona

    return n  # Si no encontramos antes, se usan n colores (nunca pasa, pues n es un caso límite)

assert pintar_colectivos(['A', 'B', 'C', 'D'], [['A', 'B', 'C'], ['A', 'C', 'D']]) == 3
assert pintar_colectivos([1, 2], [[1, 2]]) == 2
assert pintar_colectivos([1, 2], [[1, 2], [1, 2]]) == 2
assert pintar_colectivos(['A', 'B', 'C', 'D', 'E'], [['A', 'B', 'C', 'E'], ['A', 'C', 'D']]) == 4
assert pintar_colectivos([1, 2, 3, 4, 5], []) == 1