# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar el subarreglo contiguo de 
# máxima suma, utilizando División y Conquista. 

# Indicar y justificar la complejidad del algoritmo. 

# Ejemplos:
# [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
# [5, 3, -5, 4, -1] ->  [5, 3]
# [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
# [5, -4, 2, 4] -> [5, -4, 2, 4]

def _max_subarray(arr, desde, hasta):

    print(arr[desde:hasta+1])
    
    if (desde == hasta):
        return desde, hasta, arr[desde]
    
    medio = (desde + hasta) // 2

    izq_desde, izq_hasta, sum_izq = _max_subarray(arr, desde, medio)
    der_desde, der_hasta, sum_der = _max_subarray(arr, medio+1, hasta)

    if ((sum(arr[medio:der_hasta+1]) > sum_der) and (sum(arr[medio:der_hasta+1]) > sum_izq) and (sum(arr[izq_desde:der_hasta+1]) < sum(arr[medio:der_hasta+1]))):
        print(f"Gana del medio a la derecha: {arr[medio:der_hasta+1]}")
        return  medio, der_hasta, sum(arr[medio:der_hasta+1])
    
    if ((sum(arr[izq_desde:medio+1]) > sum_der) and (sum(arr[izq_desde:medio+1]) > sum_izq) and (sum(arr[izq_desde:der_hasta+1]) < sum(arr[izq_desde:medio+1]))):
        print(f"Gana de la izquierda al medio: {arr[izq_desde:medio+1]}")
        return  izq_desde, medio, sum(arr[izq_desde:medio+1])

    if ((sum_izq + sum_der) < sum_izq) and (sum_der <= sum_izq):
        print(f"Gana la izquierda: {arr[izq_desde:izq_hasta+1]} > {arr[der_desde:der_hasta+1]}")
        return izq_desde, izq_hasta, sum_izq
    
    if ((sum_izq + sum_der) < sum_der) and (sum_izq <= sum_der):
        print(f"Gana la derecha: {arr[izq_desde:izq_hasta+1]} < {arr[der_desde:der_hasta+1]}")
        return der_desde, der_hasta, sum_der
    
    if ((sum(arr[izq_desde:der_hasta+1]) < sum_izq)):
        print(f"Vemos el medio. Gana la izquierda: {arr[izq_desde:izq_hasta+1]} > {arr[izq_desde:der_hasta+1]}")
        return izq_desde, izq_hasta, sum_izq
    
    if ((sum(arr[izq_desde:der_hasta+1]) < sum_der)):
        print(f"Vemos el medio. Gana la derecha: {arr[der_desde:der_hasta+1]} > {arr[izq_desde:der_hasta+1]}")
        return der_desde, der_hasta, sum_der
    
    print(f"Nos quedamos con la interseccion: {arr[izq_desde:der_hasta+1]}")
    return izq_desde, der_hasta, sum(arr[izq_desde:der_hasta+1])

def max_subarray(arr):
    n = len(arr) # Operacion O(1)
    desde, hasta, suma = _max_subarray(arr, 0, n-1)
    return arr[desde:hasta+1], suma

# Justificacion: Teorema maestro

# A: 2 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Debido a que necesitamos sumar todos los elementos en el subarreglo)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B

arr1 = [5, 3, 2, 4, -1]
resultado1, suma1 = max_subarray(arr1)
print(f"{arr1} →  {resultado1}, {suma1}\n")

arr2 = [5, 3, -5, 4, -1]
resultado2, suma2 = max_subarray(arr2)
print(f"{arr2} →  {resultado2}, {suma2}\n")

arr3 = [5, -4, 2, 4, -1]
resultado3, suma3 = max_subarray(arr3)
print(f"{arr3} →  {resultado3}, {suma3}\n")

arr4 = [5, -4, 2, 4]
resultado4, suma4 = max_subarray(arr4)
print(f"{arr4} →  {resultado4}, {suma4}\n")

arr5 = [-4, -1, 0, -6, -2] # -> [0]
resultado5, suma5 = max_subarray(arr5)
print(f"{arr5} →  {resultado5}, {suma5}\n")

arr6 = [10, 9, 8, -100, 5, 4, 3, 2, 1] # ->  [10, 9, 8]
resultado6, suma6 = max_subarray(arr6)
print(f"{arr6} →  {resultado6}, {suma6}\n")

arr7 = [1, 2, 3, -100, 6, 7, 8, 9, 10] # ->  [6, 7, 8, 9, 10, 11, 12]
resultado7, suma7 = max_subarray(arr7)
print(f"{arr7} →  {resultado7}, {suma7}\n")

arr8 = [5, 1, 1, 1, 1, 1, 1, 1, -100, 10] # ->  [1, 2, 3, 2, 1, 2, 1]
resultado8, suma8 = max_subarray(arr8)
print(f"{arr8} →  {resultado8}, {suma8}\n")

arr9 = [-3, 4, -1, 2, 1, 2, 1, 1, 1] # ->  [4, -1, 2, 1, 2, 1, 1, 1]
resultado9, suma9 = max_subarray(arr9)
print(f"{arr9} →  {resultado9}, {suma9}\n")

arr10 = [-3, 4, -1, 2, 1, -5, 4, -1] # ->  [4, -1, 2, 1]
resultado10, suma10 = max_subarray(arr10)
print(f"{arr10} →  {resultado10}, {suma10}\n")
