# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren sentarse a comer, y la cantidad de integrantes 
# que conforma a cada uno. Para simplificar su trabajo, se los anota en un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en 
# total n grupos. Como se trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden sentarse. 

# Implementar un algoritmo que, por backtracking, obtenga el conjunto de grupos que ocupan la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan 
# la menor cantidad de espacios vacíos).

def _max_grupos_bodegon(P, W, grupos_parcial, grupos, actual):

    print(f"Mesa parcial: {grupos_parcial}")

    if (actual >= len(P)):

        if (sum(grupos_parcial) >= sum(grupos)):
            grupos.clear()
            grupos.extend(grupos_parcial)

        return
    
    grupo = P[actual]
    grupos_parcial.append(grupo)
    if (sum(grupos_parcial) <= W):
        _max_grupos_bodegon(P, W, grupos_parcial, grupos, actual + 1)

    grupos_parcial.pop()
    _max_grupos_bodegon(P, W, grupos_parcial, grupos, actual + 1)

def max_grupos_bodegon(P, W):
    grupos = []
    _max_grupos_bodegon(P, W, [], grupos, 0)
    return grupos

assert max_grupos_bodegon([6], 12) == [6]
assert max_grupos_bodegon([5, 6], 12) == [5, 6]
assert max_grupos_bodegon([1, 3], 4) == [1, 3]
assert max_grupos_bodegon([10, 7, 5, 13], 16) == [10, 5]