# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no
# puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta $Ci. También se
# han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi.

# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. 

# Indicar y justificar la complejidad del algoritmo propuesto.

# ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda? (haciendo la equivalencia 
# de divisa, siempre suponiendo valores enteros).

# Ecuacion de recurrencia: OPT(n, P) = max{realizar campaña, no realizar campaña} = max{OPT(n-1, P-Ci) + Gi, OPT(n-1, P)}

GANANCIA = 0
COSTO = 1

def carlitos_dinamico(c_publicitaria, P, n):
    mem = [[0 for _ in range(P+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        campaña = c_publicitaria[i-1]
        for j in range(1, P+1):

            if campaña[COSTO] > j:
                mem[i][j] = mem[i-1][j]

            else:
                mem[i][j] = max(mem[i-1][j-campaña[COSTO]] + campaña[GANANCIA], mem[i-1][j])

    return mem

def carlitos_solucion(c_publicitaria, P, mem, n):
    solucion = []

    while (n > 0) and (P >= 0):

        if (mem[n][P] != mem[n-1][P]):
            solucion.append(c_publicitaria[n-1])
            P -= c_publicitaria[n-1][COSTO]

        n -= 1

    solucion.reverse()
    return solucion

def carlitos(c_publicitaria, P):
    n = len(c_publicitaria)
    mem = carlitos_dinamico(c_publicitaria, P, n)
    return carlitos_solucion(c_publicitaria, P, mem, n)

# Complejidad

# Armar la matriz de memorizacion tiene una complejidad de O(n x P) donde n es la cantidad de campañas y P es el preupuesto.

# Reconstruir la solucion tiene una complejidad de O(n) donde n es la cantidad de camapñas.

# Luego, la complejidad resulta ser O(n x P).

# ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda?. Notemos que no da lo mismo si los valores 
# están expresados en pesos argentinos, dólares u otra moneda  Esto se debe ya que al trabajar con una u otra moneda  los montos cambian 
# en cuento a la cantidad de unidades, lo cual es un problema ya que para 'P' importa la cantidad de unidades, siendo que a mayor 
# unidades la complejidad aumenta, lo hace que sea importante.

assert carlitos([], 10) == []
assert carlitos([(5, 10)], 10) == [(5, 10)]
assert carlitos([(3, 2), (4, 3), (5, 4), (6, 5)], 5) == [(3, 2), (4, 3)]
assert carlitos([(10, 1), (15, 2), (40, 3)], 6) == [(10, 1), (15, 2), (40, 3)]
assert carlitos([(5, 5), (3, 3), (7, 7)], 10) == [(3, 3), (7, 7)]
assert carlitos([(1, 1), (2, 1), (3, 1)], 2) == [(2, 1), (3, 1)]
assert carlitos([(15, 7), (8, 4), (8, 4)], 8) == [(8, 4), (8, 4)]
assert carlitos([(1, 2), (2, 3), (5, 5), (9, 8)], 11) == [(2, 3), (9, 8)]