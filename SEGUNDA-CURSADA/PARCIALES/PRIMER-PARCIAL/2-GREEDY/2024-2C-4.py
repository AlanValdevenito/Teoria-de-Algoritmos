# Tenemos un listado de proyectos a realizar, que tienen tiempo de inicio y tiempo de finalización. Contamos además con K equipos que
# pueden realizar los proyectos. Cada proyecto puede estar asignado a un único equipo (o ninguno, si no se realiza). No hay distinción
# entre los equipos (todos pueden realizar todos los proyectos). Un mismo equipo no puede estar trabajando en dos proyectos a la
# vez, aunque varios equipos pueden estar trabajando en proyectos diferentes en simultáneo sin problemas. 
# 
# Implementar un algoritmo greedy que determine la asignación de proyectos a los diferentes equipos, de tal manera que se maximice la cantidad de proyectos a 
# realizar. 

# Indicar y justificar la complejidad del algoritmo implementado. Indicar por qué se trata, en efecto, de un algoritmo greedy.

# El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo (es muy probable que el algoritmo NO sea óptimo, así que pensar bien por 
# un contraejemplo antes de decir que lo es).

INICIO = 0
FIN = 1
ULTIMO = -1

def hay_interseccion(p1, p2):
    return (p1[FIN] > p2[INICIO])

def asignar_proyectos(proyectos, K):
    proyectos_ordenados = sorted(proyectos, key = lambda p: p[FIN])
    
    asignaciones = [[] for _ in range(K)]
    asignados = set()

    for equipo in asignaciones:
        for p in proyectos_ordenados:

            if p in asignados:
                continue

            if (len(equipo) == 0) or not hay_interseccion(equipo[ULTIMO], p):
                equipo.append(p)
                asignados.add(p)

    return asignaciones

# Complejidad

# Ordenamos los proyectos por tiempo de finalizacion lo cual tiene una complejidad de O(p log (p)) con p la cantidad de proyectos.

# Iteramos los equipos y para cada equipo iteramos los proyectos ordenados lo cual tiene una complejidad de O(k x p) con k la cantidad de equipos y p 
# la cantidad de proyectos.

# Luego, la complejidad resulta ser O(p log(p) + k x p) con k la cantidad de equipos y p la cantidad de proyectos.

# Algoritmo Greedy

# El algoritmo Greedy tiene como regla sencilla asignar primero los proyectos de tiempo de finalizacion menor siempre y cuando no haya interseccion
# con los proyectos asignados anteriormente. Se asigna cada proyecto al primer equipo que este disponible.

# Luego, se aplica esta regla de forma iterativa.

# ¿El algoritmo es optimo?. No, no es optimo ya que existe el siguiente contraejemplo:

# Consideramos los proyectos [(1,4), (2,7), (8,9), (5,11)] con K = 2.

# Nuestro algoritmo asignaria de la siguiente forma:
# 1) Equipo 1 = [(1,4)]
# 2) Equipo 1 = [(1,4), (8,9)]
# 3) Equipo 2 = [(2,7)]

# Y el proyecto (5,11) no podria ser asignado.

# Notamos que nuestro algoritmo no encuentra el optimo ya que la asignacion optima seria [[(1,4), (5,11)], [(2,7), (8,9)]].

assert asignar_proyectos([(1,3), (4,6), (7,9), (1,9)], 2) == [[(1,3), (4,6), (7,9)], [(1,9)]]

assert asignar_proyectos([(1,5), (2,3), (4,6), (4,7)], 2) == [[(2,3), (4,6)], [(1,5)]]

assert asignar_proyectos([(1,4), (6,12), (14,20), (3,7), (9,15), (2,10), (12,16), (5,11)], 1) == [[(1,4), (5,11), (12,16)]]

assert asignar_proyectos([(1,4), (6,12), (14,20), (3,7), (9,15), (2,10), (12,16), (5,11)], 2) == [[(1,4), (5,11), (12,16)], [(3,7), (9,15)]]

assert asignar_proyectos([(1,4), (6,12), (14,20), (3,7), (9,15), (2,10), (12,16), (5,11)], 3) == [[(1,4), (5,11), (12,16)], [(3,7), (9,15)], [(2,10), (14,20)]]

assert asignar_proyectos([(1,4), (6,12), (14,20), (3,7), (9,15), (2,10), (12,16), (5,11)], 4) == [[(1,4), (5,11), (12,16)], [(3,7), (9,15)], [(2,10), (14,20)], [(6,12)]]

assert asignar_proyectos([(1,4), (2,7), (8,9), (5,11)], 2) == [[(1,4), (8,9)], [(2,7)]]