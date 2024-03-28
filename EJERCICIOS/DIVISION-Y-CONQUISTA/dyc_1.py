# Implementar, por división y conquista, una función que dado un arreglo sin elementos repetidos y casi 
# ordenado (todos los elementos se encuentran ordenados, salvo uno), obtenga el elemento fuera de lugar. 

# Indicar y justificar el orden.

def _elemento_desordenado(arr, desde, hasta):
    
    if (desde == hasta):
        return arr[desde]

    medio = (desde + hasta) // 2

    if (arr[medio] > arr[medio+1]):
        return arr[medio]

    izq = _elemento_desordenado(arr, desde, medio)
    der = _elemento_desordenado(arr, medio+1, hasta)
    
    return izq if (izq > der) else der

def elemento_desordenado(arr):
    n = len(arr) # Operacion O(1)
    return _elemento_desordenado(arr, 0, n-1)

arr1 = [2, 3, 15, 16, 19, 33, 4, 35]
resultado = elemento_desordenado(arr1)
print(f"El elemento desordenado es: {resultado}")