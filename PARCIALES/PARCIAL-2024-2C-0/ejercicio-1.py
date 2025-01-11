# Resolver, utilizando backtracking, el problema de la mochila con cantidades mínimas. Este tiene el mismo planteo al
# original pero además cuenta con un parámetro K, donde además de las condiciones impuestas para el problema original,
# se deben utilizar al menos K elementos. Es decir, el planteo completo es: Dados n elementos de valores v1, v2, ..., vn
# con pesos p1, p2, ..., pn, y valores W y K, encontrar el subconjunto de al menos K elementos, cuya suma de valor sea
# máxima y cuyo peso no exceda el valor de W .

VALOR = 0
PESO = 1
ELEM = 2

def _mochila(elementos, w, k, elemento_actual, solucion_actual, solucion_optima):

    # print(f"Elemento actual: {elemento_actual}")
    # print(f"Conjunto parcial: {solucion_actual}")
    # print(f"Conjunto optimo: {solucion_optima}\n")

    if len(solucion_actual[ELEM]) == k:
        return [solucion_actual[VALOR], solucion_actual[PESO], list(solucion_actual[ELEM])] if solucion_actual[VALOR] > solucion_optima[VALOR] else [solucion_optima[VALOR], solucion_optima[PESO], list(solucion_optima[ELEM])]

    if len(elementos) == elemento_actual:
        return [solucion_actual[VALOR], solucion_actual[PESO], list(solucion_actual[ELEM])] if solucion_actual[VALOR] > solucion_optima[VALOR] else [solucion_optima[VALOR], solucion_optima[PESO], list(solucion_optima[ELEM])]

    elemento = elementos[elemento_actual]
    solucion_actual[ELEM].append(elemento)

    if (solucion_actual[PESO] + elemento[PESO] <= w):
        solucion_actual[PESO] = solucion_actual[PESO] + elemento[PESO]
        solucion_actual[VALOR] = solucion_actual[VALOR] + elemento[VALOR]
        
        solucion_optima = _mochila(elementos, w, k, elemento_actual + 1, solucion_actual, solucion_optima)
        
        solucion_actual[PESO] = solucion_actual[PESO] - elemento[PESO]
        solucion_actual[VALOR] = solucion_actual[VALOR] - elemento[VALOR]

    solucion_actual[ELEM].pop()
    return _mochila(elementos, w, k, elemento_actual + 1, solucion_actual, solucion_optima)

def mochila(elementos, w, k):
    return _mochila(elementos, w, k, 0, [0, 0, []], [0, 0, []])

assert mochila([(5, 10)], 10, 1)[ELEM] == [(5, 10)]
assert mochila([(5, 5), (3, 3), (7, 7)], 10, 2)[ELEM] == [(3, 3), (7, 7)]
assert mochila([(1, 1), (2, 1), (3, 1)], 2, 2)[ELEM] == [(2, 1), (3, 1)]
assert mochila([(15, 7), (8, 4), (8, 4)], 8, 2)[ELEM] == [(8, 4), (8, 4)]
assert mochila([(3, 2), (4, 3), (5, 4), (6, 5)], 5, 2)[ELEM] == [(3, 2), (4, 3)]
assert mochila([(10, 1), (15, 2), (40, 3)], 6, 3)[ELEM] == [(10, 1), (15, 2), (40, 3)]
assert mochila([(1, 2), (2, 3), (5, 5), (9, 8)], 11, 2)[ELEM] == [(2, 3), (9, 8)]