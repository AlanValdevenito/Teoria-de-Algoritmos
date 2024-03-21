# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros). 

# Se pide una función de orden O(log(n)) que encuentre el índice del primer 0. Si no hay 
# ningún 0 (solo hay unos), debe devolver -1.

def _indice_primer_cero(arr, desde, hasta):
    
    if (desde == hasta):
        return -1

    medio = (desde + hasta) // 2

    if (arr[medio] == 0):
        return medio

    if (arr[medio] == 0) and (arr[medio-1] == 1):
        return medio

    if (arr[medio] == 1):
        return _indice_primer_cero(arr, medio+1, hasta)
    
    return _indice_primer_cero(arr, desde, medio)

def indice_primer_cero(arr):

    if (arr[0] == 0):
        return 0

    n = len(arr) # Operacion O(1)
    return _indice_primer_cero(arr, 0, n-1)

# Justificacion: Teorema maestro

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2                                B

arr = [1,1,1,0,0,0,0]
resultado = indice_primer_cero(arr)
print(f"El indice del primer 0 es: {resultado}")