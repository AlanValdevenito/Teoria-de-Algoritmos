# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci. 
# Indicar y justificar la complejidad del algoritmo implementado.

# Definición:
# n = 0 --> Debe devolver 1
# n = 1 --> Debe devolver 1
# n --> Debe devolver la suma entre los dos anteriores números de fibonacci (los fibonacci n-2 y n-1)

# Ecuacion de recurrencia: f(n) = f(n-1) + f(n-2).

def fibonacci(n):

    if (n == 0):
        return 0
    
    if (n == 1):
        return 1
    
    anterior = 0
    actual = 1

    for i in range(1, n):
        siguiente = actual + anterior
        anterior = actual
        actual = siguiente

    return actual

# Complejidad: Debido a que iteramos n veces la complejidad resulta ser O(n).

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(7) == 13
assert fibonacci(10) == 55
assert fibonacci(20) == 6765