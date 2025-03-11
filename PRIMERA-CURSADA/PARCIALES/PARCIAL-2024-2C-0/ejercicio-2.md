# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de K-Coloreo al problema de Separación en R Cliques: K-Coloreo $\leq_P$ Separación en R Cliques

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando
la doble implicacion.

La segunda demostracion nos indica que el problema de Separación en R Cliques es al menos tan dificil de resolver
como el problema de K-Coloreo. Esto significa que resolver el problema de K-Coloreo puede ser
transformado en resolver el problema de Separación en R Cliques.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(grafo, r, solucion):

    # Validamos que la cantidad de cliques sea igual a R
    if len(solucion) != r:
        return False

    visitados = set()

    # Validamos para cada clique que todos sus vertices esten conectados entre si
    for clique in solucion:
        for v in clique:

            if v in visitados:
                return False

            for w in clique:

                if v == w:
                    continue

                if (v not in grafo.obtener_vertices()) or (w not in grafo.obtener_vertices()):
                    return False

                if not grafo.estan_unidos(v, w):
                    return False

            visitados.add(v)

    return True
```

Complejidad: Iteramos cada clique y en cada iteracion iteramos sus vertices mediante un bucle anidado. Esto resulta en una complejidad 
de O(RxV²) donde R se corresponde con la cantidad de cliques y V se corresponde con la cantidad de vertices de cada clique.

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que K-Coloreo $\leq_P$ Separación en R Cliques.

### Reduccion planteada

¿Podemos resolver el problema de K-Coloreo utilizando la solucion del problema de Separación en R Cliques?.

Vamos a utilizar una caja negra que resuelve el problema del problema de Separación en R Cliques para resolver el problema de K-Coloreo.

El problema de K-Coloreo recibe un grafo y un valor $K$.

Transformacion del problema: Transformamos la entrada del problema de K-Coloreo en una entrada del problema de Separación en R Cliques
- El valor de $K$ correspondiente al problema de K-Coloreo se corresponde con el valor de $R$ correspondiente al problema de Separacion en R Cliques
- Creamos el grafo $G'$ complementario al grafo $G$ correspondiente al problema de K-Coloreo

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de K-Coloreo de tamaño a lo sumo $K$, si y solo si, hay solucion para el problema de Separación en R Cliques de tamaño a lo sumo $R$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay K-Coloreo, entonces hay Separación en R Cliques

Hipotesis: Hay solucion de K-Coloreo de tamaño a lo sumo $K$ en $G$.

Si el grafo G es K-coloreable, entonces los vertices pueden dividirse en K conjuntos, donde ningun conjunto posee vertices adyacentes.

En el grafo complemento $G'$ esto implica que cada uno de estos K conjuntos es un clique, ya que como en G no poseen vertices adyacentes,
entonces en $G'$ estaran todos conectados entre si.

Por lo tanto, hay Separacion en R Cliques en $G'$.

### Si hay Separación en R Cliques, entonces hay K-Coloreo

Hipotesis: Hay solucion para el problema de Separación en R Cliques de tamaño a lo sumo $R$ en $G'$.

Si el grafo $G'$ tiene R cliques, entonces tenemos R conjuntos donde todos sus vertices se conectan entre si.

En el grafo complemento G esto implica que cada uno de estos R conjuntos son disjuntos, es decir que ninguno posee vertices adyacentes.

Por lo tanto, hay K-Coloreo en G.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de Separación en R Cliques es un problema NP-Completo.