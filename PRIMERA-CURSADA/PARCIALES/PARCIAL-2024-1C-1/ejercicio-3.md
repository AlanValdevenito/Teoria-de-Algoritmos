# Demostracion

Para demostrar que es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Vertex Cover al problema del Cumpleaños de Coty: Vertex Cover $\leq_P$ Cumpleaños de Coty

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando
la doble implicacion.

La segunda demostracion nos indica que el problema del Cumpleaños de Coty es al menos tan dificil de resolver
como el problema de Vertex Cover. Esto significa que resolver el problema de Vertex Cover puede ser
transformado en resolver el problema del Cumpleaños de Coty.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(invitados, k, conocidos, solucion):

    # Validamos que la cantidad k de regalos sea igual o mayor a la cantidad de personas que tienen asignado un regalo
    if (len(solucion) >= k):
        return False

    # Validamos que cada persona que tiene un regalo asignado se encuentre entre los invitados
    for i in solucion:

        if i not in invitados:
            return False

    # Validamos que para cada par de conocidos (c1, c2) al menos uno tenga un regalo asignado
    for c1, c2 in conocidos:

        if (c1 not in solucion) and (c2 not in solucion):
            return False

    return True
```

Complejidad: Iteramos la solucion y en cada iteracion validamos que la persona que tiene asignado un regalo se encuentre en la lista de invitados, con lo cual esto tiene una complejidad de O(k) con k la cantidad de regalos. Iteramos la lista de pares de conocidos y en cada iteacion validamos que al menos uno tenga un regalo asignado, lo cual tiene una complejidad de O(c) con c la cantidad de pares de invitados. Luego, la complejidad total resulta ser O(k + c) donde k es la cantidad de regalos y c es la cantidad de pares de invitados.

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Vertex Cover $\leq_P$ Cumpleaños de Coty.

### Reduccion planteada

¿Podemos resolver el problema de Vertex Cover utilizando la solucion del problema de Cumpleaños de Coty?.

Vamos a utilizar una caja negra que resuelve el problema del problema de Cumpleaños de Coty para resolver el problema de Vertex Cover.

El problema de Vertex Cover recibe un grafo y un valor $k'$.

Transformacion del problema: Transformamos la entrada del problema de Vertex Cover en una entrada del problema de Cumpleaños de Coty
- El valor de $k'$ correspondiente al problema de Vertex Cover se corresponde con el valor de $k$ correspondiente al problema del Cumpleaños de Coty
- Un invitado I por cada vertice V del grafo correspondiente al problema de Vertex Cover
- Un par de invitados conocidos $(I_i, I_j)$ por cada par de vertices $(V_i, V_j)$ unidos por una arista (adyacentes) en el grafo correspondiente al problema de Vertex Cover

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Vertex Cover de tamaño a lo sumo $k'$, si y solo si, hay solucion para el problema del Cumpleaños de Coty de tamaño a lo sumo $k$.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Vertex Cover, entonces hay Cumpleaños de Coty

Hipotesis: Hay solucion de Vertex Cover de tamaño a lo sumo $k'$

Si hay solucion de Vertex Cover de tamaño a lo sumo $k'$, entonces hay $k'$ vertices que cubren todas las aristas del grafo.

Luego, teniendo en cuenta la transformacion planteada, cada invitado se corresponde con un vertice y cada par de conocidos se corresponde con vertices adyacentes.

Es decir, si tenemos $k'$ vertices que cubren todas las aristas del grafo, entonces tenemos $k'$ invitados con un regalo asignado de tal forma que al menos uno de cada par de conocidos tiene asignado un regalo.

Luego, hay solucion para el problema del Cumpleaños de Coty de tamaño a lo sumo $k$.

### Si hay Cumpleaños de Coty, entonces hay Vertex Cover

Hipotesis: Hay solucion para el problema del Cumpleaños de Coty de tamaño a lo sumo $k$

Si hay solucion para el problema del Cumpleaños de Coty de tamaño a lo sumo $k$, entonces hay $k$ invitados con un regalo asignado de tal forma que para los pares de conocidos al menos uno de ellos tiene un regalo asignado.

Luego, teniendo en cuenta la transformacion planteada, cada invitado se corresponde con un vertice y cada par de conocidos se corresponde con vertices adyacentes.

Es decir, si tenemos $k$ invitados con un regalo asignado de tal forma que para los pares de conocidos al menos uno de ellos tiene un regalo asignado, entonces tenemos $k'$ vertices que cubren todas las aristas del grafo.

¿Por que?. Porque cada par de conocidos se creo a partir de los vertices adyacentes del grafo.

Luego, hay solucion de Vertex Cover de tamaño a lo sumo $k'$

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema del Cumpleaños de Coty es un problema NP-Completo.