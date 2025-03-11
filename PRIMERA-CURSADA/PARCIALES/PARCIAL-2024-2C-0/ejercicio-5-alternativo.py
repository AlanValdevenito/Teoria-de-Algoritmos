# Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. 

# Indicar y justificar adecuadamente la complejidad del algoritmo implementado. Es probable que la complejidad de ambas soluciones no 
# quede igual, no te estreses por ello.

# Tres escenarios:
# 1) Comprar y vender en la mitad izquierda
# 2) Comprar y vender en la mitad derecha
# 3) Comprar en la mitad izquierda y vender en la mitad derecha

def _inmueble(predicciones, inicio, fin):

    if inicio >= fin:
        return inicio, inicio

    medio = (inicio + fin) // 2

    # Escenario 1: Comprar y vender en la mitad izquierda
    compra_izq, venta_izq = _inmueble(predicciones, inicio, medio)
    ganancia_izq = predicciones[venta_izq] - predicciones[compra_izq]

    # Escenario 2: Comprar y vender en la mitad derecha
    compra_der, venta_der = _inmueble(predicciones, medio + 1, fin)
    ganancia_der = predicciones[compra_der] - predicciones[venta_der]

    # Escenario 3: Comprar en la mitad izquierda y vender en la mitad derecha
    min_izq = min(range(inicio, medio + 1), key=lambda i: predicciones[i])
    max_der = max(range(medio + 1, fin + 1), key=lambda i: predicciones[i])
    ganancia_cruzada = predicciones[max_der] - predicciones[min_izq]

    if ganancia_cruzada >= max(ganancia_izq, ganancia_der):
        return min_izq, max_der
    
    elif ganancia_izq >= ganancia_der:
        return compra_izq, venta_izq

    return compra_der, venta_der

def inmueble(predicciones):
    return _inmueble(predicciones, 0, len(predicciones)-1)

# Complejidad: Teorema maestro

# A: 2 (En cada ejecution tenemos 2 llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Se busca de forma lineal el minimo a la izquierda y el maximo a la derecha)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C log (n)) = O(n^1 log (n)) = O(n log(n))
#    B         2                              B                2

assert inmueble([3, 7, 9]) == (0, 2)
assert inmueble([3, 4, 7, 10, 9]) == (0, 3)