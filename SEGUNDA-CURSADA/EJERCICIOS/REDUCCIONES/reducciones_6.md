# Enunciado

Definir el problema de decisión de las N-Reinas. Usar que N-Reinas es un problema NP-Completo para demostrar que Independent Set es un problema NP-Completo.

Problema de decision N-Reinas: Dado un tablero de ajedrez $n×n$, ¿es posible ubicar al menos $n$ reinas de tal manera que ninguna pueda comerse con ninguna?.

Problema de decision Independent Set: Dado un grafo no dirigido, ¿es posible obtener un conjunto de al menos k vertices que representen un Independent Set?.

# Demostracion

Para demostrar que el problema de Independent Set es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de N-Reinas al problema del Independent Set: N-Reinas $\leq_P$ Independent Set

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema de Independent Set es al menos tan dificil de resolver como el problema de N-Reinas. Esto significa que resolver el problema de N-Reinas puede ser transformado en resolver el problema de Independent Set.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(grafo, k, solucion):
    
    # Validamos que la solucion tenga al menos k vertices
    if len(solucion) < k: return False

    vertices = set(grafo.obtener_vertices())

    # Validamos que los vertices de la solucion pertenezcan al grafo
    for v in solucion:
        if v not in vertices: return False

    # Validamos que los vertices de la solucion no esten unidos por una arista
    # Es decir, que la solucion sea efectivamente un Independent Set
    for v in solucion:
        for w in solucion:

            if v == w: continue

            if grafo.estan_unidos(v, w): return False

    return True
```

Complejidad: La complejidad resulta ser O(V²) con V la cantidad de vertices debido a que...
- Validar si la solucion tiene al menos k vertices cuesta O(1)
- Convertir los vertices en un conjunto cuesta O(V) con V la cantidad de vertices
- Validar que los vertices de la solucion pertenezcan al grafo cuesta O(V) con V la cantidad de vertces
- Validar que los vertices de la solucion no esten unidos por una arista cuesta O(V²) con V la cantidad de vertices

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que N-Reinas $\leq_P$ Independent Set.

### Reduccion planteada

¿Podemos resolver el problema de N-Reinas utilizando la solucion del problema de Independent Set?.

Vamos a utilizar una caja negra que resuelve el problema de Independent Set para resolver el problema de N-Reinas.

El problema de N-Reinas recibe un valor $n$.

Transformacion del problema: Transformamos la entrada del problema de N-Reinas en una entrada del problema de Independent Set
- Creamos un grafo $G$ con un total de $nxn$ vertices
- Unimos el vertice $V_i$ con el vertice $V_j$ solamente si se encuentran en la misma fila, misma columna o misma diagonal del tablero de ajedrez
- El valor de $n$ en el problema de N-Reinas coincide con el valor de $k$ en el problema de Independent Set

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de N-Reinas de tamaño al menos $n$, si y solo si, hay solucion para el problema de Independent Set de tamaño al menos $k$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay N-Reinas, entonces hay Independent Set

Hipotesis: Hay solucion de N-Reinas de tamaño al menos $n$
Tesis: Hay solucion para el problema de Independent Set de tamaño al menos $k$

Cada reina esta colocada en una celda del tablero y cada celda del tablero corresponde a un vertice en el grafo G.

Como ninguna reina ataca a otra, entonces no hay arista entre los vertices correspondientes en G, ya que las aristas se construyeron
precisamente cuando dos celdas estan en la misma fila, columna o diagonal.

Por lo tanto, el conjunto de vertices correspondientes a esas $n$ reinas forma un Independent Set de tamaño $n$ en G.

Luego, como $n = k$ tenemos que si hay solucion de N-Reinas, entonces hay solucion de Independent Set.

### Si hay Independent Set, entonces hay N-Reinas

Hipotesis: Hay solucion para el problema de Independent Set de tamaño al menos $k$
Tesis: Hay solucion de N-Reinas de tamaño al menos $n$

El conjunto solucion de Independent Set en G corresponde a $n$ celdas del tablero donde no hay ataques entre ellas porque no hay aristas entre los vertices, lo que significa que las celdas no comparten fila, columna, ni diagonal.

Colocamos una reina en cada una de estas celdas.

Como las celdas no se atacan entre si por construccion del grafo, esta configuracion de reinas es valida.

Luego, como $n = k$ tenemos que si hay solucion de Independent Set, entonces hay solucion de N-Reinas.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de Independent Set es un problema NP-Completo.