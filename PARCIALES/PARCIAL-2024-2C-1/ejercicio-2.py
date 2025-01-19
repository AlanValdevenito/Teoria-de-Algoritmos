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

def mover_compuestos(congeladores):
    congeladores_ordenados = sorted(congeladores, key=lambda c: sum(c))
    
    perdida = 0

    for i in range(0, len(congeladores_ordenados)-1):

        perdida += sum(congeladores_ordenados[i])
        perdida += sum(congeladores_ordenados[i+1])

        congeladores_ordenados[i+1].extend(congeladores_ordenados[i])

    return perdida

# Complejidad

# Ordenamos la lista de congeladores teniendo en cuenta la suma total de compuestos que posee cada congelador. Calcular la suma total
# de cada congelador tiene una complejidad de O(n x m) siendo n la cantidad de congeladores y m la cantidad de elementos de cada congelador.
# Luego, la complejidad del ordenamiento sera O(n x m + n log (n)) donde n es la cantidad de congeladores y m la cantidad de elementos de 
# cada congelador.

# Por otro lado, iteramos la lista de congeladores ordenados y en cada iteracion se agregan los elementos del congelador i al congelador 
# i+1. Luego, la complejidad sera O(n + m) donde n es la cantidad de congeladores y m la cantidad de elementos de cada congelador.

# Finalmente, la complejidad total sera O(n x m + n log (n)).

# Algoritmo Greedy

# El algoritmo tiene como regla sencilla ordenar los congeladores teniendo en cuenta la suma total de compuestos que posee cada congelador
# y luego iterarlos de menor a mayor, siempre moviendo los compuestos del congelador i al congelador i+1.

# ¿La solucion es optima?. ¿Existe algun contraejemplo?. La solucion no es optima. Un contraejemplo considerar la siguiente configuracion
# de congeladores: [[7, 4, 1], [7], [8], [5, 5], [11]]

# Nuestro algoritmo Greedy lo resolveria de la siguiente forma:
# [7], [8], [5, 5], [11], [7, 4, 1] -> Perdida: 0
# [7, 8], [5, 5], [11], [7, 4, 1] -> Perdida: 15
# [7, 8, 5, 5], [11], [7, 4, 1] -> Perdida: 15 + 25
# [7, 8, 5, 5, 11], [7, 4, 1] -> Perdida: 15 + 25 + 36
# [7, 8, 5, 5, 11], [7, 4, 1] -> Perdida: 15 + 25 + 36 + 48
# [7, 8, 5, 5, 11, 7, 4, 1] -> Perdida: 124

# Mientras que la solucion optima seria la siguiente:
# [7], [8], [5, 5], [11], [7, 4, 1] -> Perdida: 0
# [7, 8], [5, 5], [11], [7, 4, 1] -> Perdida: 15
# [7, 8], [5, 5, 11], [7, 4, 1] -> Perdida: 15 + 21
# [7, 8, 7, 4, 1], [5, 5, 11] -> Perdida: 15 + 21 + 27
# [7, 8, 7, 4, 1], [5, 5, 11] -> Perdida: 15 + 21 + 27 + 48
# [7, 8, 7, 4, 1, 5, 5, 11] -> Perdida: 111

# La solucion optima podria lograrse si se trabajara con un Heap de minimos, de tal forma que siempre unamos primero los 2 congeladores tales
# que sus compuestos generen la menor perdida. La complejidad resultaria ser O(n log(n)) donde n es la cantidad de congeladores.

congeladores = [[5, 3], [7, 4, 1], [8]]
resultado = mover_compuestos(congeladores)

assert resultado == 44

congeladores = [[7, 4, 1], [7], [8], [5, 5], [11]]
resultado = mover_compuestos(congeladores)

assert resultado == 124