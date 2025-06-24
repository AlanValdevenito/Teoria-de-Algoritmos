from grafo import Grafo
from collections import deque

def _dfs(grafo, v, destino, visitados, pila):
    visitados.add(v)

    if v == destino:
        pila.appendleft(v)
        return

    for w in grafo.adyacentes(v):
        if w not in visitados:
            _dfs(grafo, w, destino, visitados, pila)

    pila.appendleft(v)

def orden_topologico(grafo, origen, destino):
    visitados = set()
    pila = deque()

    _dfs(grafo, origen, destino, visitados, pila)

    return [pila.popleft() for _ in range(0, len(pila))]