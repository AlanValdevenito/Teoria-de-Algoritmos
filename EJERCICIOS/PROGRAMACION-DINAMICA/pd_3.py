
# Dada una escalera, y sabiendo que tenemos la capacidad de subir escalones de a 1 o 2 o 3 pasos, encontrar, utilizando 
# programación dinámica, cuántas formas diferentes hay de subir la escalera hasta el paso n. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplos:
# n = 0 ⇾ Debe devolver 1 (no moverse)
# n = 1 ⇾ Debe devolver 1 (paso de 1)
# n = 2 ⇾ Debe devolver 2 (dos pasos de 1, o un paso de 2)
# n = 3 ⇾ Debe devolver 4 (un paso de 3, o tres pasos de 1, o un paso de 2 y uno de 1, o un paso de 1 y un paso de 2)
# n = 4 ⇾ Debe devolver 7
# n = 5 ⇾ Debe devolver 13

# Ecuacion de recurrencia: E(n)= E(n-1) + E(n-2) + E(n-3)

def escalones_dinamico(n):
    mem = [0] * (n+1)

    mem[0] = 1
    mem[1] = 1
    mem[2] = 2

    for i in range(3, n+1):
        mem[i] = mem[i-1] + mem[i-2] + mem[i-3]
    
    return mem

def escalones(n):

    if (n == 0) or (n == 1):
        return 1
    
    if (n == 2):
        return 2
    
    mem = escalones_dinamico(n)
    return mem[n]

# Complejidad: Tenemos O(n) por calcular la matriz de memorizacion.

assert escalones(0) == 1
assert escalones(1) == 1
assert escalones(2) == 2
assert escalones(3) == 4
assert escalones(4) == 7
assert escalones(5) == 13