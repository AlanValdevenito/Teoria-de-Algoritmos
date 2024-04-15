# Implementar una función, que utilice división y conquista, de orden O(n log (⁡n)) que dado un arreglo de n
# números enteros devuelva true o false según si existe algún elemento que aparezca más de la mitad de las veces. 

# Justificar el orden de la solución. 

# Ejemplos:

# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true

def contar_apariciones(arr, desde, hasta, n):
    contador = 0

    for i in range(desde, hasta+1):
        if (n == arr[i]):
            contador += 1

    return contador

def _mas_de_la_mitad(arr, desde, hasta):

    # Caso base: Un unico elemento en el arreglo. 
    # Al tener un unico elemento en el arreglo, este esta mas de la mitad de las veces y lo devolvemos.
    if (desde == hasta):
        return arr[desde]
    
    medio = (desde + hasta) // 2

    izq_candidato = _mas_de_la_mitad(arr, desde, medio)
    der_candidato = _mas_de_la_mitad(arr, medio+1, hasta)

    izq_contador = contar_apariciones(arr, desde, hasta, izq_candidato)
    der_contador = contar_apariciones(arr, desde, hasta, der_candidato)

    if izq_contador > (((hasta+1) - desde) // 2):
        return izq_candidato
    
    if der_contador > (((hasta+1) - desde) // 2):
        return der_candidato
    
    return None

def mas_de_la_mitad(arr):
    n = len(arr) # Operacion (1)
    candidato = _mas_de_la_mitad(arr, 0, n-1)

    return True if candidato else False

# Justificacion: Teorema maestro

# A: 2 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Debido a que necesitamos iterar el arreglo para contar las apariciones de los candidatos)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B

arr1 = [1, 2, 1, 2, 3]
resultado1 = mas_de_la_mitad(arr1)
print(f"{arr1} →  Resultado: {resultado1} - Esperado: False \n")

arr2 = [1, 1, 2, 3]
resultado2 = mas_de_la_mitad(arr2)
print(f"{arr2} →  Resultado: {resultado2} - Esperado: False \n")

arr3 = [1, 2, 3, 1, 1, 1]
resultado3 = mas_de_la_mitad(arr3)
print(f"{arr3} →  Resultado: {resultado3} - Esperado: True \n")

arr3 = [1]
resultado3 = mas_de_la_mitad(arr3)
print(f"{arr3} →  Resultado: {resultado3} - Esperado: True \n")