# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. 

# Decidió en este caso robar toda una calle en un barrio privado, que tiene la particularidad de ser circular. 

# Gracias a los trabajos de inteligencia realizados, sabemos cuánto se puede obtener por robar en cada casa. 

# Podemos enumerar a la primer casa como la casa 0, de la cual podríamos obtener g0, la casa a su derecha es 
# la 1, que nos daría g1, y así hasta llegar a la casa n-1, que nos daría gn-1. 

# Toda casa se considera adyacente a las casas i-1 e i+1. 

# Además, como la calle es circular, la casas 0 y n-1 también son vecinas. 

# El problema con el que cuenta el Lunático es que sabe de experiencias anteriores que, si roba en una 
# casa, los vecinos directos se enterarían muy rápido. No le daría tiempo a luego intentar robarles a ellos. 
# Es decir, para robar una casa debe prescindir de robarle a sus vecinos directos. 

# El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. 
# Dado que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. 

# Implementar un algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles
# casas habría que robar, a partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir 
# y describir la ecuación de recurrencia correspondiente.

# Indicar y justificar la complejidad del algoritmo propuesto.

# Notemos que este es un problema similar a 'Juan el Vago' que a su vez es similar a un problema de Scheduling con pesos.

# Ejemplo: Consideremos el arreglo [100, 20, 30, 70, 50, 5] de ganancias. La ganancia maxima obtenible seria 180 atracando
#          las casas [0, 2, 4].

# OPT(0) = 0
# OPT(1) = 100
# OPT(1) = max{robar la casa, no robar la casa} = max{0+20, 100} = 100
# OPT(3) = max{robar la casa, no robar la casa} = max{100+30, 100} = 130
# OPT(4) = max{robar la casa, no robar la casa} = max{70+100, 130} = 170
# OPT(5) = max{robar la casa, no robar la casa} = max{130+50, 170} = 180
# OPT(6) = max{robar la casa, no robar la casa} = max{5+170, 180} = 180

# Para manejar el aspecto circular podemos dividir el problema en dos subproblemas separados:
# - Considerar robar desde la casa 0 hasta la casa n-2 (excluimos la ultima)
# - Considerar robar desde la casa 1 hasta la casa n-1 (excluimos la primera)

# De esta forma garantizamos que no se violen las restricciones de robo en casas adyacentes 
# para la primera y ultima casa.

# Ecuacion de recurrencia: OPT(i) = max{robar la casa, no robar la casa} = max{OPT(i-2) + gi, OPT(i-1)} para i >=2.

def lunatico_dinamico(ganancias, n):
    mem = [0] * (n)
    mem[0] = ganancias[0]
    mem[1] = max(ganancias[0], ganancias[1])

    for i in range(2, n):
        mem[i] = max(ganancias[i] + mem[i-2], mem[i-1])

    return mem

def lunatico_solucion(mem, ganancias, c):
    solucion = []

    while (c >= 0):
        robar = (mem[c-2] if c > 1 else 0) + ganancias[c]
        no_robar = mem[c-1] if c > 0 else 0

        if (robar >= no_robar):
            solucion.append(c)
            c -= 2
        else:
            c -= 1

    solucion.reverse()
    return solucion

def lunatico(ganancias):
    n = len(ganancias)

    if n == 0:
        return (0, [])
    
    if n == 1:
        return (ganancias[0], [0])
    
    if n == 2:
        return (ganancias[0], [0]) if (ganancias[0] >= ganancias[1]) else (ganancias[1], [1])

    mem1 = lunatico_dinamico(ganancias[:-1], n-1)
    mem2 = lunatico_dinamico(ganancias[1:], n-1)

    # Vemos el ultimo resultado ya que alli se encuentra la mayor ganancia.
    if mem1[n-2] > mem2[n-2]:
        solucion = lunatico_solucion(mem1, ganancias[:-1], n-2)
        return (mem1[n-2], solucion)

    solucion = lunatico_solucion(mem2, ganancias[1:], n-2)
    solucion = [x + 1 for x in solucion] # Ajustamos los indices
    return (mem2[n-2], solucion)

# Complejidad: Tenemos O(n) por calcular la matriz de memorizacion y O(n) por recuperar la solucion. Luego, la 
# complejidad total es O(n).

assert lunatico([]) == (0, [])
assert lunatico([100]) == (100, [0])
assert lunatico([100, 20]) == (100, [0])
assert lunatico([100, 20, 30]) == (100, [0])
assert lunatico([60, 100, 60]) == (100, [1])
assert lunatico([100, 20, 30, 70, 50, 5]) == (180, [0, 2, 4])
assert lunatico([100, 20, 30, 70, 50]) == (170, [0, 3])