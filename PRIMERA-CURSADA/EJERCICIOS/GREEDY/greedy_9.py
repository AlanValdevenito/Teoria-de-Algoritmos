# Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes 
# del deadline. Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia. Para este 
# problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten. Es decir, dados los arreglos de: T tiempo de 
# duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea i empieza en S_i, entonces termina 
# en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0).

# Nuestra latencia máxima será aquella i que maximice el valor L_i.

# Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar 
# la siguiente. Indicar y justificar la complejidad del algoritmo implementado.

# Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla 
# indique: (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar. ¿Por qué se trata de un algoritmo Greedy?. Justificar.

def minimizar_latencia(L_deadline, T_tareas):
    tareas_ordenadas = sorted([(T_tareas[i], L_deadline[i]) for i in range(len(L_deadline))], key=lambda x: x[1])
    tareas = []

    S_i = 0
    for i in range(len(tareas_ordenadas)):
        T_i = tareas_ordenadas[i][0]
        D_i = tareas_ordenadas[i][1]

        L_i = (S_i + T_i) - D_i if (S_i + T_i) > D_i else 0

        S_i += T_i
        tareas.append((T_i, L_i))

    return tareas

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de tareas lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla sencilla ordenar de menor a mayor por deadline nuestras tareas y siempre completar primero 
#                      la tarea de menor deadline. Luego, se aplica iterativamente esta regla para minimizar la latencia máxima en el 
#                      que las tareas se ejecuten. La solucion es optima ya que al hacer las tareas de menor deadline, estoy siempre 
#                      minimizando la latencia posible. Ademàs, es eficiente sin tener en cuenta los tiempos de las tareas ya que no es
#                      necesario porque independientemente del orden en que se hagan las tareas vamos a tardar siempre lo mismo.

assert minimizar_latencia([100, 10], [1, 10]) == [(10, 0), (1, 0)]
assert minimizar_latencia([2, 10], [1, 10]) == [(1, 0), (10, 1)]
assert minimizar_latencia([1, 2, 3, 4], [5, 3, 2, 4]) == [(5, 4), (3, 6), (2, 7), (4, 10)]
assert minimizar_latencia([], []) == []
assert minimizar_latencia([1], [5]) == [(5, 4)]