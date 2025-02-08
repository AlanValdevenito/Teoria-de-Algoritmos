# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Independent Set al problema de los Actores: Independent Set $\leq_P$ Actores

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema de los Actores es al menos tan dificil de resolver como el problema de Independent Set. Esto significa que resolver el problema de Independent Set puede ser transformado en resolver el problema de los Actores.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py

# Actores = [A1, A2, A3]

# Obras = {A1: [O1, O2], A2: [O1], A3: [O3]}

# Solucion = [A1, A3] con k = 2

def verificador(actores, obras, k, solucion):
    
    # Validamos que la solucion tenga exactamente k actores
    if len(solucion) != k:
        return False

    # Validamos que los actores que conforman la solucion sean realmente actores
    for a in solucion:

        if a not in actores:
            return False

    # Validamos que los k actores no compartan elenco en otras peliculas
    for a1 in solucion:
        for a2 in solucion:

            if a1 == a2:
                continue

            p1 = set(obras[a1])
            p2 = set(obras[a2])

            # Validamos si hay interseccion en los conjuntos de peliculas
            # Si hay interseccion, entonces compartieron elenco en alguna pelicula previa
            if p1 & p2:
                return False

    return True
```

Complejidad: La complejidad resulta ser O(k² x O) con k la cantidad de actores en la solucion y O la cantidad de obras
- Validar que la solucion tenga exactamente k actores tiene una complejidad de O(1)
- Validar que los actores que conforman la solucion sean realmente actores tiene una complejdiad de O(k) con k la cantidad de actores en la solucion
- Validar que los k actores no compartna elenco en otras peliculas tiene una complejidad de O(k² x O) con k la cantidad de actores en la solucion y O la cantidad de obras

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Independent Set $\leq_P$ Actores.

### Reduccion planteada

¿Podemos resolver el problema de Independent Set utilizando la solucion del problema de Actores?.

Vamos a utilizar una caja negra que resuelve el problema de los problema de Actores para resolver el problema de Independent Set.

El problema de Independent Set recibe un grafo G y un valor $k'$

Transformacion del problema: Transformamos la entrada del problema de Independent Set en una entrada del problema de Actores
- El valor $k'$ del problema de Independent Set se corresponde con el valor $k$ del problema de Actores
- Transformamos los vertices del grafo G en un conjunto de actores. Es decir, cada vertice se corresponde con un actor
- Transformamos cada arista que une dos vertices ($V_i$, $V_j$) en una pelicula en la que compartieron elenco. Es decir, dos grafos unidos por una arista ($V_i$, $V_j$) se corresponderan con dos actores que compartieron elenco en una pelicula.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Independent Set de tamaño exactamente $k'$, si y solo si, hay solucion para el problema de los Actores de tamaño exactamente $k$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Independent Set, entonces hay Actores

Hipotesis: Hay solucion de Independent Set de tamaño exactamente $k'$

Si tenemos solucion de Independent Set de tamaño exactamente $k'$, entonces tenemos un conjunto de $k'$ vertices que no son adyacentes entre si.

Teniendo en cuenta la transformacion propuesta, si cada vertice representa un actor y cada arista que une dos vertices ($V_i$, $V_j$) representa dos actores que compartieron elenco en una pelicula, si nuestro conjunto tiene $k'$ vertices que no son adyacentes entre si, entonces tenemos $k$ actores que no compartieron elenco en una pelicula.

Luego, hay solucion para el problema de los Actores de tamaño exactamente $k$.

### Si hay Actores, entonces hay Independent Set

Hipotesis: Hay solucion para el problema de los Actores de tamaño exactamente $k$

Si tenemos solucion del problema de los Actores de tamaño exactamente $k$, entonces tenemos un conjunto de $k$ actores que no compartieron elenco en una pelicula.

Teniendo en cuenta la transformacion propuesta, si cada actor representa un vertice y nuestro conjunto de $k$ actores no compartieron elenco en una pelicula, entonces tenemos un conjunto de $k'$ vertices que no son adyacentes entre si.

Si tuviesemos un par de vertices adyacentes entre si, esto implicaria que compartieron elenco en una pelicula ya que cada arista que une dos vertices representa esto. Luego, eso es absurdo ya que partimos de la hipotesis de que la solucion es correcta.

Luego, hay solucion de Independent Set de tamaño exactamente $k'$.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de los Actores es un problema NP-Completo.