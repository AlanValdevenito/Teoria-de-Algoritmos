# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las operaciones posibles son:

# (i) aumentar el valor del operando en 1;

# (ii) duplicar el valor del operando.

# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y cuáles son dichas operaciones). 

# Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo implementado. 

# Aclaración: Asegurarse de que el algoritmo presentado sea de programación dinámica, con su correspondiente ecuación de recurrencia.

# Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'

# Ejemplos

# OPT(1) = mas1
# OPT(2) = mas1, por2
# OPT(3) = mas1, por2, mas1
# OPT(4) = mas1, por2, por2
# OPT(5) = mas1, por2, por2, mas1
# OPT(6) = mas1, por2, mas1, por2
# OPT(7) = mas1, por2, mas1, por2, mas1
# OPT(8) = mas1, por2, por2, por2

# ¿Como podemos resolver un problema a partir de subproblemas mas pequeños?.

# Observando los ejemplos, podemos ver que para resolver un problema donde n es par podemos obtener el OPT de n/2 y duplicarlo.
# Mientras que para resolver un problema donde n es impar podemos obtener el OPT de n-1 y aumentarlo.

# Ecuacion de recurrencia: OPT(n) = min{N par, N impar} = min{OPT(n/2) + 1, OPT(n-1) + 1}

AUMENTAR = 'mas1'
DUPLICAR = 'por2'

def operaciones_dinamico(k):

    if (k == 0):
        return 0

    mem = [0] * (k+1)

    for i in range(1, k+1):
        mem[i] = min(mem[i//2] + 1, mem[i-1] + 1)

    return mem

def operaciones_solucion(k, mem):
    solucion = []

    while k > 0:
        
        if (k % 2 == 0):
            solucion.append(DUPLICAR)
            k = k // 2

        else:
            solucion.append(AUMENTAR)
            k -= 1

    solucion.reverse()
    return solucion

def operaciones(k):
    mem = operaciones_dinamico(k)
    solucion = operaciones_solucion(k, mem)
    return solucion

assert operaciones(6) == [AUMENTAR, DUPLICAR, AUMENTAR, DUPLICAR]