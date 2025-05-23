# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar toda una calle en un barrio privado, que tiene 
# la particularidad de ser circular. 

# Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa 0, 
# de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. Toda casa se considera 
# adyacente a las casas i-1 e i+1. Además, como la calle es circular, la casas 0 y n-1 también son vecinas. El problema con el que cuenta el Lunático es que 
# sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. 

# No le daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. El Lunático nos encarga 
# saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar 
# el óptimo a este problema. 

# Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a partir de recibir un arreglo de 
# las ganancias obtenibles. 

# Para esto, escribir y describir la ecuación de recurrencia correspondiente. 

# Indicar y justificar la complejidad del algoritmo propuesto.

# Devolver una lista con las posiciones de las casas a robar.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de casas a robar.

# Ejemplo: Consideremos el arreglo [100, 20, 30, 70, 50, 5] de ganancias.

# OPT([]) = 0
# OPT([100]) = [100] 
# OPT([100, 20]) = [100]
# OPT([100, 20, 30]) = [100]
# OPT([100, 20, 30, 70]) = [100, 30]
# OPT([100, 20, 30, 70, 50]) = [100, 50]
# OPT([100, 20, 30, 70, 50, 5]) = [100, 30, 50]

# La ganancia maxima obtenible seria 180 robando las casas [0, 2, 4].

# Notemos que este es un problema similar a 'Juan el Vago' que a su vez es similar a un problema de 'Scheduling con pesos', con la particularidad de que en 
# lugar de dias tenemos casas y la casas 0 y n-1 son vecinas.

# Luego, podriamos resolver este problema utilizando la misma idea para la ecuacion de recurrencia y para manejar el aspecto circular podemos dividir el 
# problema en dos subproblemas:
# - Considerar robar desde la casa 0 hasta la casa n-2 (excluimos la ultima)
# - Considerar robar desde la casa 1 hasta la casa n-1 (excluimos la primera)

# De esta forma garantizamos que no se violen las restricciones de robo en casas adyacentes para la primera y ultima casa.

# Ecuacion de recurrencia: OPT(i) = max(robar la casa actual, no robar la casa actual) = max(OPT[i-2] + gi, OPT(i-1)) con i >= 2

# Casos base:
# - Si tenemos 0 casas, entonces el OPT sera 0
# - Si tenemos 1 casa, entonces el OPT sera la ganancia de la casa
# - Si tenemos 2 casas, entonces el OPT sera la ganancia maxima entre las 2 casas

def lunatico_dinamico(ganancias, n):
    mem = [0] * (n)

    mem[0] = ganancias[0]
    mem[1] = max(ganancias[0], ganancias[1])

    for i in range(2, n):
        mem[i] = max(mem[i-2] + ganancias[i], mem[i-1])

    return mem

def lunatico_solucion(ganancias, mem, n):
    solucion = []

    while (n >= 0):
        robar_actual = (mem[n-2] if n > 1 else 0) + ganancias[n]
        no_robar_actual = mem[n-1] if n > 0 else 0

        if robar_actual > no_robar_actual:
            solucion.append(n)
            n -= 2

        else:
            n -= 1

    solucion.reverse()
    return solucion

def lunatico(ganancias):
    n = len(ganancias)

    if (n == 0): return (0, [])

    if (n == 1): return (ganancias[0], [0])

    if (n == 2): return (max(ganancias[0], ganancias[1]), [0 if ganancias[0] > ganancias[1] else 1])

    mem1 = lunatico_dinamico(ganancias[:-1], n-1)
    mem2 = lunatico_dinamico(ganancias[1:], n-1)

    if mem1[n-2] > mem2[n-2]:
        solucion = lunatico_solucion(ganancias[:-1], mem1, n-2)
        return (mem1[n-2], solucion)

    solucion = lunatico_solucion(ganancias[1:], mem2, n-2)
    solucion = [i + 1 for i in solucion] # Ajustamos los indices
    return (mem2[n-2], solucion)

# Complejidad

# Matriz de memorizacion: Dado que iteramos las casas la complejidad resulta ser O(n) donde n es la cantidad de casas.

# Reconstruccion de solucion: Dado que iteramos las casas la complejidad resulta ser O(n) donde n es la cantidad de casas.

# La complejidad total resulta ser O(n) donde n es la cantidad de casas.

assert lunatico([]) == (0, [])
assert lunatico([100]) == (100, [0])
assert lunatico([100, 20]) == (100, [0])
assert lunatico([100, 20, 30]) == (100, [0])
assert lunatico([60, 100, 60]) == (100, [1])
assert lunatico([100, 20, 30, 70, 50, 5]) == (180, [0, 2, 4])
assert lunatico([100, 20, 30, 70, 50]) == (170, [0, 3])

# Nota: En lugar de utilizar la funcion 'lunatico_dinamico' podriamos llamar dos veces a la funcion que resuelve el problema de Juan el Vago
# - El primer llamado sin el primer elemento.
# - El segundo llamado sin el ultimo elemento.

# Luego, entre las dos soluciones obtenidas elegimos aquella cuyo ultimo elemento sea mayor y a esta le aplicamos la reconstruccion para obtener la solucion.