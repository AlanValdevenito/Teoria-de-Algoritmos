# Enunciado

El Hitting-Set Problem se define de la siguiente forma: Dado un conjunto de elemento A de n elementos, m subconjuntos $B_1,B_2,...,B_m​$ de A ($B_i$ ⊆ A ∀i), y un número k, ¿existe un subconjunto $C$ ⊆ $A$ con $∣C∣ ≤ k$ tal que C tenga al menos un elemento de cada $B_i$​ (es decir, C ∩ $B_i$ ≠ ∅ ∀i)?

Demostrar que el Hitting-Set Problem es un problema NP-Completo.

Utilizaremos el problema de Dominating-Set para la demostracion.

Problema de decision Dominating-Set: Dado un grafo G, ¿es posible obtener un conjunto de a lo sumo $n$ vertices que representen un Dominating-Set?.

Un set dominante (Dominating-Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D.

# Demostracion

Para demostrar que el problema de Hitting-Set es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Dominating-Set al problema de Hitting-Set: Dominating-Set  $\leq_P$ Hitting-Set

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema de Dominating-Set es al menos tan dificil de resolver como el problema de Hitting-Set. Esto significa que resolver el problema de Dominating-Set puede ser transformado en resolver el problema de Hitting-Set.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(subconjunto_A, subconjuntos_B, k, solucion_C):
    
    # Validamos que el subconjunto C tenga a lo sumo k elementos
    if len(solucion_C) > k: return False

    subconjunto_A = set(subconjunto_A)

    # Validamos que todos los elementos de C se encuentren en A
    for elem in solucion_C:
        if elem not in subconjunto_A: return False

    subconjuntos_B = set(subconjuntos_B)

   # Validamos que C tenga al menos un elemento de cada subconjunto en B
   for elem in solucion_C:
        interseccion = False

        for conjunto in subconjuntos_B:
            if elem in conjunto:
                interseccion = True
                break

        if not interseccion: return False
    
    return True
```

Complejidad: La complejidad resulta ser O(k x B) con k la cantidad de elementos en C y B la cantidad de subconjuntos en B
- Validar si la solucion tiene a lo sumo k vertices cuesta O(1)
- Validar que todos los elementos de C se encuentran en A cuesta O(k) con k la cantidad de elementos en C
- Validar que C tenga al menos un elemento de cada subconjunto en B cuesta O(k x B) con k la cantidad de elementos en C y B la cantidad de subconjuntos en B

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Dominating-Set $\leq_P$ Hitting-set.

### Reduccion planteada

¿Podemos resolver el problema de Dominating-Set utilizando la solucion del problema Hitting-Set?.

Vamos a utilizar una caja negra que resuelve el problema de Hitting-Set para resolver el problema de Dominating-Set.

El problema de Dominating-Set recibe un grafo G y un valor $n$

Transformacion del problema: Transformamos la entrada del problema de Dominating-Set en una entrada del problema Hitting-Set
- Cada vertice $V_i$ perteneciente al grafo $G$ lo transformamos en un elemento del conjunto A
- Cada vertice $V_i$ y sus vertices adyacentes $V_j$ en el grafo $G$ lo transformamos en un subconjunto $B_i$
- El numero $n$ del problema de Dominating Set se corresponde con el numero $k$ del problema de Hitting Set

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Dominating-Set de a lo sumo $n$ vertices, si y solo si, hay solucion para el problema del Hitting-Set de tamaño a lo sumo $k$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Dominating-Set, entonces hay Hitting-Set

Hipotesis: Hay solucion de Dominating-Set de a lo sumo $n$ vertices
Tesis: Hay solucion para el problema del Hitting-Set de tamaño a lo sumo $k$

Como D es un conjunto dominante, para todo vertice se cumple que pertenece a D o bien es adyacente a un vértice en D.

Es decir, tenemos que D ∩ $B_i$ ≠ ∅ para todo $i$ donde $B_i$ es el subconjunto que contiene al vertice $V_i$ y sus adyacentes.

Luego, como $n = k$ y como D cumple la definicion de ser un Hitting-Set tenemos que si hay solucion de Dominating-Set, entonces hay solucion de Hitting-Set.

### Si hay Hitting-Set, entonces hay Dominating-Set

Hipotesis: Hay solucion para el problema del Hitting-Set de tamaño a lo sumo $k$
Tesis: Hay solucion de Dominating-Set de a lo sumo $n$ vertices

Para todo vertice $V_i$ tenemos que el conjunto $B_i$ tiene interseccion no vacia con C.

Esto implica que cada vertice del grafo esta dominado por algun vertice de C, porque para todo vertice se cumple que pertenece a C o bien es adyacente a un vertice en C.

Entonces, tenemos que C es un conjunto dominante.

Luego, como $k = n$ tenemos que si hay solucion de Hitting-Set, entonces hay solucion de Domination-Set.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de Hitting-Set es un problema NP-Completo.