# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Ciclo Hamiltoniano al problema del Hamiltonian Completition: Ciclo Hamiltoniano $\leq_P$ Hamiltonian Completition

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema del Hamiltonian Completition es al menos tan dificil de resolver como el problema de Ciclo Hamiltoniano. Esto significa que resolver el problema de Ciclo Hamiltoniano puede ser transformado en resolver el problema del Hamiltonian Completition.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(grafo, k, grafo_solucion, ciclo_solucion):
    
    # Validamos que el grafo solucion tenga como maximo K aristas nuevas
    aristas_original = set()

    for v in grafo.obtener_vertices():
        for w in grafo.adyacentes(v):

            if (v == w) or ((v,w) in aristas_original)
                continue
            
            if (w,v) not in aristas_original:
                aristas_original.add((v,w))

    aristas_solucion = set()
    
    for v in grafo_solucion.obtener_vertices():
        for w in grafo_solucion.adyacentes(v):

            if (v == w) or ((v,w) in aristas_solucion)
                continue
            
            if (w,v) not in aristas_solucion:
                aristas_solucion.add((v,w))

    if len(aristas_original) + k < len(aristas_solucion):
        return False

    # Validamos que el ciclo Hamiltoniano contenga exactamente los mismos vertices que el grafo original
    if set(grafo.obtener_vertices()) != set(ciclo_solucion):
        return False

    # Validamos que los vertices que conforman la solucion no se repitan y sean un ciclo Hamiltoniano
    visitados = set()

    for v in solucion:
        
        if v not in grafo.obtener_vertices() or v in visitados:
            return False
        
        visitados.add(v)

    # Validamos que los vertices que conforman la solucion esten unidos y sean un ciclo Hamiltoniano
    for i in range(1, len(vertices)):

        v = vertices[i-1]
        w = vertices[i]

        if not grafo.estan_unidos(v, w):
            return False

    primero = ciclo_solucion[0]
    ultimo = ciclo_solucion[-1]

    if not grafo_solucion.estan_unidos(ultimo, primero):
        return False

    return True
```

Complejidad: La complejidad del validador es O(V + E) con V la cantidad de vertices y E la cantidad de aristas.
- Validar que el grafo solucion tenga como maximo K aristas nuevas tiene una complejidad de O(V + E) con V la cantidad de vertices y E la cantidad de aristas ya que debemos recorrer los vertices y sus adyacentes para encontrar las aristas.
- Validar que el ciclo Hamiltoniano contenga exactamente los mismos vertices que el grafo original tiene una complejidad de O(V) con V la cantidad de vertices ya que convertimos la lista a un conjunto.
- Validar que los vertices que conforman la solucion sean un ciclo Hamiltoniano tiene una compplejidad de O(V) con V la cantidad de vertices ya que un ciclo Hamiltoniano es un camino que recorre todos los vertices una vez y el ultimo vertice visitado es adyacente al primero.

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Ciclo Hamiltoniano $\leq_P$ Hamiltonian Completition.

### Reduccion planteada

¿Podemos resolver el problema de Ciclo Hamiltoniano utilizando la solucion del problema Hamiltonian Completition?.

Vamos a utilizar una caja negra que resuelve el problema del problema Hamiltonian Completition para resolver el problema de Ciclo Hamiltoniano.

El problema de Ciclo Hamiltoniano recibe un grafo $G'$.

Transformacion del problema: Transformamos la entrada del problema de Ciclo Hamiltoniano en una entrada del problema Hamiltonian Completition
- El grafo $G'$ del problema de Ciclo Hamiltoniano se corresponde con el grafo $G$ del problema del Hamiltonian Completition.
- El valor de $K$ es cero.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Ciclo Hamiltoniano, si y solo si, hay solucion para el problema del Hamiltonian Completition con a lo sumo $K$ aristas agregadas.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Ciclo Hamiltoniano, entonces hay Hamiltonian Completition

Hipotesis: Hay solucion de Ciclo Hamiltoniano.

Dada nuestra hipotesis, existe un camino que recorre todos los vertices una unica vez, donde el primer y ultimo vertice son adyacentes.

Luego, existe un ciclo hamiltoniano, con lo cual hay solucion para el problema de Hamiltonian Completition agregando $K = 0$ aristas.

### Si hay Hamiltonian Completition, entonces hay Ciclo Hamiltoniano

Hipotesis: Hay solucion para el problema del Hamiltonian Completition con a lo sumo $K$ aristas agregadas.

Dada nuestra hipotesis, se agregaron $K=0$ aristas de tal forma que existe un camino que recorre todos los vertices una unica vez, donde el primer y ultimo vertice son adyacentes.

Luego, existe un ciclo hamiltoniano, con lo cual hay solucion para el problema de Ciclo Hamiltoniano.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema del Hamiltonian Completition es un problema NP-Completo.