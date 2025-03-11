# Resolver el problema de Osvaldo (ejercicio 3) pero por división y conquista. 

# Indicar y justificar adecuadamente la complejidad del algoritmo implementado. Es probable que la complejidad de ambas soluciones no 
# quede igual, no te estreses por ello.

# Tres escenarios:
# 1) Comprar y vender en la mitad izquierda
# 2) Comprar y vender en la mitad derecha
# 3) Comprar en la mitad izquierda y vender en la mitad derecha

def _inmueble_compra(predicciones, inicio, fin):

    if (fin - inicio) <= 1:
        return inicio if predicciones[inicio] < predicciones[fin] else fin
    
    medio = (inicio + fin) // 2

    izq = _inmueble_compra(predicciones, inicio, medio)
    der = _inmueble_compra(predicciones, medio+1, fin)

    return izq if predicciones[izq] < predicciones[der] else der

# Complejidad: Teorema maestro

# A: 2 (En cada ejecution tenemos 2 llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 0 (El resto de operaciones son constantes)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^0) = 2 T(n/2)

# log (A) = log (2) = 1 > C → T(n) = O(n^log (A)) = O(n^log (2)) = O(n^1) = O(n)
#    B         2                            B              2

def _inmueble_venta(predicciones, inicio, fin):

    if (fin - inicio) <= 1:
        return inicio if predicciones[inicio] > predicciones[fin] else fin
    
    medio = (inicio + fin) // 2

    izq = _inmueble_venta(predicciones, inicio, medio)
    der = _inmueble_venta(predicciones, medio+1, fin)

    return izq if predicciones[izq] > predicciones[der] else der

# Complejidad: Teorema maestro

# A: 2 (En cada ejecution tenemos 2 llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 0 (El resto de operaciones son constantes)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^0) = 2 T(n/2)

# log (A) = log (2) = 1 > C → T(n) = O(n^log (A)) = O(n^log (2)) = O(n^1) = O(n)
#    B         2                            B              2

def inmueble(predicciones):
    venta = _inmueble_venta(predicciones, 0, len(predicciones)-1)
    compra = _inmueble_compra(predicciones, 0, venta)

    return compra, venta

# Complejidad: O(n)

assert inmueble([3, 7, 9]) == (0, 2)
assert inmueble([3, 4, 7, 10, 9]) == (0, 3)