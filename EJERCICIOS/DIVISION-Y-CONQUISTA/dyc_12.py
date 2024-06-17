# Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, tal que la cantidad total de elementos del arreglo 
# es potencia de 2 (por ende, n también lo es). 
# 
# Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que quede con la 
# forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional (obviando el utilizado por la recursividad y variables 
# de tipos simples). 

# ¿Cual es la complejidad del algoritmo?.

# Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). Luego, pensar a partir de allí el 
# caso de 8 elementos, etc… para encontrar el patrón.

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def _alternar(arr, desde, hasta):

    if (hasta - desde == 1):
        return
    
    medio = (desde + hasta) // 2
    segmento = (medio - desde + 1) // 2

    for i in range(segmento):
        swap(arr, medio - segmento + 1 + i, medio + 1 + i)

    _alternar(arr, desde, medio)
    _alternar(arr, medio+1, hasta)

def alternar(arr):
    n = len(arr)
    _alternar(arr, 0, n-1)
    return arr

# Justificacion: Teorema maestro

# A: 2 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Debido a que necesitamos hacer swap entre los elementos)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B

assert alternar(["C1","C2","D1","D2"]) == ['C1', 'D1', 'C2', 'D2']
assert alternar(["C1","C2","C3","C4","D1","D2","D3","D4"]) == ['C1', 'D1', 'C2', 'D2', 'C3', 'D3', 'C4', 'D4']