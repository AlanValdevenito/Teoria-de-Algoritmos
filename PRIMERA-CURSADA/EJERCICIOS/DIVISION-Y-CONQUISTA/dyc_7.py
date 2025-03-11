# Implementar un algoritmo que dados n puntos en un plano, busque la pareja que se encuentre más cercana, por división y conquista, con 
# un orden de complejidad mejor que O(n^2). 

# Justificar el orden del algoritmo mediante el teorema maestro.

import math

COORDENADA_X = 0
COORDENADA_Y = 1
VENTANA = 15

def dist(p0, p1):
    return math.sqrt((p0[COORDENADA_X]-p1[COORDENADA_X])**2 + (p0[COORDENADA_Y]-p1[COORDENADA_Y])**2)

def puntos_mas_cercanos_Sy(S,d):
    min_dist = d
    min_par = (None, None)

    for i in range(len(S)):
        for j in range (min(VENTANA, len(S))):

            if (i == j):
                continue

            distance = dist(S[i], S[j])

            if distance < min_dist:
                min_dist = distance
                min_par = (S[i], S[j])
    
    return min_par

def mas_cercanos(p):
    min_dist = float('inf')
    min_par = (None, None)

    for i in range(len(p)):
        for j in range (len(p)):

            if (i == j):
                continue

            if dist(p[i], p[j]) < min_dist:
                min_dist = dist(p[i], p[j])
                min_par = (p[i], p[j])
    
    return min_par

def _puntos_mas_cercanos(px, py):
    
    if len(px) <= 3:
        return mas_cercanos(px)
    
    medio = len(px) // 2
    punto_medio = px[medio][COORDENADA_X]
    
    qx = px[:medio]
    rx = px[medio:]

    qy = [p for p in py if p[COORDENADA_X] <= punto_medio]
    ry = [p for p in py if p[COORDENADA_X] > punto_medio]

    q0, q1 = _puntos_mas_cercanos(qx, qy)
    r0, r1 = _puntos_mas_cercanos(rx, ry)

    d = min(dist(q0, q1), dist(r0, r1))

    Sy = [p for p in py if abs(p[COORDENADA_X] - punto_medio) <= d]

    s0, s1 = puntos_mas_cercanos_Sy(Sy, d)

    if (s0 is not None) and (s1 is not None) and (dist(s0, s1) < d):
        return s0, s1
    
    elif dist(q0, q1) < dist(r0, r1):
        return q0, q1

    else:
        return r0, r1

def puntos_mas_cercanos(puntos):
    px = sorted(puntos, key=lambda p: p[COORDENADA_X])
    py = sorted(puntos, key=lambda p: p[COORDENADA_Y])

    p0, p1 = _puntos_mas_cercanos(px, py)
    return p0, p1

# Complejidad: Debido al ordenamiento de los puntos y al uso de nociones de MergeSort la complejidad resulta ser O(n log(n)).

assert puntos_mas_cercanos([(5,8),(1,9),(9,6),(16,3),(11,17),(4,19),(2,2),(7,18),(10,10),(1,13)]) == ((7, 18), (4, 19))