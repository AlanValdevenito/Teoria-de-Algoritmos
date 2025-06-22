# En clase vimos una solución óptima del problema del cambio utilizando programación dinámica. 

# Ahora planteamos un problema similar: Implementar un algoritmo que dado un set de monedas posibles y una cantidad de cambio a dar, devuelva la cantidad 
# de formas diferentes que hay para dar dicho cambio. 

# El algoritmo a implementar debe ser también por programación dinámica. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# Importante: antes de escribir código, escribir (y describir) la ecuación de recurrencia.

# ¿Que tipo de problema es?. Nos preguntamos cuantas formas diferentes hay de lograr un cierto objetivo. ES decir, es un problema de combinatoria.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de cambio a dar.

# ¿Importa el orden?. Es decir, ¿contamos como una forma de dar cambio si el orden cambia?. No importa el orden y consideramos que 1+2+1 y 2+1+1 son la misma 
# forma.

# Ejemplo: Consideremos el conjunto de monedas [1, 3, 4] y el cambio a dar 6.

# OPT[0] = 0
# OPT[1] = 1 (dando 1)
# OPT[2] = 1 (dando 1+1)
# OPT[3] = 2 (dando 1+1+1, dando 3)
# OPT[4] = 3 (dando 1+1+1+1, dando 1+3, dando 4)
# OPT[5] = 3 (dando 1+1+1+1+1, dando 1+1+3, dando 1+4)
# OPT[6] = 4 (dando 1+1+1+1+1+1, dando 3+3, dando 1+1+1+3, dando 1+1+4)

# ¿Como se componen estos subproblemas para solucionar subproblemas mas grandes?.

# Ecuacion de recurrencia: OPT[i] = sum(OPT[i-m]) para toda moneda m <= i

# Nota: Para que esta ecuacion de recurrencia sea valida se deben procesar las monedas una por una, por fuera de la sumatoria. Esto evita que contemos las
# distintas permutaciones y nos aseguramos de contar combinaciones unicas.

# Caso base: OPT[0] = 1

# Para la moneda 1: 
# OPT[1] = OPT[1-1] = 1
# OPT[2] = OPT[2-1] = 1
# OPT[3] = OPT[3-1] = 1
# OPT[4] = OPT[4-1] = 1
# OPT[5] = OPT[5-1] = 1
# OPT[6] = OPT[6-1] = 1

# Para la moneda 3:
# OPT[3] += OPT[3-3] += OPT[0] = 1 + 1 = 2
# OPT[4] += OPT[4-3] += OPT[1] = 1 + 1 = 2
# OPT[5] += OPT[5-3] += OPT[2] = 1 + 1 = 2
# OPT[6] += OPT[6-3] += OPT[3] = 1 + 2 = 3

# Para la moneda 4:
# OPT[4] += OPT[4-4] += OPT[0] = 2 + 1 = 3
# OPT[5] += OPT[5-4] += OPT[1] = 2 + 1 = 3
# OPT[6] += OPT[6-4] += OPT[2] = 3 + 1 = 4

# OPT = [1, 1, 1, 2, 3, 3, 4]

def cambio_dinamico(monedas, monto):
    mem = [0] * (monto + 1)
    mem[0] = 1

    for m in monedas:
        # print(f"\nPara la moneda {m}:")
        for i in range(1, monto + 1):

            if m > i: continue
            # print(f"OPT[{i}] = {mem[i]} += OPT[{i}-{m}] = OPT[{i-m}] = {mem[i-m]}")
            mem[i] += mem[i-m]

    return mem

def cambio(monedas, monto):
    mem = cambio_dinamico(monedas, monto)
    # print(f"OPT = {mem}")
    return mem[monto]

assert cambio([1, 3, 4], 6) == 4

# Complejidad

# Matriz de memorizacion: La complejidad resulta ser O(c x m) con c la cantidad de monedas y m el monto de cambio a dar.
# - Iteramos las c monedas lo cual tiene una complejidad de O(c).
# - Por cada moneda, iteramos desde 1 hasta el monto de cambio a dar m lo cual tiene una complejidad de O(c x m).

# Luego, la complejidad total resulta ser O(c x m) con c la cantidad de monedas y m el monto de cambio a dar.