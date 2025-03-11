# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no puede sobrepasar, y tiene que una serie de 
# campañas publicitarias para elegir. La campaña i cuesta Ci. También se han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada 
# campaña, que denominaremos Gi. 

# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos.

# Indicar y justificar la complejidad del algoritmo propuesto.

# ¿Da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda?. Por ejemplo, si una campaña cuesta 100 dólares, para pasar a pesos se 
# debe hacer la conversión de divisa.

# Queremos maximizar la ganancia sin exceder el persupuesto.

# Notemos que este problema es similar al problema de la mochila. A continuacion relacionamos las variables de cada problema:
# - Presupuesto P = Capacidad W
# - Costo C = Peso P
# - Ganancia G = Valor V

# Nota: Se podria reutilizar la solucion del ejercicio 7 pero se decidio copiar el codigo y adaptarlo a este.

# Ecuacion de recurrencia: OPT(n,P) = max{no elegir campaña publicitaria, elegir campaña publicitaria} = 
#                                   = max{OPT(n-1, P), OPT(n-1, P-Ci) + Gi}

GANANCIA = 0
COSTO = 1

def carlitos_dinamico(c_publicitaria, n, P):
    mem = [[0 for i in range(P+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        campaña = c_publicitaria[i-1]
        for j in range(1, P+1):

            if (campaña[COSTO] > j):
                mem[i][j] = mem[i-1][j]

            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j - campaña[COSTO]] + campaña[GANANCIA])

    return mem

def carlitos_solucion(mem, c_publicitaria, n, P):
    solucion = []

    while (n > 0) and (P >= 0):

        if (mem[n][P] != mem[n-1][P]):
            solucion.append(c_publicitaria[n-1])
            P -= c_publicitaria[n-1][COSTO]

        n -= 1

    solucion.reverse()
    return solucion

# Cada campaña publicitaria i de la forma (Gi, Ci)
def carlitos(c_publicitaria, P):
    n = len(c_publicitaria)
    mem = carlitos_dinamico(c_publicitaria, n, P)
    return carlitos_solucion(mem, c_publicitaria, n, P)

# Complejidad: Tenemos O(n x P) por calcular la matriz de memorizacion, donde n es el numero de elementos y P es el presupuesto, y O(n) por recuperar 
#              la solucion ya que en el peor de los casos recorre los elementos una vez. Luego, la complejidad total es O(n x P).

# Notemos que no da lo mismo si los valores están expresados en pesos argentinos, dólares u otra moneda  Esto se debe ya que al trabajar con una u otra moneda 
# los montos cambian en cuento a la cantidad de unidades, lo cual es un problema ya que para 'P' importa la cantidad de unidades, siendo que a mayor 
# unidades la complejidad aumenta, lo hace que sea importante.

assert carlitos([], 10) == []
assert carlitos([(5, 10)], 10) == [(5, 10)]
assert carlitos([(3, 2), (4, 3), (5, 4), (6, 5)], 5) == [(3, 2), (4, 3)]
assert carlitos([(10, 1), (15, 2), (40, 3)], 6) == [(10, 1), (15, 2), (40, 3)]
assert carlitos([(5, 5), (3, 3), (7, 7)], 10) == [(3, 3), (7, 7)]
assert carlitos([(1, 1), (2, 1), (3, 1)], 2) == [(2, 1), (3, 1)]
assert carlitos([(15, 7), (8, 4), (8, 4)], 8) == [(8, 4), (8, 4)]
assert carlitos([(1, 2), (2, 3), (5, 5), (9, 8)], 11) == [(2, 3), (9, 8)]