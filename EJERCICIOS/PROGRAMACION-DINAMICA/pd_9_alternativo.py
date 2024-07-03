# Tenemos un conjunto de números v_1 , v_2, …, v_n, y queremos obtener un subconjunto de todos esos números tal que su suma sea igual o 
# menor a un valor V, tratando de aproximarse lo más posible a V. 

# Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores, y la suma objetivo V, y devuelva qué elementos 
# deben ser utilizados para aproximar la suma lo más posible a V, sin pasarse. 

# Indicar y justificar la complejidad del algoritmo implementado.

# NOtemos que este problema es igual al de la mochila siempre y cuando para cada elemento se cumpla que W (peso) = V (valor).

from pd_7 import mochila

def transformar_entrada(elementos):
    return [(e, e) for e in elementos]

def subset_sum(elementos, v):
    elementos = transformar_entrada(elementos)
    solucion = mochila(elementos, v)
    return [e[0] for e in solucion]

# Complejidad: Tenemos O(n) por realizar la transformacion y luego O(n x v) debido a la complejidad del problema de la mochila. Luego, la
# complejidad total es O(n x v).

assert subset_sum([5, 6], 12) == [5, 6]
assert subset_sum([1, 3], 4) == [1, 3]
assert subset_sum([10, 7, 5, 13], 16) == [10, 5]