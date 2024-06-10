# En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto. Cada día podemos y debemos 
# comprar uno (y sólo uno) de los productos, pero Wakanda está atravesando una era de deflación y los precios disminuyen todo el tiempo. 
# El precio del producto i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios del primer 
# día. Si bien para reducir costos se debería esperar a que los productos sigan bajando, los tiempos de entrega no nos permiten esperar, y 
# cada día debemos comprar uno de los productos.

# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar todos los productos. 
# Indicar y justificar la complejidad del algoritmo implementado. 

# ¿El algoritmo implementado encuentra siempre la solución óptima?. Justificar.
# ¿Por qué se trata de un algoritmo Greedy?. Justificar

def calcular_deflacion(producto, dia):
    return (producto/(2**dia))

def precios_deflacion(R):
    cantidad_productos = len(R)
    productos_ordenados = sorted(R)
    precio_minimo = []

    for dia in range(cantidad_productos):
        producto = productos_ordenados.pop(0)
        producto_con_deflacion = calcular_deflacion(producto, dia)
        precio_minimo.append(producto_con_deflacion)

    return sum(precio_minimo)

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de productos lo cual
#                 tiene una complejidad de O(n). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n log(n)).

# 2) Algoritmo Greedy: Tenemos como regla de dominio que cada día podemos y debemos comprar uno (y sólo uno) de los productos y
#                      como regla sencilla ordenar de menor a mayor el precio de nuestros productos y siempre comprar primero el
#                      producto de menor valor ya que debemos esperar a que los productos de mayor precio bajen lo mas que podamos.
#                      Luego, se aplica iterativamente esta regla para comprar todos los productos.
#                      La solucion es optima ya que cada día podemos y debemos comprar uno (y sólo uno) de los productos.

assert precios_deflacion([10.05, 5, 20.4, 10]) == 15.0625
assert precios_deflacion([10, 5, 20, 10]) == 15.0
assert precios_deflacion([5, 10]) == 10.0
assert precios_deflacion([]) == 0
assert precios_deflacion([5, 20, 10]) == 15.0
assert precios_deflacion([10]) == 10
