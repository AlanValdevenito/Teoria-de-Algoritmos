# Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene un valor, y un peso que ocupa de la capacidad total. 
# Queremos maximizar el valor de lo que llevamos sin exceder la capacidad. Implementar un algoritmo Greedy que, reciba dos arreglos de 
# valores y pesos de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total. 

# Indicar y justificar la complejidad del algoritmo implementado. 
# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar. 
# ¿Por qué se trata de un algoritmo Greedy?. Justificar.

VALOR = 0
PESO = 1

def ordenar_por_mayor_relacion(elementos):
    return sorted(elementos, key=lambda e: e[VALOR]//e[PESO], reverse=True)

# Cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementos_ordenados = ordenar_por_mayor_relacion(elementos)
    elementos_maximizados = []

    for e in elementos_ordenados:

        if W <= 0:
            break

        if W - e[PESO] >= 0:
            W -= e[PESO]
            elementos_maximizados.append(e)

    return elementos_maximizados

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de elementos lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla sencilla quedarnos con el elemento cuya relacion v/w sea mayor y que no supere la capacidad 
#                      de la mochila. Luego, se aplica iterativamente esta regla con el objetivo de guardar aquellos elementos
#                      que maximizan la ganancia total. Básicamente calculamos v/w, ordenamos por mayor valor y vemos cuantos 
#                      elementos entran en la mochila. Lo que hacemos con esta división es que para cada elemento de valor 
#                      V, lo castigamos con el peso W. Mientras mayor peso, más se castiga a ese elemento.

#                      La solucion no es siempre optima. Veamos un contraejemplo.

#                      Elementos (v, w):[(3,1),(10,10)] → Solución: [(3,1)]

#                      Guardaríamos el primer, pero la solución óptima seria guardar el segundo elemento.

assert mochila([(10,10), (9,9), (8,1)], 10) == [(8,1), (9,9)]
assert mochila([(10000, 11), (1, 10)], 10) == [(1, 10)]
assert mochila([(1, 5), (5, 4)], 4) == [(5, 4)]