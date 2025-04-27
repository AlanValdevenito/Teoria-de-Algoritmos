# Tati empezó a trabajar en un laboratorio químico, donde trabaja con compuestos que se vaporizan o subliman muy
# rápidamente, por lo que suelen estar almacenados en congeladores. ¿El problema?. Su predecesora, Nerea, tenía un
# único trabajo y lo hizo mal: en vez de almacenar todos los compuestos en un único congelador, guardó cada compuesto
# en un congelador por separado.

# La empresa no puede sostener un costo tan elevado, y deben deshacerse de todos los congeladores (salvo 1). Esto se
# resuelve tan simple como pasar todos los compuestos a un único congelador, pero desde el momento que uno de estos se
# abre, se empieza a perder contenido de los compuestos que lleva dentro porque se vuelven gas, y desean minimizar las
# pérdidas que esto produzca. Lo que se puede hacer es, en una unidad de tiempo, abrir dos congeladores A y B, y mover
# todo lo que haya en el congelador A al B. Se perderá en el medio el equivalente de lo que pierde cada componente por
# unidad de tiempo (dato conocido para cada uno). Se puede seleccionar cualquier par de congeladores para hacer lo
# antes mencionado. Ejemplo: si tengo el congelador A con el compuesto c1 que pierde 5 por unidad de tiempo, y el
# congelador B con el compuesto c2 que pierde 3 por unidad de tiempo, mover lo del congelado A al B nos implica una
# pérdida de 5 + 3 = 8. Si ahora movemos lo que hay en el congelador B al congelador C (que tiene los componentes c3,
# c4 y c5 con pérdidas de 7, 4 y 1 respectivamente), el costo de ese movimiento será 5 + 3 + 7 + 4 + 1 = 20, lo cual se
# suma, obviamente, a cualquier otra pérdida anterior antes incurrida.

# Implementar un algoritmo greedy que obtenga el mínimo de pérdida que se puede lograr para terminar con un único
# congelador. A fines del parcial no es necesario indicar cómo es este proceso, sólo el valor final. 

# Indicar y justificar la complejidad del algoritmo. 

# Justificar por qué el algoritmo implementado es, en efecto, un algoritmo greedy. 

# ¿Es el algoritmo implementado óptimo? Si es, dar una breve explicación, si no lo es dar un contraejemplo.

import heapq

PERDIDA = 0
COMPUESTOS = 1

def mover_compuestos(congeladores):
    heap_congeladores = [(sum(c), c) for c in congeladores]
    heapq.heapify(heap_congeladores)

    perdida = 0

    while len(heap_congeladores) > 1:

        congelador_a = heapq.heappop(heap_congeladores)
        congelador_b = heapq.heappop(heap_congeladores)

        congelador = (congelador_a[PERDIDA] + congelador_b[PERDIDA], congelador_a[COMPUESTOS] + congelador_b[COMPUESTOS])
        heapq.heappush(heap_congeladores, congelador)

        perdida += congelador_a[PERDIDA] + congelador_b[PERDIDA]

    return perdida


# Complejidad

# Iteramos la lista de congeladores para crear una nueva lista, lo cual tiene una complejidad de O(n) con n la cantidad de congeladores.

# Transformamos la lista de congeladores en un heap de minimos lo cual tiene una complejidad de O(n) con n la cantidad de congeladores.

# Iteramos la lista de congeladores hasta que solamente haya un unico congelador y en cada iteracion sacamos dos elementos del heap e insertamos otro lo cual
# tiene una complejidad total de (n log(n)) con n la cantidad de congeladores.

# Luego, la complejidad resutla O(n log(n)) con n la cantidad de congeladores.


# Algoritmo Greedy

# El algoritmo Greedy tiene como regla sencilla seleccionar los dos congeladores que tengan menor perdida y mover sus compuestos de un congelador a otro.

# Luego, se aplica iterativamente esta regla hasta tener un unico congelador.

# ¿El algoritmo es optimo?. Si, es optimo

# Dado que se utiliza un heap de minimos siempre se seleccionan los dos congelador que tenga menor perdida, lo cual minimiza en cada iteracion la perdida total.


congeladores = [[5, 3], [7, 4, 1], [8]]
assert mover_compuestos(congeladores) == 44

congeladores = [[7, 4, 1], [7], [8], [5, 5], [11]]
assert mover_compuestos(congeladores) == 111