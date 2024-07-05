# Implementar un algoritmo tipo Backtracking que reciba una cantidad de dados n y una suma s. La función debe devolver todas las tiradas posibles de n dados cuya 
# suma es s.

# Por ejemplo, con n = 2 y s = 7, debe devolver [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]. 

# ¿De qué complejidad es el algoritmo en tiempo?. ¿Y en espacio?.

MIN_DADO = 1
MAX_DADO = 6

def _sumatoria_dados(dados, suma, sumatoria_parcial, sumatorias):

    # Vemos si se llego a una solucion
    if (sum(sumatoria_parcial) == suma) and (dados == 0):
        sumatorias.append(sumatoria_parcial[:])
        return
    
    # Vemos si se pasa de s incluso si se elige el valor mas chico para los tiros restantes
    if (sum(sumatoria_parcial) + dados*MIN_DADO) > suma:
        return
    
    # Vemos si no alcanzo a s incluso si se elige el valor mas grande para los tiros restantes
    if (sum(sumatoria_parcial) + dados*MAX_DADO) < suma:
        return
    
    for valor in range(MIN_DADO, MAX_DADO+1):
        sumatoria_parcial.append(valor)
        _sumatoria_dados(dados - 1, suma, sumatoria_parcial, sumatorias)
        sumatoria_parcial.pop()

    return

def sumatoria_dados(n, s):
    sumatorias = []
    _sumatoria_dados(n, s, [], sumatorias)
    return sumatorias

# Complejidad: La complejidad temporal y espacial resulta ser O(d^n) donde d es la cantidad de lados que tienen los n dados.

assert sumatoria_dados(2, 7) == [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]]