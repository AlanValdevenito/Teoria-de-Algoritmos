# Implementar una función (que utilice división y conquista) de complejidad O(n log (n)) que dado un arreglo de n números enteros devuelva 
# true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución. 

# Ejemplos:

# [1, 2, 1, 2, 3] -> false
# [1, 1, 2, 3] -> false
# [1, 2, 3, 1, 1, 1] -> true
# [1] -> true

# Notemos que si un elemento aparece mas de la mitad de las veces, entonces aparece en la mitad del arreglo.

# Luego, nuestro caso base sera cuando tengamos un unico elemento en el arreglo. Al tener un unico elemento en el arreglo, este esta 
# mas de la mitad de las veces y lo devolvemos.

def aparece_mas_de_la_mitad(inicio, fin, apariciones):
    return (apariciones > (((fin+1) - inicio) // 2))

def contar_apariciones(arr, inicio, fin, elemento):
    apariciones = 0

    for i in range(inicio, fin+1):
        if (arr[i] == elemento): apariciones += 1

    return apariciones

def _mas_de_la_mitad(arr, inicio, fin):

    if (inicio == fin):
        return arr[inicio]
    
    medio = (inicio + fin) // 2

    candidato_izq = _mas_de_la_mitad(arr, inicio, medio)
    candidato_der = _mas_de_la_mitad(arr, medio+1, fin)

    apariciones_izq = contar_apariciones(arr, inicio, fin, candidato_izq)
    apariciones_der = contar_apariciones(arr, inicio, fin, candidato_der)

    # print(f"Arreglo: {arr[inicio:fin+1]}")
    # print(f"Candidato izquierdo: {candidato_izq} - Apariciones: {apariciones_izq}") 
    # print(f"Candidato derecho: {candidato_der} - Apariciones: {apariciones_der}\n")

    return True if aparece_mas_de_la_mitad(inicio, fin, apariciones_izq) or aparece_mas_de_la_mitad(inicio, fin, apariciones_der) else False

def mas_de_la_mitad(arr):
    return _mas_de_la_mitad(arr, 0, len(arr) - 1)

# Complejidad

# A: 2 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Costo de partir y juntar)

# T(n) = A T(n/B) + O(n^C) = 2 T(n/2) + O(n)

# log (2) = 1 ￫ T(n) = O(n^C log (n)) = O(n^C log (n)) = O(n^1 log (n)) = O(n log(n))
#    2                          B 

assert mas_de_la_mitad([1, 2, 1, 2, 3]) == False
assert mas_de_la_mitad([1, 1, 2, 3]) == False
assert mas_de_la_mitad([1, 2, 3, 1, 1, 1]) == True
assert mas_de_la_mitad([1]) == True