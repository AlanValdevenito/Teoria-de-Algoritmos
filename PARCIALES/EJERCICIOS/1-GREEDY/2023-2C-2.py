# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que
# usa mucho sus celulares. El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que
# construir sobre la ruta nuevas antenas. Cada antena tiene un rango de cobertura de R kilómetros (valor constante
# conocido). 

# Implementar un algoritmo Greedy que reciba las ubicaciones de las casas (número de kilómetro sobre esta ruta) y devuelva 
# los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura, y se construya para 
# esto la menor cantidad de antenas posibles.

# Indicar y justificar la complejidad del algoritmo implementado. 

# Justificar por qué se trata de un algoritmo greedy.

ULTIMA_ANTENA = -1

def cobertura(casas, R, K):
    casas_ordenadas = sorted(casas)
    
    antenas = []

    for casa in casas_ordenadas:

        if (len(antenas) == 0) or not (casa >= antenas[ULTIMA_ANTENA] - R and casa <= antenas[ULTIMA_ANTENA] + R):
            ubicacion = casa + R

            if ubicacion > K:
                ubicacion = K

            antenas.append(ubicacion)

    return antenas

# Complejidad

# Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de casas lo cual tiene una complejidad 
# de O(n). 

# Ademàs, todas las operaciones restantes son O(1). 

# Luego, la complejidad esultante es O(n log(n)).

# Algoritmo Greedy 

# Tenemos como regla sencilla siempre colocar una antena en la posicion mas alejada posible que aun cubra la casa actual. 

# Luego, se aplica iterativamente esta regla para que todas las casas tengan cobertura.

# La solucion es optima ya que ya que al colocar cada antena de forma que cubra el punto más lejano posible hacia adelante, se 
# minimiza el número total de antenas necesarias para cubrir todas las casas.

assert cobertura([150, 50, 100], 50, 1000) == [100]
assert cobertura([50, 150, 105], 50, 1000) == [100]
assert cobertura([51, 107, 844, 802, 151, 902], 50, 1000) == [101, 852]
assert cobertura([], 50, 1000) == []
assert cobertura([100, 290], 50, 300) == [150, 300]