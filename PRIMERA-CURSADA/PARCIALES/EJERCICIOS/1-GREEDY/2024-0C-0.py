# El famoso ladrón Francesco Rizzoli (hermano del “árbitro” de la final del 2014), ha decidido hacer un atraco a un
# laboratorio farmacéutico. Allí puede robarse diferentes fármacos que se están estudiando (en formato líquido). Tiene un
# catálogo del valor de cada fármaco, que puede vender en el mercado negro. De cada fármaco hay una diferente cantidad
# disponible (medible en ml). Rizzoli sólo tiene posibilidad en su equipo de llevarse como máximo L ml en fármacos. Lo
# bueno es que sabe que puede fraccionar y poner proporciones de los fármacos; y en ese caso lo vendería en su valor
# proporcional. 

# Implementar un algoritmo greedy que obtenga los fármacos (y cantidades) que Rizzoli debe robarse para obtener la máxima 
# ganancia posible (el algoritmo debe ser óptimo, en esta familia no se aceptan los robos a medias).

# Justificar por qué el algoritmo propuesto es Greedy. Indicar y justificar la complejidad del algoritmo implementado.

NOMBRE = 0
CANTIDAD = 1
VALOR = 2

def laboratorio(farmacos,  L):
    farmacos_ordenados = sorted(farmacos, key=lambda x: x[VALOR]/x[CANTIDAD], reverse=True)
    robo = []

    cantidad = 0
    capacidad = L

    for farmaco in farmacos_ordenados:

        if (capacidad <= 0):
            break

        if (capacidad - farmaco[CANTIDAD] >= 0):
            capacidad -= farmaco[CANTIDAD]
            cantidad += farmaco[CANTIDAD]
            robo.append((farmaco[NOMBRE], farmaco[CANTIDAD]))
        
        else:
            fraccion = L - cantidad 

            capacidad -= fraccion
            cantidad += fraccion
            robo.append((farmaco[NOMBRE], fraccion))
    
    return robo

farmacos = [("F1", 10, 10), ("F2", 9, 9), ("F3", 1, 8)]
L = 10

assert laboratorio(farmacos, L) == [("F3", 1), ("F1", 9)]

farmacos = [("F1", 1, 3), ("F2", 10, 10)]
L = 10

assert laboratorio(farmacos, L) == [("F1", 1), ("F2", 9)]

# Complejidad

# Ordenamos la lista de farmacos segun la relacion VALOR/CANTIDAD de forma descentente (mayor a menor) y esto tiene una complejidad
# de O(F log(F)) con F la cantidad de farmacos.

# En el peor caso se recorren todos los farmacos lo cual tiene una complejidad de O(F) y en cada iteracion se realizan operaciones O(1).

# Luego, la complejidad resulta ser O(F log(F)) con F la cantidad de farmacos.

# Algoritmo Greedy

# El algoritmo tiene como regla sencilla en cada iteracion guardar farmacos segun la relacion VALOR/CANTIDAD mientras no se supere la 
# capacidad L y en caso de superar dicha capacidad, fraccionar el farmaco hasta alcanzar la capacidad L.

# Se aplica de forma iterativa esta regla hasta alcanzar la capacidad L.

# Ademàs, se ordenan los farmacos segun la relacion VALOR/CANTIDAD para castigar a cada farmaco con su cantidad.