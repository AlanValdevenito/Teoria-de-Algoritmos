# Implementar Merge Sort. 

# Justificar el orden del algoritmo mediante el teorema maestro.

def merge(a, b):
    i, j = 0, 0
    resultado = []

    while (i < len(a) and j < len(b)):

        if (a[i] < b[j]):
            resultado.append(a[i])
            i += 1

        else:
            resultado.append(b[j])
            j += 1
    
    resultado += a[i:]
    resultado += b[j:]

    print(f"Merge: {resultado}")

    return resultado

def _merge_sort(arr, desde, hasta):

    print(arr[desde:hasta+1])

    if desde >= hasta:
        return [arr[desde]]
    
    medio = (desde + hasta) // 2

    izq = _merge_sort(arr, desde, medio)
    der = _merge_sort(arr, medio+1, hasta)

    return merge(izq, der) 

def merge_sort(arr):
    n = len(arr) # Operacion (1)

    if (n == 0):
        return []

    return _merge_sort(arr, 0, n-1)

# Justificacion: Teorema maestro

# A: 1 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Intercalamos los elementos de los subarreglos izquierdo y derecho de forma ordenada y en el peor caso
#       debemos iterar todo el arreglo)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B  

arr1 = [0, 9, 3, 8, 5, 3, 2, 4, 7]
resultado1 = merge_sort(arr1)
print(f"{arr1} →  {resultado1}")