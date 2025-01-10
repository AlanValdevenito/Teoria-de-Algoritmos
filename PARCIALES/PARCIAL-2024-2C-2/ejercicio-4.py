# Contamos con una lista de n coordenadas satelitales (latitud-longitud) que conforman un polígono convexo, ordenadas
# en sentido antihorario. 

# Queremos mostrar toda el área interior del polígono con el mayor tamaño posible en nuestra pantalla rectangular de la computadora. 

# El programa que muestra el mapa acepta como parámetros 2 coordenadas para construir el rectángulo a mostrar: los correspondientes a 
# los límites inferior izquierdo y superior derecho, tal que toda la imagen quede dentro de los límites. 

# Implementar un algoritmo que resuelva el problema con complejidad O(log n).

# Justificar adecuadamente la complejidad del algoritmo implementado.

def buscar_rectangulo(poligono):
    pass

poligono = [
    (1, 1),  # A
    (2, -1),  # B
    (4, -1),  # C
    (5, 1),  # D
    (3, 3),  # E
]

rectangulo = buscar_rectangulo(poligono)

assert rectangulo == ((1, -1), (5, 3))