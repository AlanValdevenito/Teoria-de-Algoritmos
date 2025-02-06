import random

class Grafo:
    '''Representacion de un grafo como lista de adyacencia (diccionarios de diccionarios).'''

    def __init__(self, es_dirigido, vertices_iniciales = None):
        '''Crea un grafo vacío, este puede ser dirigido o no dirigido.'''

        self.es_dirigido = es_dirigido
        self.vertices = {}

        if not vertices_iniciales is None:
            for v in vertices_iniciales:
                self.vertices[v] = self.vertices.get(v, {})

    def agregar_vertice(self, v):
        '''Dado un nuevo vertice v, lo agrega al grafo.
        En caso de que el vertice ya existiera, lo deja tal cual estaba.'''

        self.vertices[v] = self.vertices.get(v, {})

    def borrar_vertice(self, v): 
        '''Dado un vertice v, lo borra del grafo.'''

        if self.pertenece_vertice(v):
            del self.vertices[v]

            for w in self.obtener_vertices():
                if v in self.vertices[w]:
                    del self.vertices[w][v]

    def agregar_arista(self, v, w, peso = 1):
        '''Agrega una nueva arista entre los vertices v y w.
        En caso de ser un grafo no pesado, el peso sera igual a 1.
        El resultado sera v <---> w en el caso de que el grafo sea no dirigido.
        El resultado sera v |---> w en el caso de que el grafo sea dirigido.
        En caso de que alguno de los dos vertices v o w no pertenezcan al grafo, devuelve False.'''
        
        if not self.pertenece_vertice(v) or not self.pertenece_vertice(w):
            return False

        self.vertices[v][w] = peso

        if not self.es_dirigido:
            self.vertices[w][v] = peso

        return True

    def borrar_arista(self, v, w): 
        '''Dados dos vertices v y w, borra la arista entre ellos en caso de que esten unidos.'''

        if self.estan_unidos(v, w):
            if v in self.vertices[w]:
                del self.vertices[w][v]

            if w in self.vertices[v]:
                del self.vertices[v][w]

    def estan_unidos(self, v, w):
        '''Dado dos vertices v y w, devuelve True si se puede ir de v a w (es decir, si estan unidos).
        En caso contrario devuelve False.'''
        
        if not self.pertenece_vertice(v) or not self.pertenece_vertice(w):
            return False

        if w in self.vertices[v]:
            return True

        return False

    def peso_arista(self, v, w):
        '''Dados dos vertices v y w, devuelve el peso que tiene la arista que los une.
        Estaran unidos si existe una arista (camino) de v hacia w.
		Devuelve None en caso de que los vertices no esten unidos.'''

        if self.estan_unidos(v, w):
            return self.vertices[v][w]

        return None

    def obtener_vertices(self):
        '''Devuelve una lista con todos los vertices del grafo.
        En caso de que el grafo este vacio, devuelve una lista vacia.'''

        resultado = []

        for v in self.vertices:
            resultado.append(v)

        return resultado

    def vertice_aleatorio(self):
        '''Devuelve un vertice aleatorio.'''

        return random.choice(self.obtener_vertices())

    def adyacentes(self, v):
        '''Dado un vertice v, devuelve una lista con todos los adyacentes de v en el grafo.
        En caso de que el vertice v no tenga adyacentes, devuelve una lista vacia.
        En caso de que el vertice v no se encuentre en el grafo, devuelve None.'''

        if not self.pertenece_vertice(v):
            return None
        
        resultado = []

        for w in self.vertices[v]:
            resultado.append(w)

        return resultado
        
    def pertenece_vertice(self, v):
        '''Dado un vertive c, devuelve True si el vertice pertenece al grafo.
        En caso contrario devuelve False.'''

        return v in self.vertices

    def __str__(self):
        '''Devuelve una cadena que represante el grafo como listas de adyacencia.'''

        cadena = ""

        for v in self.vertices:
            adyacentes = self.adyacentes(v)
            cadena += (f"{v} → {adyacentes}\n")

        return cadena[:-1]