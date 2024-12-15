# Definimos a un grafo ordenado como un grafo dirigido con vértices v1, ···, vn en el que todos los vértices, salvo vn
# tienen al menos una arista que sale del vértice, y cada arista va de un vértice de menor índice a uno de mayor índice (es
# decir, las aristas tienen la forma (vi, vj) con i < j).

# Implementar un algoritmo de programación dinámica que dado un grafo ordenado (y, si les resulta útil, una lista con los vértices en orden) 
# determine cuál es la longitud del camino más largo. Dar la ecuación de recurrencia correspondiente. 

# Dar también el algoritmo de recontrucción de la solución.

# Indicar y justificar la complejidad del algoritmo implementado.

# Ecuacion de recurrencia: OPT(i) = max{OPT(j) + 1} donde j se corresponde a los vertices V_j predecesores de V_i

from grafo import Grafo

def camino_mas_largo_dinamico(grafo, vertices):
    mem = [0] * len(vertices)

    for i in range(0, len(vertices)):
        caminos = []
        for j in range (0, i):

            if grafo.estan_unidos(vertices[j], vertices[i]):
                caminos.append(1 + mem[j])

        mem[i] = max(caminos) if len(caminos) > 0 else 0

    print(mem)
    return mem

def camino_mas_largo_solucion(grafo, vertices, mem):
    
    i = max(range(len(mem)), key = lambda v: mem[v])
    solucion = [vertices[i]]

    while mem[i] > 0:
        for j in range(0, i):
            if mem[j] == mem[i] - 1 and grafo.estan_unidos(vertices[j], vertices[i]):
                solucion.append(vertices[j])
                i = j
                break

    solucion.reverse()
    return solucion

def camino_mas_largo(grafo, vertices):
    mem = camino_mas_largo_dinamico(grafo, vertices)
    solucion = camino_mas_largo_solucion(grafo, vertices, mem)
    return solucion

# Complejidad

# Construccion de la matriz de memorizacion: Se iteran los vertices y en cada iteracion los
# predecedores de cada vertice. En el peor caso, los predecedores serian todos los vertices
# con lo cual la complejidad resulta ser O(V²) donde V es la cantidad de vertices. 

# Re-construccion de la solucion: Encontrar el indice i con el camino mas largo tiene
# una complejidad de O(V) ya que recorremos toda la matriz de memorizacion buscando el
# maximo valor. Por otro lado, tenemos dos bucles anidados donde en el peor caso si
# el camino mas largo recorre todos los vertices la complejidad resulta ser O(V²).

# Luego, la complejidad total resulta ser O(V²).

grafo = Grafo(True, ["1","2","3","4","5"])

grafo.agregar_arista("1","2")
grafo.agregar_arista("1","4")

grafo.agregar_arista("2","4")
grafo.agregar_arista("2","5")

grafo.agregar_arista("3","4")

grafo.agregar_arista("4","5")

assert camino_mas_largo(grafo, ["1","2","3","4","5"]) == ["1","2","4","5"]