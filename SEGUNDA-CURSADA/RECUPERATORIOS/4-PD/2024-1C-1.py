# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados, utilizando programación dinámica. 

# Indicar y justificar la complejidad del algoritmo implementado (cuidado con esto, es fácil tentarse a dar una cota más alta de lo correcto). 

# Implementar un algoritmo que permita reconstruir la solución.

# Aclaración: Siempre es posible escribir a n como suma de n términos de la forma 1², por lo que siempre existe solución. Sin embargo, la expresión 10 = 3² + 1²
# es una manera más económica de escribirlo para n = 10, pues sólo tiene dos términos.

# Nota: Este problema es similar al problema del Cambio donde nuestro sistema monetario serian los terminos elevados al cuadrado.

# ¿Que tipo de problema es?. Es un problema de minimizacion.

# ¿Que define si un subproblema es mas grande o pequeño?. El tamaño de n.

# Ejemplo: Consideremos n = 10.

# OPT[0] = 0
# OPT[1] = 1 + min(OPT[0]) = 1 + 0 = 1 (1²)
# OPT[2] = 1 + min(OPT[1]) = 1 + 1 = 2 (1² + 1²)
# OPT[3] = 1 + min(OPT[2]) = 1 + 2 = 3 (1² + 1² + 1²)
# OPT[4] = 1 + min(OPT[0], OPT[3]) = 1 + 0 = 1 (2²)
# OPT[5] = 1 + min(OPT[1], OPT[4]) = 1 + 1 = 2 (2² + 1²)
# OPT[6] = 1 + min(OPT[2], OPT[5]) = 1 + 2 = 3 (2² + 1² + 1²)
# OPT[7] = 1 + min(OPT[3], OPT[6]) = 1 + 3 = 4 (2² + 1² + 1² + 1²)
# OPT[8] = 1 + min(OPT[4], OPT[7]) = 1 + 1 = 2 (2² + 2²)
# OPT[9] = 1 + min(OPT[0], OPT[1], OPT[8]) = 1 + 0 = 1 (3²)
# OPT[1]) = 1 + min(OPT[1], OPT[6], OPT[9]) = 1 + 1 = 2 (3² + 1²)

# ¿Como se componen estos subproblemas para solucionar subproblemas mas grandes?.

# Ecuacion de recurrencia: OPT[i] = 1 + min(OPT[i-m²]) para todo m² <= i

# Casos base:
# 1) Si n = 0 entonces la cantidad de terminos es 0
# 2) Si n = 1 entonces la cantidad de terminos es 1

def terminos_dinamico(n):
    mem = [0] * (n + 1)

    for i in range(1, n + 1):
        minimo = i

        for termino in range(1, n + 1):

            termino_cuadrado = termino**2

            if (termino_cuadrado > i):
                continue

            cantidad = 1 + mem[i - termino_cuadrado]

            if (cantidad < minimo):
                minimo = cantidad

        mem[i] = minimo

    return mem

def terminos_solucion(mem, n):
    solucion = []

    while n > 0:

        for termino in range(1, n + 1):
            termino_cuadrado = termino**2

            if (termino_cuadrado <= n) and (mem[n] == 1 + mem[n - termino_cuadrado]):
                solucion.append(f"{termino}²")
                n -= termino_cuadrado
                break
    
    solucion.reverse()
    return " + ".join(str(termino) for termino in solucion)

def terminos(n):
    mem = terminos_dinamico(n)
    solucion = terminos_solucion(mem, n)

    return mem[n], solucion

assert terminos(1) == (1, "1²")
assert terminos(2) == (2, "1² + 1²")
assert terminos(3) == (3, "1² + 1² + 1²")
assert terminos(4) == (1, "2²")
assert terminos(5) == (2, "2² + 1²")
assert terminos(6) == (3, "2² + 1² + 1²")
assert terminos(7) == (4, "2² + 1² + 1² + 1²")
assert terminos(8) == (2, "2² + 2²")
assert terminos(9) == (1, "3²")
assert terminos(10) == (2, "3² + 1²")

# Complejidad

# Matriz de memorizacion: La complejidad resulta ser O(V) con V la cantidad de vertices.

# Reconstruccion de la solucion: La complejidad resulta ser O(V) con V la cantidad de vertices.

# Luego, la complejidad total resulta resulta ser O(V) con V la cantidad de vertices.