# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema del casamiento de Antonina se encuentra en NP
- Reducir el problema de Separacion en R cliques al problema del casamiento de Antonina: Separacion en R cliques $\leq_P$ Casamiento de Antonina

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando
la doble implicacion.

La segunda demostracion nos indica que el problema del casamiento de Antonina es al menos tan dificil de resolver
como el problema de Separacion en R cliques. Esto significa que resolver el problema de Separacion en R cliques puede ser
transformado en resolver el problema del casamiento de Antonina.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Validador: Recibe una instancia del problema y una solucion.

```py
def validador(invitados, conocidos, k, solucion):

    # Validamos que el numero de mesas sea igual a K
    if len(solucion) != k:
        return False

    # Validamos que, para cada mesa, todos los integrantes se lleven bien
    for mesa in solucion:
        for invitado1 in mesa:
            for invitado2 in mesa:

                if invitado1 == invitado2:
                    continue

                if (not (invitado1, invitado2) in conocidos) and (not (invitado2, invitado1) in conocidos):
                    return False

    return True
```

Complejidad: Dado que iteramos cada mesa y para cada mesa iteramos en un bucle anidado sus invitados la complejidad resulta ser O(KxI²) donde K se corresponde con la cantidad de mesas e I se corresponde con la cantidad de invitados de cada mesa.

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Separacion en R cliques $\leq_P$ Casamiento de Antonina.

### Reduccion planteada

¿Podemos resolver el problema de Separacion en R cliques utilizando la solucion del problema del casamiento de Antonina?.

Vamos a utilizar una caja negra que resuelve el problema del problema del casamiento de Antonina para resolver el problema de Separacion en R cliques.

El problema de Separacion en R cliques recibe un grafo y un valor $R$.

Transformacion del problema:
- Transformamos cada vertice $V_i$ del grafo en un invitado $I_i$ de la lista de invitados.
- Transformamos cada par de vertices adyacentes $(V_i, V_j)$ en un par de conocidos $(I_i, I_j)$ de la lista de conocidos.
- El valor de $R$ correspondiente al problema de Separacion en R cliques coincide con el valor de $k$ correspondiente al problema del casamiento de Antonina.

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Separacion en R cliques de tamaño a lo sumo $R$, si y solo si, hay solucion para el Casamiento de Antonina de tamaño a lo sumo $k$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Separacion en R cliques, entonces hay Casamiento de Antonina

Hipotesis: Hay solucion de Separacion en R cliques de tamaño a lo sumo $R$.

Dado que la hipotesis es verdadera, entonces tenemos R subgrafos completos por la definicion de clique.

Teniendo en cuenta la transformacion planteada, cada subgrafo representa una mesa de invitados. Por otro lado, dado que cada subgrafo es completo y que cada vertice se corresponde con un invitado, tenemos que en cada mesa todos los integrantes se conocen o se llevan bien con todos.

Luego, si hay Separacion en R cliques, entonces hay Casamiento de Antonina.

### Si hay Casamiento de Antonina, entonces hay Separacion en R cliques

Hipotesis: Hay solucion para el Casamiento de Antonina de tamaño a lo sumo $k$.

Dado que la hipotesis es verdadera, entonces tenemos $k$ mesas donde todos los integrantes se conocen o se llevan bien entre todos.

En el problema de Separacion en R cliques podemos definir que los vertices que componen cada clique, coinciden con los invitados de cada mesa.

Dado que en casa mesa los invitados se conocen o se llevan bien con todos, esto quiere decir que se corresponden con vertices tal que todos se conectan con todos. Es decir, un subgrafo completo.

Luego, si hay Casamiento de Antonina, entonces hay Separacion en R cliques.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema del casamiento de Antonina es un problema NP-Completo.