# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes 
# que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en 
# total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 

# Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan 
# la menor cantidad de espacios vacíos).

VALOR = 0
ELEMENTOS = 1

def es_compatible(conjunto_parcial, W, elemento):
    return conjunto_parcial[VALOR] + elemento <= W

def _max_grupos_bodegon(elementos, W, actual, conjunto_parcial, conjunto_optimo):

    if actual >= len(elementos):
        return [conjunto_parcial[VALOR], list(conjunto_parcial[ELEMENTOS])] if conjunto_parcial[VALOR] > conjunto_optimo[VALOR] else [conjunto_optimo[VALOR], list(conjunto_optimo[ELEMENTOS])]

    # Poda: El conjunto parcial ocupo todo el espacio
    if conjunto_parcial[VALOR] == W:
        return [conjunto_parcial[VALOR], list(conjunto_parcial[ELEMENTOS])]
    
    # Poda: El conjunto parcial supera al optimo
    if conjunto_parcial[VALOR] > conjunto_optimo[VALOR]:
        conjunto_optimo = [conjunto_parcial[VALOR], list(conjunto_parcial[ELEMENTOS])]
    
    elemento = elementos[actual]
    
    # Poda: El elemento actual entra en la mcohila
    if es_compatible(conjunto_parcial, W, elemento):
        conjunto_parcial[VALOR] += elemento
        conjunto_parcial[ELEMENTOS].append(elemento)
        
        conjunto_optimo = _max_grupos_bodegon(elementos, W, actual + 1, conjunto_parcial, conjunto_optimo)

        conjunto_parcial[VALOR] -= elemento
        conjunto_parcial[ELEMENTOS].pop()

    return _max_grupos_bodegon(elementos, W, actual + 1, conjunto_parcial, conjunto_optimo)

def max_grupos_bodegon(elementos, W):
    return _max_grupos_bodegon(elementos, W, 0, [0, []], [0, []])[ELEMENTOS]

assert max_grupos_bodegon([6], 12) == [6]
assert max_grupos_bodegon([5, 6], 12) == [5, 6]
assert max_grupos_bodegon([1, 3], 4) == [1, 3]
assert max_grupos_bodegon([10, 7, 5, 13], 16) == [10, 5]