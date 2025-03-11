# Contamos con una lista de n coordenadas satelitales (latitud-longitud) que conforman un polígono convexo, ordenadas
# en sentido antihorario. 

# Queremos mostrar toda el área interior del polígono con el mayor tamaño posible en nuestra pantalla rectangular de la computadora. 

# El programa que muestra el mapa acepta como parámetros 2 coordenadas para construir el rectángulo a mostrar: los correspondientes a 
# los límites inferior izquierdo y superior derecho, tal que toda la imagen quede dentro de los límites. 

# Implementar un algoritmo que resuelva el problema con complejidad O(log n).

# Justificar adecuadamente la complejidad del algoritmo implementado.

# def buscar_coordenadas(puntos, inicio, fin, eje):

#     if (fin - inicio) == 1:
#         return puntos[inicio][eje], puntos[fin][eje]

#     medio = (inicio + fin) // 2

#     extremos_izq = buscar_coordenadas(puntos, inicio, medio, eje)
#     extremos_der = buscar_coordenadas(puntos, medio, fin, eje)

#     return min(extremos_izq[0], extremos_der[0]), max(extremos_izq[1], extremos_der[1])

# def buscar_rectangulo(poligono):
#     n = len(poligono)

#     x_min, x_max = buscar_coordenadas(poligono, 0, n-1, 0)
#     y_min, y_max = buscar_coordenadas(poligono, 0, n-1, 1)

#     limite_inferior_izq = (x_min, y_min)
#     limite_superior_der = (x_max, y_max)

#     return limite_inferior_izq, limite_superior_der

# def encontrar_extremo(poligono, inicio, fin, eje):

#     # Caso base: quedan solo 3 puntos → devolvemos el índice del máximo
#     if fin - inicio <= 2:
#         return max(range(inicio, fin + 1), key=lambda i: poligono[i][eje])

#     medio = (inicio + fin) // 2

#     # Definir los vectores A, B y C
#     A = (poligono[inicio], poligono[inicio + 1])   # Desde inicio hasta su siguiente
#     B = (poligono[fin - 1], poligono[fin])         # Desde penúltimo hasta fin
#     C = (poligono[medio], poligono[medio + 1])     # Desde medio hasta su siguiente

#     # Determinar en qué mitad está el máximo
#     if A[0][eje] <= C[0][eje] and C[0][eje] >= B[0][eje]:
#         return encontrar_extremo(poligono, medio, fin, eje)  # Buscar en la derecha
#     else:
#         return encontrar_extremo(poligono, inicio, medio, eje)  # Buscar en la izquierda

# def buscar_rectangulo(poligono):
#     xmin = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 0)][0]
#     xmax = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 0)][0]
#     ymin = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 1)][1]
#     ymax = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 1)][1]

#     return (xmin, ymin), (xmax, ymax)

def encontrar_extremo(poligono, inicio, fin, eje):
    # Caso base: quedan solo 3 puntos → devolvemos el índice del máximo
    if fin - inicio <= 2:
        return max(range(inicio, fin + 1), key=lambda i: poligono[i][eje])

    medio = (inicio + fin) // 2

    # Definir los vectores A, B y C
    A = poligono[inicio]
    B = poligono[fin]
    C = poligono[medio]

    print(f"A: {A}, B: {B}, C{C}")

    # Detectamos la tendencia de los vectores → ¿suben no bajan?
    tendencia_A = poligono[inicio + 1][eje] - A[eje]  # Diferencia entre A y su siguiente
    tendencia_C = poligono[medio + 1][eje] - C[eje]   # Diferencia entre C y su siguiente

    print(f"Tendencia de A: {tendencia_A} - Tendencia de C: {tendencia_C}")

    # Caso 1: A sube y C baja → Buscar en [A+1, C]**
    if tendencia_A >= 0 and tendencia_C < 0:
        print("Caso 1")
        return encontrar_extremo(poligono, inicio + 1, medio, eje)

    # Caso 2: A sube y C sube, con C arriba de A → Buscar en [C+1, B]**
    if tendencia_A >= 0 and tendencia_C > 0 and C[eje] >= A[eje]:
        print("Caso 2")
        return encontrar_extremo(poligono, medio + 1, fin, eje)

    # Caso 3: A sube y C sube, con C debajo de A → Buscar en [A+1, C]**
    if tendencia_A >= 0 and tendencia_C > 0 and C[eje] < A[eje]:
        print("Caso 3")
        return encontrar_extremo(poligono, inicio + 1, medio, eje)

    # Los mismos casos, pero con A bajando en vez de subiendo
    if tendencia_A < 0 and tendencia_C > 0:
        print("Caso 4")
        return encontrar_extremo(poligono, inicio + 1, medio, eje)

    if tendencia_A < 0 and tendencia_C < 0 and C[eje] >= A[eje]:
        print("Caso 5")
        return encontrar_extremo(poligono, medio + 1, fin, eje)

    if tendencia_A < 0 and tendencia_C < 0 and C[eje] < A[eje]:
        print("Caso 6")
        return encontrar_extremo(poligono, inicio + 1, medio, eje)

    return medio  # Caso por defecto (no debería ocurrir)

def buscar_rectangulo(poligono):
    xmin = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 0)][0]
    print("")
    xmax = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 0)][0]
    print("")
    ymin = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 1)][1]
    print("")
    ymax = poligono[encontrar_extremo(poligono, 0, len(poligono) - 1, 1)][1]

    return (xmin, ymin), (xmax, ymax)

poligono = [
    (1, 3),  # A
    (2, 1),  # B
    (4, 1),  # C
    (5, 3),  # D
    (3, 5),  # E
]

rectangulo = buscar_rectangulo(poligono)
print(rectangulo)
assert rectangulo == ((1, 1), (5, 5))