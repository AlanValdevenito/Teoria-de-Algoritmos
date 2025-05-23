# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. Allí reina el caos y la 
# delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. En particular, nos vamos a centrar en unos 
# pedidos que recibe de parte de dichos grupos por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control 
# sobre un rango de kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ). Si hay una 
# mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse). Cada mafia pide por un 
# rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos. 

# Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos 
# otorgados (asegurándose  de no otorgarle algún lugar a dos mafias diferentes). 

# Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y  determine a cuáles se les otorgará control, de forma 
# que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?.

# Notamos que este problema es similar al problema de Scheduling donde en lugar de un aula tenemos un territorio.

# Tenemos como regla de dominio que no puede haber dos mafias ocupando el mismo territorio.

INICIO = 0
FIN = 1
ULTIMO = -1

def hay_interseccion(p1, p2):
    return (p2[FIN] >= p1[INICIO])

# Pedidos: lista de tuplas con (km inicio, km fin)
def asignar_mafias(pedidos):
    pedidos_ordenados = sorted(pedidos, key=lambda p: p[FIN])

    asignaciones = []

    for p in pedidos_ordenados:

        if (len(asignaciones) == 0) or (not hay_interseccion(p, asignaciones[ULTIMO])):
            asignaciones.append(p)

    return asignaciones

# Complejidad

# El algoritmo ordena los pedidos segun KM de fin de forma ascendente. Esto tiene una complejidad de O(p log(p)) con p la cantidad de pedidos.

# El algoritmo itera los pedidos ordenados. Esto tiene una complejidad de O(p) con p la cantidad de pedidos.

# Luego, el algoritmo tiene una complejidad de O(p log(p)) con p la cantidad de pedidos.


# Algoritmo Greedy

# El algoritmo tiene como regla sencilla asignar la primera mafia cuyo KM de fin sea menor mientras no haya interseccion con el territorio de la ultima mafia asignada.

# El algoritmo  aplica iterativamente esta regla para maximizar la cantidad de pedidos otorgados.

# ¿El algoritmo es optimo?. Si, es optimo ya que al asignar la mafia cuyo KM fin sea menor, el territorio asignado ocupara menos territorio dejando la mayor cantidad 
# posible de territorio libre para futuras asignaciones, maximizando la cantidad total de territorios asignados.

assert asignar_mafias([(1,4), (6,12), (15,20), (3,7), (9,15), (2,10), (12,16), (5,11)]) == [(1,4), (5,11), (12,16)]


# 1                 20
# |--| |-----| |----|
#   |---| |-----|
#  |-------| |---|
#     |-----|


# 1                18
# |--|

#            |--|
#     |-----|


assert asignar_mafias([(1,3), (2,4), (3,5), (4,6)]) == [(1,3), (4,6)]
assert asignar_mafias([(1, 10), (2, 3), (4, 5), (6, 7), (8, 9)]) == [(2, 3), (4, 5), (6, 7), (8, 9)]