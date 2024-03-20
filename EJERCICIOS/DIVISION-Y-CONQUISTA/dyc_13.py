# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de 
# máxima suma, utilizando División y Conquista. 

# Indicar y justificar la complejidad del algoritmo. 

# Ejemplos:
# [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
# [5, 3, -5, 4, -1] ->  [5, 3]
# [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
# [5, -4, 2, 4] -> [5, -4, 2, 4]

def _max_subarray(arr, desde, hasta):
    
    if (desde == hasta):
        return desde, hasta, arr[desde]
    
    medio = (desde + hasta) // 2

    izq_desde, izq_hasta, sum_izq = _max_subarray(arr, desde, medio)
    der_desde, der_hasta, sum_der = _max_subarray(arr, medio+1, hasta)
    
    if ((sum_izq + sum_der) > sum_izq) and ((sum_izq + sum_der) > sum_der):
        return izq_desde, der_hasta, sum_izq + sum_der
    
    return (izq_desde, izq_hasta, sum_izq + arr[medio]) if sum_izq + arr[medio] > sum_der + arr[medio] else (der_desde, der_hasta, sum_der + arr[medio])
    
def max_subarray(arr):
    n = len(arr) # Operacion O(1)
    inicio, fin, suma = _max_subarray(arr, 0, n-1)
    return arr[inicio:fin+1], suma

# Justificacion: Teorema maestro

# A: 2 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                            B

arr1 = [5, 3, 2, 4, -1]
resultado1, suma1 = max_subarray(arr1)
print(f"{arr1} →  {resultado1}")

arr2 = [5, 3, -5, 4, -1]
resultado2, suma2 = max_subarray(arr2)
print(f"{arr2} →  {resultado2}")

arr3 = [5, -4, 2, 4, -1]
resultado3, suma3 = max_subarray(arr3)
print(f"{arr3} →  {resultado3}")

arr4 = [5, -4, 2, 4]
resultado4, suma4 = max_subarray(arr4)
print(f"{arr4} →  {resultado4}")