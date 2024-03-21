# Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente hasta una determinada 
# posición p, y estrictamente decreciente a partir de ella (con 0 < p < N - 1). 

# Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2. Se pide:

# 1. Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p del pico.  La 
# función será invocada inicialmente como: PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el 
# arreglo tenga forma de pico.

# 2. Justificar el orden del algoritmo mediante el teorema maestro.

def posicion_pico(v, ini, fin):
    
    if (ini == fin):
        return ini
    
    medio = (ini + fin) // 2

    if (v[medio-1] < v[medio]) and (v[medio+1] < v[medio]):
        return medio

    if (v[medio-1] < v[medio]):
        return posicion_pico(v, medio+1, fin)
    
    return posicion_pico(v, ini, medio)

# Justificacion: Teorema maestro

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2                                B

v = [1, 2, 3, 1, 0, -2]
resultado = posicion_pico(v, 0, len(v)-1)
print(f"La posicion delpico es: {resultado}")