# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de 
# integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran 
# el grupo i, siendo en total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su 
# grupo pueden sentarse. 

# Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras 
# palabras, que dejan la menor cantidad de espacios vacíos). 

# Indicar y justificar la complejidad del algoritmo.

# Devolver una lista con los valores de los grupos a ubicar, en el orden original en el que se encontraban en el vector P.

# ¿Que tipo de problema es?. Es un problema de maximizacion. Buscamos maximizar la cantidad de espacio ocupado en la mesa.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de grupos y la capacidad de la mesa.

# Ejemplo: Consideremos el arreglo P = [10, 7, 5, 13] de grupos y una mesa con capacidad W = 16.

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10], 
#  [0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 10, 10, 10, 10, 10, 10, 10], 
#  [0, 0, 0, 0, 0, 5, 5, 7, 7, 7, 10, 10, 12, 12, 12, 15, 15], 
#  [0, 0, 0, 0, 0, 5, 5, 7, 7, 7, 10, 10, 12, 13, 13, 15, 15]]

# Nota: De forma vertical aumenta la cantidad de grupos y de forma horizontal aumenta la capacidad de la mesa.

# La maxima cantidad de espacio ocupado en la mesa seria 15 ubicando los grupos [10, 5].

# Notemos que este es un problema similar a 'Problema de la mochila', con la particularidad de que en lugar de elementos con peso y valor tenemos grupos.

# Si bien es un problema similar, no existe el concepto de valor de forma explicita. De forma explicita solo existe el concepto de peso, que es el lugar que 
# ocuparia cada grupo. Luego, como queremos maximizar la cantidad de espacio ocupado en la mesa tenemos que el valor coincide el lugar que ocupa cada grupo.

# Luego, podriamos resolver este problema utilizando la misma idea para la ecuacion de recurrencia teniendo en cuenta que el valor coincide con el peso.

# Ecuacion de recurrencia: OPT(i, W) = max(ubicar grupo actual, no ubicar grupo actual) = max(OPT(i-1, W-P[i]) + P[i], OPT(i-1, W)) para i > 0

def bodegon_dinamico_mem(P, W, n):
    mem = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        grupo = P[i-1]
        for j in range(1, W+1):
            
            if (grupo <= j):
                mem[i][j] = max(mem[i-1][j-grupo] + grupo, mem[i-1][j])

            else:
                mem[i][j] = mem[i-1][j]

    return mem

def bodegon_solucion(P, W, mem, n):
    solucion = []

    while (W >= 0 and n > 0):
        
        if (mem[n][W] != mem[n-1][W]):
            solucion.append(P[n-1])
            W -= P[n-1]

        n -= 1

    solucion.reverse()
    return solucion

def bodegon_dinamico(P, W):
    n = len(P)

    mem = bodegon_dinamico_mem(P, W, n)
    return bodegon_solucion(P, W, mem, n)

# Complejidad

# Matriz de memorizacion: Dado que tenemos dos bucles anidados donde para cada grupo iteramos cada capacidad posible la complejidad resulta ser O(P x W) donde P 
# es la cantidad de grupos y W es la capacidad de la mesa.

# Reconstruccion de solucion: Dado que iteramos los grupos la complejidad resulta ser O(P) donde P es la cantidad de grupos.

# La complejidad total resulta ser O(P x W) donde P es la cantidad de grupos y W es la capacidad de la mesa.

assert bodegon_dinamico([6], 12) == [6]
assert bodegon_dinamico([5, 6], 12) == [5, 6]
assert bodegon_dinamico([1, 3], 4) == [1, 3]
assert bodegon_dinamico([10, 7, 5, 13], 16) == [10, 5]

# Nota: En lugar de utilizar la funcion 'bodegon_dinamico_mem' podriamos llamar a la funcion que resuelve el problema de la mochila con la particularidad
# de el valor de cada grupo coincidiria con el lugar que ocupa (peso).