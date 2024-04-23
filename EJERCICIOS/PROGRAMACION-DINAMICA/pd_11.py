# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar desde 0 a K, siendo que las 
# operaciones posibles son:

# (i) aumentar el valor del operando en 1;

# (ii) duplicar el valor del operando.

# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a 
# realizar (y cuáles son dichas operaciones). 

# Desarrollar la ecuación de recurrencia.

# Indicar y justificar la complejidad del algoritmo implementado.

# Devolver un arreglo de las operaciones a realizar en orden. En texto cada opción es 'mas1' o 'por2'.

# Definicion:

# O(1) = mas1
# O(2) = mas1, por2
# O(3) = mas1, por2, mas1
# O(4) = mas1, por2, por2
# O(5) = mas1, por2, por2, mas1
# O(6) = mas1, por2, mas1, por2

# Ecuacion de recurrencia: O(N) = min{N par, N impar} = min{O(N/2) + 1, O(N-1) + 1}

# Ejemplo: O(6) = min{3 + 1, 4 + 1} = min{4, 5} = 4
# Solucion para K = 6: mas1, por2, mas1, por2 

AUMENTAR_OPERANDO = 'mas1'
DUPLICAR_OPERANDO = 'por2'

def operaciones_dinamico(k):

    if (k == 0):
        return 0
    
    mem = [0] * (k+1)
    mem[0] = 0

    for i in range(1, k+1):
        mem[i] = min(mem[i//2] + 1, mem[i-1] + 1)

    return mem

def operaciones_solucion(mem, k, solucion):

    if (k == 0):
        return solucion
    
    if (k % 2 == 0):
        solucion.append(DUPLICAR_OPERANDO)
        return operaciones_solucion(mem, k // 2, solucion)

    solucion.append(AUMENTAR_OPERANDO)
    return operaciones_solucion(mem, k - 1, solucion)

def operaciones(k):
    mem = operaciones_dinamico(k)
    solucion = operaciones_solucion(mem, k, [])
    return solucion[::-1]

# Complejidad: Tenemos O(k) por calcular la matriz de memorizacion y O(k) por recuperar la solucion. Luego, la
# complejidad total es O(k).

assert operaciones(6) == [AUMENTAR_OPERANDO, DUPLICAR_OPERANDO, AUMENTAR_OPERANDO, DUPLICAR_OPERANDO]