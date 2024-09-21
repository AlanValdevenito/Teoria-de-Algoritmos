# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene 
# el número de kilómetro donde está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma 
# que no haya bifurcaciones con vigilancia a más de 50 km.

# Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplo:

# | Ciudad      | Bifurcación |
# |-------------|-------------|
# | Castelli    | 185         |
# | Gral Guido  | 242         |
# | Lezama      | 156         |
# | Maipú       | 270         |
# | Sevigne     | 194         |

# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner 
# otro. Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las 
# ciudades con distancia menor a 50km.

# En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería 
# colocar un móvil policial en Sevigne.

CIUDAD = 0
BIFURCACION = 1

UMBRAL = 50

def bifurcaciones_con_patrulla(ciudades):

    if len(ciudades) == 0:
        return []

    ciudades_ordenadas = sorted(ciudades, key=lambda c: c[BIFURCACION])
    policiales = []

    maxima_distancia = ciudades_ordenadas[0][BIFURCACION] + UMBRAL

    ultima_estacion = float('-inf')

    for i in range(len(ciudades_ordenadas)):

        if (ciudades_ordenadas[i][BIFURCACION] <= ultima_estacion + UMBRAL):
            continue 
            
        if (ciudades_ordenadas[i][BIFURCACION] > maxima_distancia):

            if (len(policiales) > 0) and (policiales[-1][BIFURCACION] + UMBRAL > ciudades_ordenadas[i-1][BIFURCACION]):
                maxima_distancia = ciudades_ordenadas[i][BIFURCACION] + UMBRAL
                continue

            policiales.append(ciudades_ordenadas[i - 1])
            ultima_estacion = ciudades_ordenadas[i - 1][BIFURCACION]
            maxima_distancia = ciudades_ordenadas[i][BIFURCACION] + UMBRAL

    if (ciudades_ordenadas[-1][BIFURCACION] > ultima_estacion + UMBRAL):
        policiales.append(ciudades_ordenadas[-1])

    return policiales

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de ciudades lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla sencilla ordenar de menor a mayor por bifurcacion nuestras ciudades y siempre ubicar primero 
#                      la ciudad anterior a aquella ciudad cuya bifurcacion no este cubierta por la maxima distancia actual. Luego, se 
#                      aplica iterativamente esta regla para minimizar la cantidad de policiales ubicados. La solucion es optima ya que 
#                      al ubicar los policiales lo mas lejos posible teniendo en cuenta la maxima distancia, estoy siempre minimizando 
#                      la cantidad de policiales ubicados. Es decir, todo el tiempo lo que estamos haciendo es posponer lo mas posible 
#                      ubicar un policial.

assert bifurcaciones_con_patrulla([('Castelli', 185), ('Gral Guido', 242), ('Lezama', 156), ('Maipu', 270), ('Sevigne', 194)]) == [('Sevigne', 194), ('Maipu', 270)]
assert bifurcaciones_con_patrulla([('Castelli', 185), ('Gral Guido', 242), ('Sevigne', 194)]) == [('Sevigne', 194)]

assert bifurcaciones_con_patrulla([('a', 50), ('b', 100), ('c', 150)]) == [('b', 100)]
assert bifurcaciones_con_patrulla([('a', 51), ('b', 100), ('c', 149), ('d', 801), ('e', 850), ('f', 899)]) == [('b', 100), ('e', 850)]
assert bifurcaciones_con_patrulla([('b', 100), ('c', 149), ('d', 801), ('e', 850)]) == [('c', 149), ('e', 850)]