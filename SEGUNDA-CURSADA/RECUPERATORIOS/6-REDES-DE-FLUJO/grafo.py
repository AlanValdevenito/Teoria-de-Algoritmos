class Grafo:
    def __init__(self, dirigido=True, vertices=None):
        self.dirigido = dirigido
        self.adyacencias = {}
        if vertices:
            for v in vertices:
                self.adyacencias[v] = {}

    def agregar_vertice(self, v):
        self.adyacencias[v] = self.adyacencias.get(v, {})

    def borrar_vertice(self, v): 

        if self.pertenece_vertice(v):
            del self.adyacencias[v]

            for w in self.obtener_vertices():
                if v in self.adyacencias[w]:
                    del self.adyacencias[w][v]

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
    
    def pertenece_vertice(self, v):
        return v in self.vertices

    def __str__(self):
        cadena = ""

        for v in self.adyacencias:
            adyacentes = self.adyacentes(v)
            cadena += (f"{v} → {adyacentes}\n")

        return cadena[:-1]