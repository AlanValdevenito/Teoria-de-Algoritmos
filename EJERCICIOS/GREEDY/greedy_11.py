# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen. 

# Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir los 
# productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5 y para 
# una lista con los pesos: [ 4, 2, 1, 3, 5 ]. 

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar. 

# Indicar y justificar la complejidad del algoritmo implementado.

def bolsas(capacidad, productos):
    productos_ordenados = sorted(productos, reverse=True)
    bolsas = []

    for producto in productos_ordenados:
        colocado = False

        for bolsa in bolsas:
            peso = sum(bolsa)
            
            if (peso + producto) <= capacidad:
                bolsa.append(producto)
                colocado = True
                break

        if not colocado:
            bolsas.append([producto])

    return bolsas

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de elementos lo cual
#                 en el peor caso tiene una complejidad de O(n²). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n²).

# 2) Algoritmo Greedy: Tenemos como regla sencilla quedarnos con el elemento cuyo peso sea mayor y que no supere la capacidad 
#                      de la bolsa actual. Luego, se aplica iterativamente esta regla con el objetivo de guardar aquellos elementos
#                      que minimizan la cantidad de bolsas.

#                      La solucion no es siempre optima. Veamos un contraejemplo.

#                      Productos: [3,3,2,2,2,2] con capacidad 7 → Solución: [[3, 3], [2, 2, 2], [2]]

#                      La solución óptima seria [[3,2,2], [3,2,2]].

assert bolsas(5, [4,2,1,3,5]) == [[5], [4, 1], [3, 2]]