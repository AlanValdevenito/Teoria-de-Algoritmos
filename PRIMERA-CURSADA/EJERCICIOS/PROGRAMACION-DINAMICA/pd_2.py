# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. Además, cada charla 
# tiene asociado un valor de ganancia. Implementar un algoritmo que, utilizando programación dinámica, reciba un 
# arreglo que en cada posición tenga una charla representada por una tripla de inicio, fin y valor de cada 
# charla, e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Ecuacion de recurrencia: OPT(i) = max{dar la charla, no dar la charla} = max{vi + p(i), OPT(i-1)}

HORA_INICIO = 0
HORA_FIN = 1
VALOR = 2

def calcular_p(charlas, n):
    p = [0] * n

    for i in range(0, n):
        izq, der = 0, i-1
        while izq <= der:
            medio = (izq+der) // 2
            if charlas[medio][HORA_FIN] <= charlas[i][HORA_INICIO]:
                p[i] = medio + 1
                izq = medio + 1
            else:
                der = medio - 1
    
    return p

def scheduling_dinamico(n, p, charlas):

    if n == 0:
        return 0
    
    mem = [0] * (n+1)
    mem[0] = 0

    for i in range(1, n+1):
        mem[i] = max(charlas[i-1][VALOR] + mem[p[i-1]], mem[i-1])

    return mem

def scheduling_solucion(mem, charlas, p, i, solucion):

    if i == 0:
        return solucion
    
    if charlas[i-1][VALOR] + mem[p[i-1]] >= mem[i]:
        solucion.append(i-1)
        return scheduling_solucion(mem, charlas, p, p[i-1], solucion)
    
    return scheduling_solucion(mem, charlas, p, i-1, solucion)    

def scheduling(charlas):
    n = len(charlas)
    charlas_ordenadas = sorted(charlas, key=lambda e: e[HORA_FIN])

    p = calcular_p(charlas_ordenadas, n)

    mem = scheduling_dinamico(n, p, charlas_ordenadas)
    solucion = scheduling_solucion(mem, charlas_ordenadas, p, n, [])
    return [charlas_ordenadas[i] for i in reversed(solucion)]

# Complejidad: Tenemos O(n log(n)) por ordenar las charlas, O(n log (n)) por hacer para cada elemento una busqueda 
# binaria, O(n) por calcular la matriz de memorizacion y O(n) por recuperar la solucion. Luego, la complejidad
# total es O(n log(n)).

assert scheduling([(1,6,1), (3,10,3), (8,14,1)]) == [(3,10,3)]

"""
1   
|----|
  |------|
       |-----|
"""

assert scheduling([(1,6,2), (3,10,4), (8,14,4), (5,19,7), (16,21,2), (18,25,1)]) == [(1,6,2), (8,14,4), (16,21,2)]

"""
1                                     
|----|               
  |------|                       
       |-----|                        
    |-------------|                     
               |----|                    
                 |------|
"""