# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema de Subgrafo Isomórfico se encuentra en NP
- Reducir el problema de K-Clique al problema de Subgrafo Isomórfico: K-Clique $\leq_P$ Subgrafo Isomórfico

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando
la doble implicacion.

La segunda demostracion nos indica que el problema de Subgrafo Isomórfico es al menos tan dificil de resolver
como el problema de K-Clique. Esto significa que resolver el problema de K-Clique puede ser
transformado en resolver Subgrafo Isomórfico.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Validador: Recibimos el grafo G1, el grafo G2 y el subgrafo de G1 que es isomorfo a G2. Iteramos los vertices de ambos grafos y en cada iteracion validamos con una funcion auxiliar si los vertices son isomorfos y que posean las mismas conexiones.

```py
def validador(g_1, g_2, g_isomorfo):

    # Validamos que G2 y el subgrafo de G1 que es isomorfo a G2 tengan la misma cantidad de vertices
    if len(g_2.obtener_vertices()) != len(g_isomorfo.obtener_vertices()):
        return False

    for v_2 in g_2.obtener_vertices():

        v_isomorfo = obtener_isomorfismo(v_2)

        # Validamos que cada vertices de G2 tenga su vertice isomorfo correspondiente en el subgrafo de G1 que es isomorfo a G2
        if not g_isomorfo.pertece_vertice(v_isomorfo):
            return False

        for w_2 in g_2.adyacentes(v_2):

            W_isomorfo = obtener_isomorfismo(W_2)

            # Validamos para cada vertice de G2 que cada uno de sus adyacentes tenga su vertice isomorfo correspondiente en el subgrafo de G1 que es isomorfo a G2
            if not g_isomorfo.pertece_vertice(W_isomorfo):
                return False

            # Validamos que existan las mismas aritas en ambos grafos
            if not g_isomorfo.estan_unidos(v_isomorfo, w_isomorfo):
                return False
    
    return True
```

Complejidad: Dado que iteramos los vertices y aristas de G2 la complejidad resulta ser O(V+E).

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que K-Clique $\leq_P$ Subgrafo Isomorfico.

### Reduccion planteada

¿Podemos resolver el problema de K-Clique utilizando la solucion de Subgrafo Isomorfico?.

Vamos a utilizar una caja negra que resuelve el problema de Subgrafo Isomorfico para resolver el problema de K-Clique.

El problema de K-Clique recibe un grafo y un valor $k$.

Transformacion del problema:
- El grafo que recibe el problema de K-Clique se corresponde con G1.
- Contruimos un grafo completo de $k$ vertices, siendo $k$ el valor que recibe el problema de K-Clique, el cual se corresponde con G2.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay K-Clique, entonces hay Subgrafo Isomorfico

Hipotesis: Dado un grafo G, existe un subgrafo completo de tamaño $k$.

El conjunto de $k$ vertices conforman un subgrafo completo, por definicion de clique.

Este subgrafo resulta ser isomorfo al grafo $G_k$ correspondiente al problema del Subgrafo Isomorfico.

Luego, si existe un K-Clique en G, existe un subgrafo en G isomorfo a $G_k$, resolviendo el problema
del Subgrafo Isomorfico.

### Si hay Subgrafo Isomorfico, entonces hay K-Clique

Hipotesis: Dado un grafo G1 y otro grafo $G_k$, existe un subgrafo de G1 que es isomorfo a $G_k$.

Por definicion de isomorfismo, el subgrafo de G1 tiene $k$ vertices y todas sus aristas estan presentes en el subgrafo.

Esto implica que cada par de vertices en el subgrafo esta conectado por una arista, lo que define un clique en G1.

Luego, si existe un subgrafo isomorfo a $G_k$, entonces el conjunto de $k$ vertices correspondientes forman un K-Clique en G1.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema
de Subgrafo Isomorfico es un problema NP-Completo.