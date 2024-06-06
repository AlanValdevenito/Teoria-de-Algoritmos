# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. 
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una era de inflación y los precios 
# aumentan todo el tiempo. El precio del producto i el día j es R[i]^{j + 1} (j comenzando en 0). 

# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
# Indicar y justificar la complejidad del algoritmo implementado. 

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar. 
# ¿Por qué se trata de un algoritmo Greedy?. Justificar.

def calcular_inflacion(producto, dia):
    return (producto**(dia + 1))

def precios_inflacion(R):
    cantidad_productos = len(R)
    productos_ordenados = sorted(R, reverse=True)
    precio_minimo = []

    for dia in range(cantidad_productos):
        producto = productos_ordenados.pop(0)
        producto_con_inflacion = calcular_inflacion(producto, dia)
        precio_minimo.append(producto_con_inflacion)

    return sum(precio_minimo)

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de productos lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla de dominio que cada día podemos y debemos comprar uno (y sólo uno) de los productos y
#                      como regla sencilla ordenar de mayor a menor el precio de nuestros productos y siempre comprar primero el
#                      producto de mayor valor ya que el precio mas grande es el que va a crecer mas rapido.
#                      Luego, se aplica iterativamente esta regla para comprar todos los productos.
#                      La solucion es optima ya que cada día podemos y debemos comprar uno (y sólo uno) de los productos.

assert precios_inflacion([8,4,9,5,10,17,2,23,3]) == 79723