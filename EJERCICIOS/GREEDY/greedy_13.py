# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus 
# celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas 
# antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).

# Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales 
# positivos) desordenadas, y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan 
# cobertura, y se construya para esto la menor cantidad de antenas posibles. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?.

def cobertura(casas, R, K):
    casas_ordenadas = sorted(casas)
    antenas = []

    i = 0
    n = len(casas_ordenadas)
    while (i < n):

        # Si estamos fuera de la jurisdiccion del intendente, continuamos con la casa siguiente
        if (casas_ordenadas[i] > K):
            i += 1
            continue

        # Colocamos una antena en la posición más alejada posible que aún cubra la casa actual
        ubicacion_antena = casas_ordenadas[i] + R

        # Si la ubicacion de la antena excede la jurisdiccion del indentende, la colocamos en la posicion mas alejada posible
        if ubicacion_antena > K:
            ubicacion_antena = K

        antenas.append(ubicacion_antena)

        # Avanzamos al siguiente punto que no esté cubierto por la antena actual
        while (i < n) and (casas_ordenadas[i] <= ubicacion_antena + R):
            i += 1
            
    return antenas

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de casas lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla sencilla ordenar de menor a mayor las ubicaciones de las casas y siempre colocar una antena
#                      en la posicion mas alejada posible que aun cubra la casa actual. Luego, se aplica iterativamente esta regla para 
#                      que todas las casas tengan cobertura. La solucion es optima ya que ya que al colocar cada antena de forma que 
#                      cubra el punto más lejano  posible hacia adelante, se minimiza el número total de antenas necesarias para 
#                      cubrir todas las casas.



'''
Greedy: el algoritmo es greedy porque su regla sencilla es que en cada paso 
coloca una antena que cubre la casa actual y luego se mueve al punto más lejano 
dentro de la cobertura actual que necesita una antena, intentando cubrir tantas 
casas como sea posible con cada antena nueva. Con esto, en cada decisión que 
toma, está consiguiendo un óptimo local, que sería cubrir la mayor cantidad de 
Km posible con cada antena.

Complejidad del algoritmo: la complejidad temporal es O(nlogn) debido al 
ordenamiento inicial de las casas, donde n es el número de casas. Después del 
ordenamiento, el algoritmo recorre las casas una vez, proceso que tiene una 
complejidad O(n). Entonces, en suma de complejidades predomina la mayor, 
O(nlogn).

Optimalidad: este algoritmo greedy proporciona una solución óptima para este 
problema, ya que al colocar cada antena de forma que cubra el punto más lejano 
posible hacia adelante, se minimiza el número total de antenas necesarias para 
cubrir todas las casas.
'''

assert cobertura([150, 50, 100], 50, 1000) == [100]
assert cobertura([50, 150, 105], 50, 1000) == [100]
assert cobertura([51, 107, 844, 802, 151, 902], 50, 1000) == [101, 852]
assert cobertura([], 50, 1000) == []
assert cobertura([1050, 150, 50, 1100, 100], 50, 1000) == [100]
assert cobertura([100, 290], 50, 300) == [150, 300]