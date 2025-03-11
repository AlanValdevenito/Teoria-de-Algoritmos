# Tenemos un conjunto de números v_1 , v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o 
# menor a un valor V, tratando de aproximarse lo más posible a V. 

# Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos 
# deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Ecuacion de recurrencia: OPT(n,V) = max{no usar el elemento, usar el elemento} = 
#                                   = max{OPT(n-1, V), OPT(n-1, V-Vi) + Vi}

def subset_sum_dinamico(elementos, n, W):
    mem = [[0 for i in range(W+1)] for j in range(n+1)]
    
    for i in range(1, n+1):
        elem = elementos[i-1]
        for j in range(1, W+1):

            if elem > j:
                mem[i][j] = mem[i-1][j]

            else:
                mem[i][j] = max(mem[i-1][j], mem[i-1][j - elem] + elem)

    return mem

def subset_sum_solucion(mem, elementos, n, W):
    solucion = []

    while n > 0 and W >= 0:

        if mem[n][W] != mem[n-1][W]:
            solucion.append(elementos[n-1])
            W -= elementos[n-1]

        n -= 1

    solucion.reverse()
    return solucion

def subset_sum(elementos, v):
    n = len(elementos)
    mem = subset_sum_dinamico(elementos, n, v)
    return subset_sum_solucion(mem, elementos, n, v)

# Complejidad: Tenemos O(n x v) por calcular la matriz de memorizacion, donde n es el numero de elementos y v es el valor al
# que debe llegar la suma, y O(n) por recuperar la solucion ya que en el peor de los casos recorre los elementos una vez. Luego, la
# complejidad total es O(n x v).

assert subset_sum([5, 6], 12) == [5, 6]
assert subset_sum([1, 3], 4) == [1, 3]
assert subset_sum([10, 7, 5, 13], 16) == [10, 5]