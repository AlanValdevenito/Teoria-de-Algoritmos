# Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
# original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
# se deben utilizar al menos K elementos. 
# 
# Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn con pesos p1, p2, ..., pn, y valores W y K, encontrar 
# el subconjunto de al menos K elementos, cuya suma de valor sea máxima y cuyo peso no exceda el valor de W.

VALOR = 0
PESO = 1
ELEMENTOS = 2

def es_compatible(conjunto_parcial, W, elemento):
    return conjunto_parcial[PESO] + elemento[PESO] <= W

def _mochila(elementos, W, K, actual, conjunto_parcial, conjunto_optimo):
    
    if actual >= len(elementos):
        return [conjunto_parcial[VALOR], conjunto_parcial[PESO], list(conjunto_parcial[ELEMENTOS])] if conjunto_parcial[VALOR] > conjunto_optimo[VALOR] else [conjunto_optimo[VALOR], conjunto_optimo[PESO], list(conjunto_optimo[ELEMENTOS])]

    # Poda: No alcanzan los elementos restantes para alcanzar K elementos
    if (len(elementos) - actual) + len(conjunto_parcial[ELEMENTOS]) < K:
        return [conjunto_parcial[VALOR], conjunto_parcial[PESO], list(conjunto_parcial[ELEMENTOS])] if conjunto_parcial[VALOR] > conjunto_optimo[VALOR] else [conjunto_optimo[VALOR], conjunto_optimo[PESO], list(conjunto_optimo[ELEMENTOS])]
   
    elemento = elementos[actual]
    
    # Poda: El elemento actual entra en la mcohila
    if es_compatible(conjunto_parcial, W, elemento):
        conjunto_parcial[VALOR] += elemento[VALOR]
        conjunto_parcial[PESO] += elemento[PESO]
        conjunto_parcial[ELEMENTOS].append(elemento)
        
        conjunto_optimo = _mochila(elementos, W, K, actual + 1, conjunto_parcial, conjunto_optimo)

        conjunto_parcial[VALOR] -= elemento[VALOR]
        conjunto_parcial[PESO] -= elemento[PESO]
        conjunto_parcial[ELEMENTOS].pop()

    return _mochila(elementos, W, K, actual + 1, conjunto_parcial, conjunto_optimo)

def mochila(elementos, W, K):
    return _mochila(elementos, W, K, 0, [0, 0, []], [0, 0, []])

assert mochila([(5, 10)], 10, 1)[ELEMENTOS] == [(5, 10)]
assert mochila([(5, 5), (3, 3), (7, 7)], 10, 2)[ELEMENTOS] == [(3, 3), (7, 7)]
assert mochila([(1, 1), (2, 1), (3, 1)], 2, 2)[ELEMENTOS] == [(2, 1), (3, 1)]
assert mochila([(15, 7), (8, 4), (8, 4)], 8, 2)[ELEMENTOS] == [(8, 4), (8, 4)]
assert mochila([(3, 2), (4, 3), (5, 4), (6, 5)], 5, 2)[ELEMENTOS] == [(3, 2), (4, 3)]
assert mochila([(10, 1), (15, 2), (40, 3)], 6, 3)[ELEMENTOS] == [(10, 1), (15, 2), (40, 3)]
assert mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11, 2)[ELEMENTOS] == [(2, 3), (9, 8)]
assert mochila([(15, 2), (40, 3)], 6, 3)[ELEMENTOS] == []