# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Dominating Set al problema del Hitting Set: Dominating Set $\leq_P$ Hitting Set

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema del Hitting Set es al menos tan dificil de resolver como el problema de Dominating Set. Esto significa que resolver el problema de Dominating Set puede ser transformado en resolver el problema del Hitting Set.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(conjunto, subconjuntos, k, solucion):
    
    if len(solucion) > k:
        return False

    for e in solucion:

        if e not in conjunto:
            return False

    for s in subconjuntos:
        interseccion = False

        for e in solucion:

            if e in s:
                interseccion = True
                break

        if not interseccion:
            return False

    return True
```

Complejidad: La complejidad resulta ser O(s x e) siendo s la cantidad de subconjuntos y e la cantidad de elementos de la solucion
- Validar el tamaño de la solucion tiene una complejidad de O(1)
- Validar que cada elemento de la solucion este en el conjunto tiene una complejidad de O(e) siendo e la cantidad de elementos de la solucion
- Validar que el conjunto solucion intersecte a todos los subconjuntos tiene una complejidad de O(s x e) siendo s la cantidad de subconjuntos y e la cantidad de elementos de la solucion

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Dominating Set $\leq_P$ Hitting Set.

### Reduccion planteada

¿Podemos resolver el problema de Dominating Set utilizando la solucion del problema Hitting Set?.

Proponemos el siguiente ejemplo para el problema de Hitting Set:
- U = {1,2,3,4,5}
- S = {{1,2,3}, {2,4}, {3,5}}
- k = 2

Un conjunto de interseccion valido es H = {2,3}.

¿Como se relaciona con el problema de Dominating Set?. En el problema de Dominating Set podriamos considerar que los vertices del grafo son los elementos de H, las aritas estan dadas por los subconjuntos de S y el tamaño de la solucion esta dado por el valor de k. Es decir, el conjunto dominante seria H.

Vamos a utilizar una caja negra que resuelve el problema del problema Hitting Set para resolver el problema de Dominating Set.

El problema de Dominating Set recibe un grafo G y un numero $k$.

Transformacion del problema: Transformamos la entrada del problema de Dominating Set en una entrada del problema Hitting Set.
- El numero $k$ del problema de Dominating Set se corresponde con el numero $k'$ del problema de Hitting Set.
- Transformamos cada vertice del grafo en un elemento del conjunto U.
- Transformamos cada uno de los vertices que estan unidos en subconjuntos de S.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Dominating Set de a lo sumo tamaño $k$, si y solo si, hay solucion para el problema del Hitting Set de a lo sumo tamaño $k'$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Dominating Set, entonces hay Hitting Set

Hipotesis: Hay solucion de Dominating Set de a lo sumo tamaño $k$.

Si hay solucion de Dominating Set de a lo sumo tamaño $k$, entonces tenemos a lo sumo $k$ vertices que forman un subconjunto D de vertices de G al que todo vértice de G pertenece a D o es adyacente a un vértice en D. Es decir, los vertices que forman el subconjunto D cubren todos los vertices del grafo G.

Si pensamos a los vertices que son adyacentes como subconjuntos, entonces el conjunto D interseca a cada uno de estos subconjuntos.

Luego, hay solucion de Hitting Set de a lo sumo tamaño $k'$.

### Si hay X, entonces hay Y

Hipotesis: Hay solucion para el problema del Hitting Set de a lo sumo tamaño $k'$.

Si hay solucion de Hitting Set de a lo sumo tamaño $k'$, entonces tenemos un conjunto H de tamaño a lo sumo $k'$ que interseca a todos los subconjuntos de S.

Si pensamos a los elementos de cada subconjunto de S como vertices que se encuentran unidos por aristas, entonces el conjunto H dominaria a cada uno de los vertices del grafo.

Luego, hay solucion de Dominating Set de a lo sumo tamaño $k$.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema del Hitting Set es un problema NP-Completo.