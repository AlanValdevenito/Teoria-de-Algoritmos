# En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un
# problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
# devuelva la cantidad de formas diferentes que hay para dar dicho cambio. 

# El algoritmo a implementar debe ser también por programación dinámica. 

# Indicar y justificar la complejidad del algoritmo implementado. Importante: antes de escribir código, escribir (y describir) la ecuación 
# de recurrencia.

# Nota: Este problema es similar al problema de Subset Sum.

# Ecuacion de recurrencia: OPT(i, j) = usar/repetir la moneda + no usar la moneda = OPT(i, j - moneda_i) + OPT(i-1, j)

# Nota: La variable i representa la moneda y la variable j representa el cambio

def cambio_dinamico(monedas, monto, n):
    mem = [[0 for _ in range(monto+1)] for _ in range(n+1)]

    for i in range(n+1):
        mem[i][0] = 1

    for i in range(1, n+1):
        moneda = monedas[i-1]
        for j in range(monto+1):
            mem[i][j] = mem[i-1][j]

            if moneda <= j:
                mem[i][j] += mem[i][j - moneda]
            
    return mem

def cambio(monedas, monto):
    n = len(monedas)

    mem = cambio_dinamico(monedas, monto, n)

    return mem[n][monto]

# Complejidad: ...

assert cambio([1,2,5], 5) == 4

# Seguimiento: 

# 1 + 1 + 1 + 1 + 1
# 2 + 1 + 1 + 1
# 2 + 2 + 1
# 5

assert cambio([4,2], 18) == 5

# 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
# 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2
# 4 + 4 + 2 + 2 + 2 + 2 + 2
# 4 + 4 + 4 + 2 + 2 + 2
# 4 + 4 + 4 + + 4 + 2