# Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin. 

# Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas, representando 
# en tuplas los horarios de inicios de las charlas, y sus horarios de fin, e indique cuáles son las charlas 
# a dar para maximizar la cantidad total de charlas. Indicar y justificar la complejidad del algoritmo implementado.

HORA_INICIO = 0
HORA_FIN = 1

ULTIMA_CHARLA = -1

def ordenar_por_menor_valor(elementos):
    return sorted(elementos, key=lambda e: e[HORA_FIN])

def hay_interseccion(anterior, nuevo):
    return anterior[HORA_FIN] >= nuevo[HORA_INICIO] 

def charlas(horarios):
    horarios_ordenados = ordenar_por_menor_valor(horarios)
    charlas = []

    for horario in horarios_ordenados:
        if (len(charlas) == 0) or (not hay_interseccion(charlas[ULTIMA_CHARLA], horario)):
            charlas.append(horario)

    return charlas

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de horarios lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla de dominio que no puede haber dos charlas al mismo tiempo y 
#                      como regla sencilla es quedarnos con la charla que termina antes. Luego, se aplica 
#                      iterativamente esta regla para maximizar la cantidad de charlas. La solucion es optima 
#                      ya que no existe un contra ejemplo que demuestre lo contrario.

pedido1 = [(1,4), (6,12), (15,20), (3,7), (9,15), (2,10), (12,16), (5,11)]
resultado1 = charlas(pedido1)
print(f"{pedido1} →  ¿{resultado1} == [(1,4), (5,11), (12,16)]?\n")

"""
1                 20
|--| |-----| |----|
  |---| |-----|
 |-------| |---|
    |-----|
"""

"""
1                18
|--|

           |--|
    |-----|
"""