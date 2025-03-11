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
# congelador. A fines del parcial no es necesario indicar cómo es este proceso, sólo el valor final. Indicar y justificar la
# complejidad del algoritmo. Justificar por qué el algoritmo implementado es, en efecto, un algoritmo greedy. ¿Es el
# algoritmo implementado óptimo?. Si es, dar una breve explicación, si no lo es dar un contraejemplo.

import heapq

SUMA = 0
COMPUESTOS = 1

def mover_compuestos(congeladores):
    min_heap = [(sum(c), c) for c in congeladores]
    heapq.heapify(min_heap)
    
    perdida = 0

    for i in range(0, len(min_heap)-1):

        c1 = heapq.heappop(min_heap)
        c2 = heapq.heappop(min_heap)

        perdida += c1[SUMA] + c2[SUMA]

        c = (c1[SUMA] + c2[SUMA], c1[COMPUESTOS] + c2[COMPUESTOS])

        heapq.heappush(min_heap, c)

    return perdida

# Complejidad

# Iteramos los congeladores para crear un nuevo arreglo, lo cual tiene una complejidad de O(n) siendo n la cantidad de congeladores.

# Creamos un heap de minimos a partir de dicho arreglo, lo cual tiene una complejidad de O(n)

# Iteramos los congeladores, en cada iteracion desencolamos los congeladores (i, i+1) y encolamos un nuevo congelador que contiene
# los compuestos de ambos. Esto tiene una complejidad de O(n) por la iteracion y O(n log(n)) por cada pop/push. 

# Luego, la complejidad resulta ser O(n log(n)).

# Algoritmo Greedy

# El algoritmo tiene como regla sencilla utilizar un heap de minimos teniendo en cuenta la suma total de compuestos que posee cada congelador
# y luego iterarlos de menor a mayor, siempre moviendo los compuestos de tal forma que siempre unamos primero los 2 congeladores tales
# que sus compuestos generen la menor perdida.

# ¿La solucion es optima?. Si, es optima ya que en cada paso del algoritmo se genera la menor perdida debido al uso de un heap de minimos.

congeladores = [[5, 3], [7, 4, 1], [8]]
resultado = mover_compuestos(congeladores)

assert resultado == 44

congeladores = [[7, 4, 1], [7], [8], [5, 5], [11]]
resultado = mover_compuestos(congeladores)

assert resultado == 111