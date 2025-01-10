# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Ciclo Hamiltoniano al problema de K-Ciclo: Ciclo Hamiltoniano $\leq_P$ K-Ciclo

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando
la doble implicacion.

La segunda demostracion nos indica que el problema de K-Ciclo es al menos tan dificil de resolver
como el problema de Ciclo Hamiltoniano. Esto significa que resolver el problema de Ciclo Hamiltoniano puede ser
transformado en resolver el problema de K-Ciclo.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(grafo, k, solucion):
    
    # Validamos que la solucion tenga al menos k vertices
    if len(solucion) < k:
        return False

    # Validamos que los vertices esten unidos
    for i in range(1, len(vertices)):

        v = vertices[i-1]
        w = vertices[i]

        if not grafo.estan_unidos(v, w):
            return False

    v = vertices[0] # Primer vertice
    w = vertices[-1] # Ultimo vertice

    # Validamos que el primer vertice y el ultimo vertice esten unidos de tal forma que el conjunto solucion sea un ciclo
    if not grafo.estan_unidos(v, w):
        return False

    return True
```

Complejidad: Se recorre el conjunto de vertices con lo cual la complejidad del verificador es O(V).

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Ciclo Hamiltoniano $\leq_P$ K-Ciclo.

### Reduccion planteada

¿Podemos resolver el problema de Ciclo Hamiltoniano utilizando la solucion del problema de K-Ciclo?.

Vamos a utilizar una caja negra que resuelve el problema del problema de K-Ciclo para resolver el problema de Ciclo Hamiltoniano.

Ciclo hamiltoniano: Camino que visita todos los vertices del grafo una unica vez, donde el primer y ultimo vertice son adyacentes.

El problema de Ciclo Hamiltoniano recibe un grafo y un valor $k$.

Transformacion del problema: Transformamos la entrada del problema de Ciclo Hamiltoniano en una entrada del problema de K-Ciclo
- Crear un grafo G' a partir del grafo G correspondiente al problema de Ciclo Hamiltoniano con exactamente $k$ vertices.
- El valor de $k$ correspondiente al problema de Ciclo Hamiltoniano coincide con el valor de $k'$ correspondiente al problema de K-Ciclo.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion para el problema de Ciclo Hamiltoniano de tamaño a lo sumo $k$, si y solo si, hay solucion para el problema de K-Ciclo de tamaño a lo sumo $k'$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Ciclo Hamiltoniano, entonces hay K-Ciclo

Hipotesis: Hay solucion para el problema de Ciclo Hamiltoniano de tamaño a lo sumo $k$ vertices.

Existe un camino que visita todos los $k$ vertices del grafo una unica vez, donde el primer y ultimo vertice son adyacentes.

Luego, existe un ciclo de exactamente $k$ vertices, con lo cual hay solucion para el problema de K-Ciclo de tamaño exactamente $k'$.

### Si hay K-Ciclo, entonces hay Ciclo Hamiltoniano

Hipotesis: Hay solucion para el problema de K-Ciclo de tamaño a lo sumo $k'$ vertices.

Existe un camino que visita $k'$ vertices del grafo, donde el primer y ultimo vertice son adyacentes.

Luego, existe un ciclo de exactamente $k'$ vertices, con lo cual hay solucion para el problema de Ciclo-Hamiltoniano de tamaño exactamente $k$.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de K-Ciclo es un problema NP-Completo.