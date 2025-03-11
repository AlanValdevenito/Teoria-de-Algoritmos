# Algoritmo sencillo: Calcular la proyección lineal de todos los puntos y nos quedamos con el máximo. Básicamente por fuerza 
# bruta calcular distancia, obteniendo la proyección y luego vemos el máximo. Esto tiene una complejidad O(n).

# Pasos:
# 1) Proyectar cada punto sobre los ejes X e Y.
# 2) Calcular la distancia de cada punto con respecto al origen en ese eje.
# 3) Determinar los valores extremos (mínimo y máximo) de estas proyecciones.

# Para cada punto podemos definir su proyección en el eje X simplemente como su coordenada y su proyección en el eje Y como 
# su coordenada.

# La distancia de cada proyección al origen (su módulo) se calcula como |x| o |y|.

def buscar_rectangulo(poligono):

    # Proyecciones y distancia sobre cada eje
    proyecciones_x = [abs(p[0]) for p in poligono]  # Proyectamos sobre X y calculamos distancia
    proyecciones_y = [abs(p[1]) for p in poligono]  # Proyectamos sobre Y y calculamos distancia

    # Determinar los extremos en X e Y
    xmin, xmax = min(proyecciones_x), max(proyecciones_x)
    ymin, ymax = min(proyecciones_y), max(proyecciones_y)

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