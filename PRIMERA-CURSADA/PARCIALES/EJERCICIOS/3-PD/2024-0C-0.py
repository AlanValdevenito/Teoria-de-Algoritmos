# En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. Ahora planteamos un
# problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar,
# devuelva la cantidad de formas diferentes que hay para dar dicho cambio. 

# El algoritmo a implementar debe ser # también por programación dinámica. 

# Indicar y justificar la complejidad del algoritmo implementado. Importante: antes de escribir código, escribir (y describir) la ecuación 
# de recurrencia.

# Ecuacion de recurrencia: OPT(i) = sum(OPT(i-m)) para toda moneda m tal que i >= m

def cambio_dinamico(monedas, monto):
    mem = [0] * (monto+1)

    # Caso base
    mem[0] = 1

    for m in monedas:
        # print(f"Moneda: {m}")
        for i in range(m, monto + 1):
            # print(f"OPT[{i}] += OPT[{i}-{m}] = OPT[{i-m}] = {mem[i-m]}")
            mem[i] += mem[i-m]

        # print("\n")

    return mem

def cambio(monedas, monto):
    mem = cambio_dinamico(monedas, monto)

    return mem[monto]

# Complejidad: Debito a la construccion de la matriz de memorizacion la complejidad resulta ser O(C x N) con C el cambio a dar y N la
# cantidad de monedas.

assert cambio([1,2,5], 5) == 4

# Seguimiento: 

# Moneda: 1
# OPT[1] += OPT[1-1] = OPT[0] = 1
# OPT[2] += OPT[2-1] = OPT[1] = 1
# OPT[3] += OPT[3-1] = OPT[2] = 1
# OPT[4] += OPT[4-1] = OPT[3] = 1
# OPT[5] += OPT[5-1] = OPT[4] = 1

# Moneda: 2
# OPT[2] += OPT[2-2] = OPT[0] = 1
# OPT[3] += OPT[3-2] = OPT[1] = 1
# OPT[4] += OPT[4-2] = OPT[2] = 2
# OPT[5] += OPT[5-2] = OPT[3] = 2

# Moneda: 5
# OPT[5] += OPT[5-5] = OPT[0] = 1

# 1 + 1 + 1 + 1 + 1
# 2 + 1 + 1 + 1
# 2 + 2 + 1
# 5

assert cambio([4,2], 18) == 5

# Seguimiento

# Moneda: 4
# OPT[4] += OPT[4-4] = OPT[0] = 1
# OPT[5] += OPT[5-4] = OPT[1] = 0
# OPT[6] += OPT[6-4] = OPT[2] = 0
# OPT[7] += OPT[7-4] = OPT[3] = 0
# OPT[8] += OPT[8-4] = OPT[4] = 1
# OPT[9] += OPT[9-4] = OPT[5] = 0
# OPT[10] += OPT[10-4] = OPT[6] = 0
# OPT[11] += OPT[11-4] = OPT[7] = 0
# OPT[12] += OPT[12-4] = OPT[8] = 1
# OPT[13] += OPT[13-4] = OPT[9] = 0
# OPT[14] += OPT[14-4] = OPT[10] = 0
# OPT[15] += OPT[15-4] = OPT[11] = 0
# OPT[16] += OPT[16-4] = OPT[12] = 1
# OPT[17] += OPT[17-4] = OPT[13] = 0
# OPT[18] += OPT[18-4] = OPT[14] = 0

# Moneda: 2
# OPT[2] += OPT[2-2] = OPT[0] = 1
# OPT[3] += OPT[3-2] = OPT[1] = 0
# OPT[4] += OPT[4-2] = OPT[2] = 1
# OPT[5] += OPT[5-2] = OPT[3] = 0
# OPT[6] += OPT[6-2] = OPT[4] = 2
# OPT[7] += OPT[7-2] = OPT[5] = 0
# OPT[8] += OPT[8-2] = OPT[6] = 2
# OPT[9] += OPT[9-2] = OPT[7] = 0
# OPT[10] += OPT[10-2] = OPT[8] = 3
# OPT[11] += OPT[11-2] = OPT[9] = 0
# OPT[12] += OPT[12-2] = OPT[10] = 3
# OPT[13] += OPT[13-2] = OPT[11] = 0
# OPT[14] += OPT[14-2] = OPT[12] = 4
# OPT[15] += OPT[15-2] = OPT[13] = 0
# OPT[16] += OPT[16-2] = OPT[14] = 4
# OPT[17] += OPT[17-2] = OPT[15] = 0
# OPT[18] += OPT[18-2] = OPT[16] = 5

# 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
# 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2
# 4 + 4 + 2 + 2 + 2 + 2 + 2
# 4 + 4 + 4 + 2 + 2 + 2
# 4 + 4 + 4 + + 4 + 2