# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la ciudad costera de Ciudad
# República. Allí reina el caos y la delincuencia, a tal punto que quien termina organizando las pequeñas mafias locales
# no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte de dichos grupos por el
# control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de
# kilómetros (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 5, la mafia 2 le pide del 3 al 8, etc. . . ). Si hay una
# mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden
# solaparse). Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”,
# indistintamente de los kilómetros pedidos. Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con
# nadie, así lo único que le interesa es maximizar la cantidad de permisos otorgados (asegurándose de no otorgarle algún
# lugar a dos mafias diferentes). 

# Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia, y determine a cuáles se les 
# otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?.

KM_INICIO = 0
KM_FIN = 1

ULTIMO = -1

def asignar_mafias(pedidos):
    pedidos_ordenados = sorted(pedidos, key=lambda p: p[KM_FIN])
    pedidos_otorgados = []

    for pedido in pedidos_ordenados:
    
        if (len(pedidos_otorgados) == 0) or (pedidos_otorgados[ULTIMO][KM_FIN] < pedido[KM_INICIO]):
            pedidos_otorgados.append(pedido)

    return pedidos_otorgados

# Complejidad

# Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de pedidos lo cual tiene una complejidad 
# de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad resultante es O(n log(n)) con n la cantidad de pedidos.

# Algoritmo Greedy

# Tenemos como regla de dominio que no puede haber dos mafias ocupando el mismo territorio y como regla sencilla otorgarle permisos 
# a aquella mafia tal que el kilometraje final de su pedido sea menor. Luego, se aplica iterativamente esta regla para maximizar la 
# cantidad de pedidos otorgados. La solucion es optima ya que no existe un contra ejemplo que demuestre lo contrario.

assert asignar_mafias([(1,4), (6,12), (15,20), (3,7), (9,15), (2,10), (12,16), (5,11)]) == [(1,4), (5,11), (12,16)]

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

           |---|
    |-----|
"""

assert asignar_mafias([(1,3), (2,4), (3,5), (4,6)]) == [(1,3), (4,6)]