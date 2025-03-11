class Grafo:
    def __init__(self, dirigido=True, vertices=None):
        self.dirigido = dirigido
        self.adyacencias = {}
        if vertices:
            for v in vertices:
                self.adyacencias[v] = {}

    def agregar_arista(self, u, v, peso):
        if u not in self.adyacencias:
            self.adyacencias[u] = {}
        self.adyacencias[u][v] = peso
        if not self.dirigido:
            if v not in self.adyacencias:
                self.adyacencias[v] = {}
            self.adyacencias[v][u] = peso

    def borrar_arista(self, u, v):
        if u in self.adyacencias and v in self.adyacencias[u]:
            del self.adyacencias[u][v]

    def cambiar_peso(self, u, v, peso):
        if u in self.adyacencias and v in self.adyacencias[u]:
            self.adyacencias[u][v] = peso

    def peso_arista(self, u, v):
        return self.adyacencias[u][v] if u in self.adyacencias and v in self.adyacencias[u] else 0

    def estan_unidos(self, u, v):
        return u in self.adyacencias and v in self.adyacencias[u]

    def adyacentes(self, u):
        return self.adyacencias[u].keys() if u in self.adyacencias else []

    def obtener_vertices(self):
        return self.adyacencias.keys()