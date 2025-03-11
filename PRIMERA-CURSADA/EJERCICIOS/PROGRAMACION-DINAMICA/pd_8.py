# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata. Se desea devolver 
# el cambio pedido, usando la mínima cantidad de monedas/billetes. Implementar un algoritmo que, por programación dinámica, reciba 
# un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué monedas/billetes deben ser 
# utilizados para minimizar la cantidad total utilizda. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Notemos que tenemos un problema de optimizacion donde debemos minimizar la cantidad de monedas.

# Ecuacion de recurrencia: OPT[i] = 1 + min(OPT[i-m]) para toda moneda m tal que m <= i

def cambio_dinamico(monedas, monto):
    mem = [0] * (monto+1)

    for i in range(1, monto+1):
        minimo = i

        for moneda in monedas:

            if moneda > i:
                continue
            
            cantidad = 1 + mem[i-moneda]

            if cantidad < minimo:
                minimo = cantidad

        mem[i] = minimo

    return mem

def cambio_solucion(monedas, monto, mem):
    solucion = []

    while monto > 0:
        for moneda in monedas:
            if (monto >= moneda) and (mem[monto] == mem[monto - moneda] + 1):
                solucion.append(moneda)
                monto -= moneda
                break

    return solucion

def cambio(monedas, monto):
    mem = cambio_dinamico(monedas, monto)
    solucion = cambio_solucion(monedas, monto, mem)
    return solucion

# Complejidad: Tenemos O(n*c) por calcular la matriz de memorizacion donde n es el monto de dinero y c la cantidad de monedas del sistema monetario.

assert cambio([50, 20, 5, 500, 1, 100, 10], 583) == [50, 20, 500, 1, 1, 1, 10]