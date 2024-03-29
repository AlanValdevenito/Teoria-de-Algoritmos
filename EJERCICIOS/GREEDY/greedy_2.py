# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una determinada cantidad de plata.

# Implementar un algoritmo Greedy que devuelva el cambio pedido, usando la mínima cantidad de monedas/billetes. 

# El algoritmo recibirá un arreglo de valores del sistema monetario, y la cantidad de cambio objetivo a dar, y 
# debe devolver qué monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar si es óptimo, o dar un contraejemplo. 

# ¿Por qué se trata de un algoritmo Greedy?. Justificar.

def cambio(monedas, monto):
    monedas_ordenadas = sorted(monedas, reverse = True)
    cambio = []

    for moneda in monedas_ordenadas:

        while (monto > 0):
            
            if (monto - moneda < 0):
                break

            cambio.append(moneda)
            monto = monto - moneda

    return cambio

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de monedas lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla de dominio que no puede haber dos charlas al mismo tiempo y
#                      como regla sencilla es ordenar de mayor a menor nuestras monedas y siempre utilizar primero el
#                      elemento de mayor valor para ver si este puede ser sustraido del cambio que se tiene que dar.
#                      Luego, se aplica iterativamente esta regla para minimizar la cantidad total de cambio.
#                      La solucion es optima ya que si nuestras monedas fueran [13, 9, 7, 5, 2, 1] y quisieramos
#                      cambio de 16, nuestro algoritmo tendria como resultado [13, 2, 1] cuando en verdad
#                      el resultado optimo para este caso es [9, 7].

monedas1 = [0, 50, 20, 5, 500, 1, 100, 10]
monto1 = 583
resultado1 = cambio(monedas1, monto1)
print(f"Cambio 1 pedido: {resultado1}")

monedas1 = [13, 9, 7, 5, 2, 1]
monto1 = 16
resultado1 = cambio(monedas1, monto1)
print(f"Cambio 2 pedido: {resultado1}")