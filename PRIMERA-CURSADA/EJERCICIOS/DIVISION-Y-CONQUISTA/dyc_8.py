# Dados un conjunto de n elementos, y 2 arreglos de longitud n, con dichos elementos. El arreglo A está completamente ordenado de 
# menor a mayor. El arreglo B se encuentra desordenado. Indicar, por división y conquista, la cantidad de inversioes necesarias al 
# arreglo B para que quede ordenado de menor a mayor, con un orden de complejidad mejor que O(n^2). 

# Justificar el orden del algoritmo mediante el teorema maestro.

def merge(a, b, inversiones):
    i, j = 0, 0
    resultado = []

    print(f"Merge (antes): {a}, {b}")
    print(f"Inversiones: {inversiones}")

    while (i < len(a) and j < len(b)):

        if (a[i] < b[j]):
            resultado.append(a[i])
            i += 1

        else:
            resultado.append(b[j])
            j += 1
            inversiones += len(a) - i
    
    resultado += a[i:]
    resultado += b[j:]

    print(f"Merge (despues): {resultado}")
    print(f"Inversiones: {inversiones}\n")
    return resultado, inversiones

def merge_sort(B, desde, hasta, inversiones):
    
    if desde >= hasta:
        return [B[desde]], inversiones
    
    medio = (desde + hasta) // 2

    izq, inv_izq = merge_sort(B, desde, medio, inversiones)
    der, inv_der = merge_sort(B, medio+1, hasta, inversiones)

    return merge(izq, der, inv_izq + inv_der)

def contar_inversiones(A, B):
    n = len(B)
    _, inversiones = merge_sort(B, 0, n-1, 0)
    return inversiones

# Justificacion: Teorema maestro

# A: 1 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Intercalamos los elementos de los subarreglos izquierdo y derecho de forma ordenada y en el peor caso
#       debemos iterar todo el arreglo)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B  

assert contar_inversiones([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == 10
assert contar_inversiones([1, 2, 3, 4], [4, 3, 2, 1]) == 6
assert contar_inversiones([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == 45
assert contar_inversiones([1, 2], [2, 1]) == 1
assert contar_inversiones([1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 8, 7, 6, 5, 4, 3, 2, 1]) == 36
assert contar_inversiones([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1]) == 28
assert contar_inversiones([1, 2, 3, 4, 5, 6], [6, 5, 4, 3, 2, 1]) == 15
assert contar_inversiones([1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1]) == 21
assert contar_inversiones([1, 2, 3], [3, 2, 1]) == 3