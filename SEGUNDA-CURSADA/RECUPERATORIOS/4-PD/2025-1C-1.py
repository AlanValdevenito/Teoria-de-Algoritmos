# Laura está de viaje por Japón y entró a un Centro Pokemon, a comprar merchandising. Va a tratar de llevarse todo lo más valioso (para ella) que pueda y que 
# entre en su mochila. 

# Tiene 2 limitaciones. La primera: no puede guardar más peso que lo que permita su mochila (tiene límite hasta W). La segunda: como sabe que puede entrar en 
# un estado de locura e inconciencia temporal, se puso un límite que no comprará por más de P precio en total (es decir, la suma de todo lo comprado).

# Cada producto tiene 3 valores asociados: su valor (vi, que Laura definió en base a su subjetividad), su precio (pi) y su peso (wi).

# Implementar un algoritmo que, utilizando programación dinámica, permita determinar qué productos debe comprar Laura tal que no superen el peso máximo que 
# puede llevar y el precio máximo dispuesto a pagar, y que logre maximizar el valor obtenido (dados por la suma de los elementos comprados). 

# También escribir el algoritmo que permita reconstruir la solución.

# Indicar y justificar la complejidad del algoritmo implementado.

# Nota: Este problema es similar al Problema de la Mochila.

# ¿Que tipo de problema es?. Es un problema de maximizacion ya que nos piden maximizar el valor obtenido.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de elementos, la capacidad W y el limite P.

# Ecuacion de recurrencia: OPT[n, W, P] = max(usar el elemento, no usar el elemento) = max(OPT[n-1, W-wi, P-pi] + vi, OPT[n-1, W, P])

VALOR = 0
PRECIO = 1
PESO = 2

def mochila_dinamico(elementos, W, P, n):
    mem = [[[0 for _ in range(P+1)] for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        elemento = elementos[i-1]
        for j in range(1, W+1):
            for k in range(1, P+1):

                if elemento[PESO] > j or elemento[PRECIO] > k:
                    mem[i][j][k] = mem[i-1][j][k]

                else:
                    mem[i][j][k] = max(mem[i-1][j-elemento[PESO]][k-elemento[PRECIO]] + elemento[VALOR], mem[i-1][j][k])

    return mem

def mochila_solucion(elementos, mem, W, P, n):
    solucion = []

    while (n > 0) and (W >= 0) and (P >= 0):

        if (mem[n][W][P] != mem[n-1][W][P]):
            solucion.append(elementos[n-1])
            W -= elementos[n-1][PESO]
            P -= elementos[n-1][PRECIO]

        n -= 1

    solucion.reverse()

    return solucion

def mochila(elementos, W, P):
    n = len(elementos)
    mem = mochila_dinamico(elementos, W, P, n)
    return mochila_solucion(elementos, mem, W, P, n)

assert mochila([(5, 5, 5), (3, 1, 3), (7, 4, 7)], 10, 5) == [(3, 1, 3), (7, 4, 7)]

# Complejidad

# Matriz de memorizacion: La complejidad resulta O(n x W x P) por calcular la matriz de memorizacion, donde n es el numero de elementos, W es la capacidad
# de la mochila y P el valor maximo a gastar.

# Reconstruccion de la solucion: La complejidad resulta ser O(n) por recuperar la solucion ya que en el peor de los casos recorre los elementos una vez.

# Luego, la complejidad total resulta resulta ser O(n x W x P) por calcular la matriz de memorizacion, donde n es el numero de elementos, W es la capacidad
# de la mochila y P el valor maximo a gastar.
