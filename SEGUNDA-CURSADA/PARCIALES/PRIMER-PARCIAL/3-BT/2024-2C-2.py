# Implementar un algoritmo que, utilizando backtracking, resuelva el problema del cambio (obtener la forma de dar
# cambio en la mínima cantidad de monedas) con una nueva restricción: no se tiene una cantidad indefinida de cada
# moneda, sino una cantidad específica (y esto hace que pueda no haber solución). 

# Suponer que la función a invocar es cambio(n, monedas, cantidad_x_monedas), donde n sea el valor a devolver en cambio, monedas sea una lista
# ordenada de los valores de las monedas, y cantidad_x_monedas un diccionario.

def hay_cantidad(moneda, cantidad_x_monedas):
    return cantidad_x_monedas[moneda] > 0

def _cambio(n, monedas, cantidad_x_monedas, suma_actual, actual, cambio_parcial, cambio_optimo):
    
    if suma_actual == n:
        
        if not cambio_optimo or (len(cambio_parcial) < len(cambio_optimo)):
            return list(cambio_parcial)
        
        return list(cambio_optimo)
    
    if suma_actual > n:
        return list(cambio_optimo)
    
    if cambio_optimo and (len(cambio_optimo) <= len(cambio_parcial)):
        return list(cambio_optimo)

    for i in range(actual, len(monedas)):
        m = monedas[i]

        if not hay_cantidad(m, cantidad_x_monedas): continue

        cambio_parcial.append(m)
        cantidad_x_monedas[m] -= 1

        cambio_optimo = _cambio(n, monedas, cantidad_x_monedas, suma_actual + m, i, cambio_parcial, cambio_optimo)

        cantidad_x_monedas[m] += 1
        cambio_parcial.pop()

    return cambio_optimo

def cambio(n, monedas, cantidad_x_monedas):
    return _cambio(n, monedas, cantidad_x_monedas, 0, 0, [], [])

assert cambio(583, [500, 100, 50, 20, 10, 5, 1], {500: 2, 100: 5, 50: 0, 20: 3, 10: 2, 5: 10, 1: 5}) == [500, 20, 20, 20, 10, 10, 1, 1, 1]
assert cambio(11, [5, 2, 1], {5: 1, 2: 3, 1: 5}) == [5, 2, 2, 2]