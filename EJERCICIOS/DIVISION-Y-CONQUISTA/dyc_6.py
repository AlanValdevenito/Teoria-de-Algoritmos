# Implementar un algoritmo de multiplicación de dos números grandes de longitud n, por división y conquista, con un orden de complejidad 
# mejor que O(n^2). 

# Justificar el orden del algoritmo mediante el teorema maestro.

# Operaciones:
# y = x >> n -> Mueve los bits n veces hacia la derecha. Es decir, devuelve los n bits mas significativos
# y = x & (2**(n) - 1) -> Devuelve los n bits menos significativos

# Ejemplo:
# 1) 173 = 10101101 -> 10 = 00001010
# 2) 173 = 10101101 -> 13 = 00001101

def multiplicar(a, b):
    n = a.bit_length()

    # Si el numero de bits es pequeño, usamos la multiplicacion directa
    if n < 2:
        return a*b
    
    m = (n+1) // 2

    a1 = a >> m
    a0 = a & (2**m - 1)

    b1 = b >> m
    b0 = b & (2**m - 1)

    p = multiplicar(a1+a0, b1+b0)
    a0b0 = multiplicar(a0, b0)
    a1b1 = multiplicar(a1, b1)

    return (a1b1 << (2*m)) + ((p - a1b1 - a0b0) << m) + a0b0

# Justificacion: Teorema maestro

# A: 3 (En cada ejecution tenemos 3 llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Debido a la division de los numeros la cual es una operacion lineal)

# T(n) = A.T(n/B) + O(n^C) = 3 T(n/2) + O(n^1) = 3 T(n/2) + O(n)

# log (A) = log (3) = 1,6 > C → T(n) = O(n^log (A)) = O(n^log (3)) = O(n^1,6)
#    B         2                              B              2

assert multiplicar(173, 173) == 29929