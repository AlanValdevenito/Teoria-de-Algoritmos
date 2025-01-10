# Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar
# cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada
# moneda, sino una cantidad específica (y esto hace que pueda no haber solución).

# Suponer que la función a invocar es cambio(n, monedas, cantidad_x_monedas), donde n sea el valor a devolver en cambio, monedas 
# sea una lista ordenada de los valores de las monedas, y cantidad_x_monedas un diccionario.

def _cambio(n, monedas, cantidad_x_monedas, n_actual, moneda_actual, cambio_optimo, cambio_actual):

    # print(f"Estado actual: {cambio_actual}")
    # print(f"Estado optimo: {cambio_optimo}\n")

    # Si la suma del cambio actual es igual al cambio a obtener, comparamos con el óptimo
    if n_actual == n:
        if not cambio_optimo or len(cambio_actual) < len(cambio_optimo):
            return list(cambio_actual)  # Retornamos una copia del cambio actual como óptimo
        
        return cambio_optimo

    # Si la suma del cambio actual supera el objetivo o ya no puede ser óptima, retornamos
    if n_actual > n or (cambio_optimo and len(cambio_actual) >= len(cambio_optimo)):
        return cambio_optimo

    # Exploramos las opciones de monedas
    for i in range(moneda_actual, len(monedas)):
        moneda = monedas[i]

        if cantidad_x_monedas[moneda] > 0:
            cantidad_x_monedas[moneda] -= 1
            cambio_actual.append(moneda)

            cambio_optimo = _cambio(
                n, monedas, cantidad_x_monedas,
                n_actual + moneda, i,  # Mantenemos el índice i (permite reutilizar la misma moneda)
                cambio_optimo, cambio_actual
            )

            cantidad_x_monedas[moneda] += 1
            cambio_actual.pop()

    return cambio_optimo


def cambio(n, monedas, cantidad_x_monedas):
    return _cambio(n, monedas, cantidad_x_monedas, 0, 0, [], [])

assert cambio(583, [500, 100, 50, 20, 10, 5, 1], {500: 2, 100: 5, 50: 0, 20: 3, 10: 2, 5: 10, 1: 5}) == [500, 20, 20, 20, 10, 10, 1, 1, 1]
assert cambio(11, [5, 2, 1], {5: 1, 2: 3, 1: 5}) == [5, 2, 2, 2]