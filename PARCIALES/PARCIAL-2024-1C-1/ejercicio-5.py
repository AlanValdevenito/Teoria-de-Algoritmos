# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. 

# Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es fácil tentarse a dar una cota más alta 
# de lo correcto).

# Implementar un algoritmo que permita reconstruir la solución.

# Aclaración: siempre es posible escribir a n como suma de n términos de la forma 1², por lo que siempre existe solución.
# Sin embargo, la expresión 10 = 3² + 1² es una manera más económica de escribirlo para n = 10, pues sólo tiene dos
# términos.

# Ecuacion de recurrencia: OPT(n) = 1 + min(OPT(n-k²)) para todo k² menor o igual a n

# Ejemplo: Consideremos el numero 10.

# OPT(0) = 0
# OPT(1) = 1 + min(OPT(0)) = 1 + 0 = 1 (1²)
# OPT(2) = 1 + min(OPT(1)) = 1 + 1 = 2 (1² + 1²)
# OPT(3) = 1 + min(OPT(2)) = 1 + 2 = 3 (1² + 1² + 1²)
# OPT(4) = 1 + min(OPT(0), OPT(3)) = 1 + 0 = 1 (2²)
# OPT(5) = 1 + min(OPT(1), OPT(4)) = 1 + 1 = 2 (2² + 1²)
# OPT(6) = 1 + min(OPT(2), OPT(5)) = 1 + 2 = 3 (2² + 1² + 1²)
# OPT(7) = 1 + min(OPT(3), OPT(6)) = 1 + 3 = 4 (2² + 1² + 1² + 1²)
# OPT(8) = 1 + min(OPT(4), OPT(7)) = 1 + 1 = 2 (2² + 2²)
# OPT(9) = 1 + min(OPT(0), OPT(1), OPT(8)) = 1 + 0 = 1 (3²)
# OPT(10) = 1 + min(OPT(1), OPT(6), OPT(9)) = 1 + 1 = 2 (3² + 1²)

import math

def suma_cuadrados_dinamico(n):
    mem = [0] * (n+1)

    for i in range(1, n+1):
        cantidades = []

        # for j in range(1, i+1):

        #     if (i - j**2) >= 0:
        #         cantidades.append(mem[i - j**2])

        for j in range(1, int(math.sqrt(i)) + 1):
            cantidades.append(mem[i - j**2])

        mem[i] = 1 + min(cantidades)

    return mem

def suma_cuadrados_solucion(n, mem):
    solucion = []

    while n > 0:
        # opciones = [j for j in range(1, n+1) if (n - j**2) >= 0]
        opciones = [j for j in range(1, int(math.sqrt(n)) + 1)]

        min_opcion = min(opciones, key=lambda num: (mem[n - num**2], num**2))

        solucion.append(min_opcion)
        n -= min_opcion**2

    solucion.reverse()
    return " + ".join(f"{n}²" for n in solucion)

def suma_cuadrados(n):

    mem = suma_cuadrados_dinamico(n)
    solucion = suma_cuadrados_solucion(n, mem)

    return mem[n], solucion

# Complejidad

# Matriz de memorizacion:

# Iteramos desde 1 hasta n lo cual tiene una complejidad de O(n)

# En cada iteracion, para cada valor de i iteramos desde 1 hasta sqrt(i) ya que para valores mayores de sqrt(i) no se cumple la 
# condicion (i >= j**2)

# Luego, la complejidad total resulta ser O(n x sqrt(n)). Es decir O(n^3/2).

# Reconstruccion de la solucion:

# Iteramos mientras n > 0. Es decir, el numero de iteraciones es igual al numero de terminos necesarios para representar n como una suma 
# de cuadrados. En el peor caso la complejidad resulta ser O(sqrt(n)).

# En cada iteracion, se calcula la lista de opciones de cuadrados menores o iguales a n y se selecciona el minimo, lo cual tiene una 
# complejidad O(sqrt(n)) ya que la lista de opciones tiene un tamaño proporcional a O(sqrt(n))

# Luego, la complejidad total resulta ser O(sqrt(n) x sqrt(n)). Es decir O(n).

# Por lo tanto, la complejidad total resulta ser O(n^3/2).

assert suma_cuadrados(1) == (1, "1²")
assert suma_cuadrados(2) == (2, "1² + 1²")
assert suma_cuadrados(3) == (3, "1² + 1² + 1²")
assert suma_cuadrados(4) == (1, "2²")
assert suma_cuadrados(5) == (2, "2² + 1²")
assert suma_cuadrados(6) == (3, "2² + 1² + 1²")
assert suma_cuadrados(7) == (4, "2² + 1² + 1² + 1²")
assert suma_cuadrados(8) == (2, "2² + 2²")
assert suma_cuadrados(9) == (1, "3²")
assert suma_cuadrados(10) == (2, "3² + 1²")