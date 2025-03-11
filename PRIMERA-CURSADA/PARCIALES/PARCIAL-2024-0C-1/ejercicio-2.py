# Todos los años la asociación de Tiro con Arco profesional realiza una preclasificación de los n jugadores que terminaron
# en las mejores posiciones del ranking para un evento exclusivo. En la tarjeta de invitación quieren adjuntar el número de
# posición en la que está actualmente y a cuántos rivales invitados logró superar en el ranking, en comparación al ranking
# del año pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado
# ordenado por el ranking actual.

# Implementar un algoritmo que dada la lista mencionada, devuelva (por ejemplo, en un diccionario) a cuántos rivales ha superado 
# cada uno de los invitados. Para realizar esto de forma eficiente, recomendamos utilizar División y Conquista.

# Ejemplo: LISTA: [(A, 3), (B, 4), (C, 2), (D, 8), (E, 6), (F, 5)]. 

# Se puede ver que el jugador A pasó del 3er lugar al 1er lugar, superando al jugador C. El jugador B llegó al segundo lugar y 
# superó al jugador C. El jugador C no logró superar a ninguno de los invitados (si bien se encuentra en la tercera posición, ya 
# tenía el año anterior mejorclasificación que el resto de invitados, por tanto no logró superar a ninguno), etc. . .

JUGADOR = 0
INDICE = 1

def merge(a, b, inversiones):
    i, j = 0, 0
    resultado = []

    # print(f"Merge (antes): {a}, {b}")
    # print(f"Inversiones: {inversiones}")

    while (i < len(a)) and (j < len(b)):

        if a[i][INDICE] < b[j][INDICE]:
            resultado.append(a[i])
            i += 1

        else:
            resultado.append(b[j])

            # Cada vez que agregamos un jugador de 'b' al resultado final, significa que todos los jugadores en 'a' que aún no han sido 
            # agregados han superado a ese jugador de 'b'.

            # Por esto, al insertar un jugador de 'b', hay que recorrer los jugadores de 'a' y actualizar su valor.

            for jugador in a:
                inversiones[jugador[JUGADOR]] = inversiones.get(jugador[JUGADOR], 0) + len(b) - j

            j += 1

    resultado += a[i:]
    resultado += b[j:]

    # print(f"Merge (despues): {resultado}")
    # print(f"Inversiones: {inversiones}\n")

    return resultado, dict(inversiones)

def merge_sort(jugadores, inicio, fin, inversiones):
    
    if (inicio >= fin):
        return [jugadores[inicio]], dict(inversiones)
    
    medio = (inicio + fin) // 2

    izq, izq_inv = merge_sort(jugadores, inicio, medio, inversiones)
    der, der_inv = merge_sort(jugadores, medio + 1, fin, inversiones)

    izq_inv.update(der_inv)

    return merge(izq, der, izq_inv)

def contar_inversiones(jugadores):
    n = len(jugadores)

    _, inversiones = merge_sort(jugadores, 0, n-1, {})

    return inversiones

assert contar_inversiones([("A", 3), ("B", 4), ("C", 2), ("D", 8), ("E", 6), ("F", 5)]) == {"A": 1, "B": 1, "D": 2, "E": 1}

# Complejidad

# A: 1 (Hay escritos dos llamados recursivos)
# B: 2 (Se divide al problema en dos)
# C: 1 (Intercalamos los elementos de los subarreglos izquierdo y derecho de forma ordenada y en el peor caso debemos iterar todo el arreglo)

# T(n) = A.T(n/B) + O(n^C) = 2 T(n/2) + O(n^1) = 2 T(n/2) + O(n)

# log (A) = log (2) = 1 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^1 . log(n)) = O(n log(n))
#    B         2                                B  

# Ejecucion

# Merge (antes): [('A', 3)], [('B', 4)]
# Inversiones: {}
# Merge (despues): [('A', 3), ('B', 4)]
# Inversiones: {}

# Merge (antes): [('A', 3), ('B', 4)], [('C', 2)]
# Inversiones: {}
# Comparamos A con C. Como C < A entonces agregamaos C al resultado. Esto nos dice que A y B superaron a C.
# Merge (despues): [('C', 2), ('A', 3), ('B', 4)]
# Inversiones: {'A': 1, 'B': 1}

# Merge (antes): [('D', 8)], [('E', 6)]
# Inversiones: {}
# Comparamos D con E. Como E < D entonces agregamos E al resultado. Esto nos dice que D supero a E.
# Merge (despues): [('E', 6), ('D', 8)]
# Inversiones: {'D': 1}

# Merge (antes): [('E', 6), ('D', 8)], [('F', 5)]
# Inversiones: {'D': 1}
# Comparamos E con F. Como F < E entonces agregamos F al resultado. Esto nos dice que E y D superaron a F.
# Merge (despues): [('F', 5), ('E', 6), ('D', 8)]
# Inversiones: {'D': 2, 'E': 1}

# Merge (antes): [('C', 2), ('A', 3), ('B', 4)], [('F', 5), ('E', 6), ('D', 8)]
# Inversiones: {'A': 1, 'B': 1, 'D': 2, 'E': 1}
# Merge (despues): [('C', 2), ('A', 3), ('B', 4), ('F', 5), ('E', 6), ('D', 8)]
# Inversiones: {'A': 1, 'B': 1, 'D': 2, 'E': 1}