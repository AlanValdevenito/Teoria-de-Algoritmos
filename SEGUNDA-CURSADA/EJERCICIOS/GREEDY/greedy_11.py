# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 

# Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los 
# productos en la menor cantidad posible de bolsas. 

# Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Buscamos minimizar la cantidad de bolsas.

# Notamos que este es un problema similar a Bin-Packing el cual es NP-Completo. Dicho esto, el algoritmo Greedy no sera optimo.

PRODUCTOS = 0
PESO = 1

def bolsas(capacidad, productos):
    productos_ordenados = sorted(productos, reverse = True)
    bolsas = []

    for producto in productos_ordenados:
        # print(f"\nProducto actual: {producto}")

        guardado = False

        for bolsa in bolsas:
            # print(f"Bolsa actual: {bolsa}")

            if (bolsa[PESO] + producto) <= capacidad:
                bolsa[PRODUCTOS].append(producto)
                bolsa[PESO] += producto

                guardado = True

                # print(f"Hay capacidad en la bolsa")
                # print(f"Guardamos producto")
                # print(f"Bolsa resultante: {bolsa}")

                break

        if not guardado:
            # print(f"No hay capacidad en las bolsas anteriores, usamos una nueva")
            # print(f"Guardamos producto")

            bolsas.append([[producto], producto])

    return [bolsa[0] for bolsa in bolsas]

# Complejidad

# El algoritmo ordena los productos de mayor a menor. Esto tiene una complejidad de O(n log(n)) con n la cantidad de productos.

# El algoritmo itera los n productos y por cada producto itera las b bolsas. Esto tiene una complejidad de O(n + b) con n la cantidad de productos y b la cantidad de bolsas.

# En el peor caso tendriamos una bolsa por producto y cada producto necesitaria revisar todas las bolsas antes de encontar una con capacidad, lo que resultaria en una complejidad 
# de O(n^2) con n la cantidad de productos.

# Como el numero de bolsas crece gradualmente, el promedio de bolsas que se deben iterar es menor que n.

# Luego, la complejidad del algoritmo es O(n log(n)) con n la cantidad de productos.


# Algoritmo Greedy

# El algoritmo tiene como regla sencilla guardar primero los productos de mayor peso en alguna bolsa con capacidad siempre y cuando no se exceda la capacidad P.

# Aplicar esta regla sencilla nos permite obtener el optimo local. Luego, aplicandola de forma iterativa obtenemos el optimo global.

# ¿El algoritmo es optimo?. No, el algoritmo no es optimo. La entrada (7, [3,3,2,2,2,2]) daria como resultado [[3, 3], [2, 2, 2], [2]] cuando el optimo seria [[3,2,2], [3,2,2]].


# Seguimiento

# Producto actual: 5
# No hay capacidad en las bolsas anteriores, usamos una nueva
# Guardamos producto

# Producto actual: 4
# Bolsa actual: [[5], 5]
# No hay capacidad en las bolsas anteriores, usamos una nueva
# Guardamos producto

# Producto actual: 3
# Bolsa actual: [[5], 5]
# Bolsa actual: [[4], 4]
# No hay capacidad en las bolsas anteriores, usamos una nueva
# Guardamos producto

# Producto actual: 2
# Bolsa actual: [[5], 5]
# Bolsa actual: [[4], 4]
# Bolsa actual: [[3], 3]
# Hay capacidad en la bolsa
# Guardamos producto
# Bolsa resultante: [[3, 2], 5]

# Producto actual: 1
# Bolsa actual: [[5], 5]
# Bolsa actual: [[4], 4]
# Hay capacidad en la bolsa
# Guardamos producto
# Bolsa resultante: [[4, 1], 5]


assert bolsas(5, [4,2,1,3,5]) == [[5], [4, 1], [3, 2]]


# Notamos que si el algoritmo tuviera como regla sencilla guardar primero los productos de menor peso este no seria optimo. 
# Contraejemplo: La entrada (5, [4,2,1,3,5]) daria como resultado [[1,2], [3], [4], [5]] cuando el optimo seria [[5], [4, 1], [3, 2]].

# Notamos que si el algoritmo tuviera como regla sencilla guardar primero los productos de mayor peso este no seria optimo. 
# Contraejemplo: La entrada (5, [4,2,1,3,5]) daria como resultado [[5], [4], [3,2], [1]] cuando el optimo seria [[5], [4, 1], [3, 2]].