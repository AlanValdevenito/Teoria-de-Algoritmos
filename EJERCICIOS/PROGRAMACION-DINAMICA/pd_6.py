# Dado el teclado numérico de un celular, y un número inicial k, encontrar la cantidad de posibles números de longitud N empezando por 
# botón del número inicial k.

# Restricción: Solamente se puede presionar un botón si está arriba, abajo, a izquierda, o derecha del botón actual.

# Implementar el algoritmo por programación dinámica. Indicar y justificar la complejidad del algoritmo implementado. 

# Ejemplos:
# Para N=1 empezando por cualquier dígito, solamente hay un número válido (el correspondiente dígito)
# Para N=2, depende de cuál dígito se comienza:
# Empezando por k=0, son válidos 00, 08 (cantidad: 2)
# Empezando por k=1, son válidos 11, 12, 14 (cantidad: 3)
# Empezando por k=2, son válidos 22, 21, 23, 25 (cantidad: 4)
# Empezando por k=3, son válidos 33, 32, 36 (cantidad: 3)
# Empezando por k=4, son válidos 44, 41, 45, 47 (cantidad: 4)
# Empezando por k=5, son válidos 55, 52, 54, 56, 58 (cantidad: 5)
# Empezando por k=6, son válidos 66, 63, 65, 69 (cantidad: 4)
# Empezando por k=7, son válidos 77, 74, 78 (cantidad: 3)
# Empezando por k=8, son válidos 88, 80, 85, 87, 89 (cantidad: 5)
# Empezando por k=9, son válidos 99, 96, 98 (cantidad: 3)

# Nota: El ejercicio puede resolverse sin el uso de Grafos, pero en caso de querer utilizarlo, está disponible como se describe.

# Notemos que la cantidad de posibles numeros esta dado por el mismo numero inicial (k) y su adyacentes.
# Modelamos la restriccion de posiciones del telefono mediante un grafo. Luego, para calcular la cantidad de posibles numeros de 
# longitud N se puede calcular considerando el vertice correspondiente al numero inicial k y sus adyacentes.

# Ecuacion de recurrencia: C[tecla][n] = c[tecla][n-1] + sum(c[cada tecla adyacente][n-1])

from grafo import Grafo

TECLAS = 10

def crear_teclado():
    grafo = Grafo(False, [0,1,2,3,4,5,6,7,8,9])
    grafo.agregar_arista(1,2)
    grafo.agregar_arista(1,4)
    grafo.agregar_arista(2,3)
    grafo.agregar_arista(2,5)
    grafo.agregar_arista(3,6)
    grafo.agregar_arista(4,5)
    grafo.agregar_arista(4,7)
    grafo.agregar_arista(5,6)
    grafo.agregar_arista(5,8)
    grafo.agregar_arista(6,9)
    grafo.agregar_arista(7,8)
    grafo.agregar_arista(8,9)
    grafo.agregar_arista(8,0)
    return grafo

def numeros_posibles_dinamico(grafo, n):
    mem = [[0 for i in range(n+1)] for j in range(TECLAS)]
    
    for tecla in range(TECLAS):
        mem[tecla][1] = 1

    for n in range(2, n+1):
        for tecla in range(TECLAS):
            contador = 0
            for vecino in grafo.adyacentes(tecla):
                contador += mem[vecino][n-1]
            
            mem[tecla][n] = mem[tecla][n-1] + contador
    
    return mem

def numeros_posibles(k, n):
    grafo = crear_teclado()
    mem = numeros_posibles_dinamico(grafo, n)
    return mem[k][n]

# Complejidad: Tenemos O(n) por calcular la matriz de memorizacion siendo n la longitud (pasos). Luego, la complejidad total es O(n).

assert numeros_posibles(0,1) == 1
assert numeros_posibles(0, 2) == 2
assert numeros_posibles(1, 2) == 3
assert numeros_posibles(2, 2) == 4
assert numeros_posibles(3, 2) == 3
assert numeros_posibles(4, 2) == 4
assert numeros_posibles(5, 2) == 5
assert numeros_posibles(6, 2) == 4
assert numeros_posibles(7, 2) == 3
assert numeros_posibles(8, 2) == 5
assert numeros_posibles(9, 2) == 3