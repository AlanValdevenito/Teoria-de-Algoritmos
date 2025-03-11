# Implementar un algoritmo potencia(b, n) que nos devuelva el resultado de b^n en tiempo O(log n). 

# Justificar adecuadamente la complejidad del algoritmo implementado. 

# Ayuda: recordar propiedades matemáticas de la potencia. Por ejemplo, que a^h ·a^k = a^(h+k)

def potencia(b, n):
    
    if (n == 0):
        return 1
    
    elif (n == 1):
        return b
    
    medio = potencia(b, n // 2)

    if (n % 2 == 0):
        return medio * medio # b^n = b^(n/2) x b^(n/2) 
    
    return b * medio * medio # b^n = b x b^(n-1) = b x b^(n/2) x b^(n/2) 

# Complejidad: Teorema maestro

# A: 1 (Se tiene solo un llamado recursivo)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2    

assert potencia(5, 2) == 25
assert potencia(4, 4) == 256
assert potencia(7, 2) == 49