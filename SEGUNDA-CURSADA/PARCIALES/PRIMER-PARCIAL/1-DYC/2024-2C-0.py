# Osvaldo es un empleado de una inescrupulosa empresa inmobiliaria, y está buscando un ascenso. Está viendo cómo se
# predice que evolucionará el precio de un inmueble (el cual no poseen, pero pueden comprar). Tiene la información de
# estas predicciones en el arreglo p, para todo día i = 1, 2, ..., n. Osvaldo quiere determinar un día j en el cuál comprar la
# casa, y un día k en el cual venderla (k > j), suponiendo que eso sucederá sin lugar a dudas. El objetivo, por supuesto,
# es la de maximizar la ganancia dada por p[k] − p[j].

# Implementar un algoritmo de división y conquista. 

# Indicar y justificar adecuadamente la complejidad del algoritmo implementado.

# Escenarios:
# 1) Compro y vendo en la primera mitad del arreglo p
# 2) Compro y vendo en la segunda mitad del arrglo p
# 3) Compro en la primera mitad y vendo en la segunda mitad del arreglo p

def _inmueble(predicciones, inicio, fin):
    
    if inicio >= fin:
        return inicio, inicio
    
    medio = (inicio + fin) // 2

    compra_izq, venta_izq = _inmueble(predicciones, inicio, medio)
    ganancia_izq = predicciones[venta_izq] - predicciones[compra_izq]
    
    compra_der, venta_der = _inmueble(predicciones, medio+1, fin)
    ganancia_der = predicciones[compra_der] - predicciones[venta_der]

    compra_cruzado = min(range(inicio, medio+1), key=lambda i: predicciones[i])
    venta_cruzado = max(range(medio+1, fin+1), key=lambda i: predicciones[i])
    ganancia_cruzado = predicciones[venta_cruzado] - predicciones[compra_cruzado]

    if ganancia_cruzado >= max(ganancia_izq, ganancia_der):
        return compra_cruzado, venta_cruzado

    if compra_izq >= compra_der:
        return compra_izq, venta_izq

    return compra_der, venta_der

def inmueble(predicciones):
    return _inmueble(predicciones, 0, len(predicciones) - 1)


# Complejidad

# A: 2 (Cantidad de llamados recursivos realizados en cada iteracion) 
# B: 2 (Proporcion de cada subproblema)
# C: 1 (Se busca de forma lineal el minimo a la izquierda y el maximo a la derecha)

# T(n) = A T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C log (n)) = O(n^1 log (n)) = O(n log(n))
#    B         2                              B                2


assert inmueble([3, 7, 9]) == (0, 2)
assert inmueble([3, 4, 7, 10, 9]) == (0, 3)