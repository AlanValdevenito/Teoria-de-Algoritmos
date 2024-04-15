# Resolver el ejercicio anterior, por división y conquista, en orden O(n), dada la misma aclaración. 

# Justificar el orden de la solución.

# Ejemplos:

# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true

# Idea: Si un elemento aparece más de la mitad de las veces en un arreglo de tamaño par, por lo menos una 
# vez tiene aparecer en posiciones consecutivas.

# Podriamos entonces generar un nuevo arreglo, tal que si un elemento aparece en posiciones consecutivas
# guarde en el nuevo arreglo dicho elemento. Estos elementos seran nuestros candidatos.

# En el caso de un arreglo de tamaño impar, nos vamos a quedar con el arreglo original hasta la longitud
# par y el elemento descartado sera tambien un candidato.

def aparece_mas_de_la_mitad(arr, elemento):
    return (arr.count(elemento) > (len(arr) // 2))

def _mas_de_la_mitad(arr):

    if (len(arr) == 0):
        return None

    if (len(arr) == 1):
        return arr[0]
    
    if (len(arr) % 2 == 1) and (aparece_mas_de_la_mitad(arr, arr[-1])):
        return arr[-1]
    
    mitad = []

    for i in range(0, len(arr)-1, 2):
        if arr[i] == arr[i+1]:
            mitad.append(arr[i])

    if mitad == []:
        return None
    
    candidato = _mas_de_la_mitad(mitad)

    if (candidato) and (aparece_mas_de_la_mitad(arr, candidato)):
        return candidato
    
    return None
    
def mas_de_la_mitad(arr):
    candidato = _mas_de_la_mitad(arr)

    return False if (not candidato) or (not aparece_mas_de_la_mitad(arr, candidato)) else True

# Justificacion: Teorema maestro

# A: 1 (Hay escritos un unico llamado recursivo)
# B: 2 (Se divide al problema a la mitad generando un nuevo arreglo con, como maximo, la mitad de los elementos)
# C: 1 (Debido a que necesitamos iterar el arreglo para contar las apariciones de los candidatos)

# T(n) = A.T(n/B) + O(n^C) = 1 T(n/2) + O(n^1) = T(n/2) + O(n)

# log (A) = log (1) = 0 < C = 1 → T(n) = O(n^C) = O(n^1) = O(n)
#    B         2

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

arr4 = [1,2,3,1,5,1,1]
resultado4 = mas_de_la_mitad(arr4)
print(f"{arr4} →  Resultado: {resultado4} - Esperado: True \n")