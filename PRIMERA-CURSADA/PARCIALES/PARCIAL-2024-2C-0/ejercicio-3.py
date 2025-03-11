# Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
# predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
# estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
# casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
# es la de maximizar la ganancia dada por p[k] − p[j].

# Implementar un algoritmo de programación dinámica que permita resolver el problema de Osvaldo. 

# Indicar y justificar la complejidad del algoritmo implementado

# Ejemplo 1: Consideremos el arreglo [3, 7, 9] de predicciones. La ganancia maxima obtenible seria 6 comprando el dia 0 y vendiendo el dia 2.

# OPT(0) = 0

# OPT(1) = OPT(0) + (p[1] - p[0]) = 0 + 4 = 4

# OPT(2) = OPT(1) + (p[2] - p[1]) = 4 + 2 = 6
 
# Ejemplo 2: Consideremos el arreglo [3, 4, 7, 10, 9] de predicciones. La ganancia maxima obtenible seria 7 comprando el dia 0 y vendiendo el dia 3.

# OPT(0) = 0

# OPT(1) = OPT(0) + (p[1] - p[0]) = 0 + 1 = 1

# OPT(2) = OPT(1) + (p[2] - p[1]) = 1 + 3 = 4

# OPT(3) = OPT(2) + (p[3] - p[2]) = 4 + 3 = 7

# OPT(4) = OPT(3) + (p[4] - p[3]) = 7 - 1 = 6

# Ecuacion de recurrencia: OPT(i) = OPT(i-1) + (p[i] - p[j]) con i > 0

# Nota: En la ecuacion de recurrencia planeada suponemos que ya compramos la casa, entonces calculamos la ganancia vendiendo el dia i. Luego, para obtener que dia comprar se recorre el arreglo hasta el dia i buscando el minimo.

def inmueble_dinamico(predicciones):
    mem = [0] * len(predicciones)

    for i in range(1, len(predicciones)):
        mem[i] = mem[i-1] + (predicciones[i] - predicciones[i-1])

    return mem

def inmueble_solucion(predicciones, mem):
    venta = max(range(len(mem)), key=lambda i: mem[i])
    compra = min(range(venta + 1), key=lambda i: predicciones[i])
    return compra, venta

def inmueble(predicciones):
    mem = inmueble_dinamico(predicciones)
    compra, venta = inmueble_solucion(predicciones, mem)
    return (compra, venta, mem[venta])

assert inmueble([3, 7, 9]) == (0, 2, 6)
assert inmueble([3, 4, 7, 10, 9]) == (0, 3, 7)