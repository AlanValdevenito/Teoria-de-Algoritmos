# El club de Amigos de Siempre prepara una cena en sus instalaciones en la que desea invitar a la máxima 
# cantidad de sus n socios. Sin embargo por protocolo cada persona invitada debe cumplir un 
# requisito: Sólo puede ser invitada si conoce a al menos otras 4 personas invitadas. 

# Dada un lista de tuplas (duplas) de personas que se conocen:
# a. Nos solicitan seleccionar el mayor número posible de invitados. Proponer una estrategia greedy 
# óptima para resolver el problema.

from grafo import Grafo

# conocidos: lista de pares de invitados que se conocen, cada elemento es un (a,b).
def obtener_invitados(conocidos):
    grafo = Grafo(False)

    for (a,b) in conocidos:

        if a not in grafo.obtener_vertices():
            grafo.agregar_vertice(a)
        
        if b not in grafo.obtener_vertices():
            grafo.agregar_vertice(b)

        if not grafo.estan_unidos(a,b):
            grafo.agregar_arista(a,b)

    cambio = True
    while cambio:
        cambio = False
        eliminar = []

        for v in grafo.obtener_vertices():
            if len(grafo.adyacentes(v)) < 4:
                eliminar.append(v)
                cambio = True

        for v in eliminar:
            grafo.borrar_vertice(v)

    return grafo.obtener_vertices()

# Justificacion

# 1) Complejidad: Notemos que, en el peor de los casos, iteramos n x n veces los vertices del grafo. Luego, la complejidad
#                 resultante es O(n^2).

# 2) Algoritmo Greedy: Tenemos como regla de dominio que cada persona sólo puede ser invitada si conoce a al 
#                      menos otras 4 personas invitadas. Luego, iterativamente se analiza el estado actual
#                      del grafo y se eliminan los vertices que no cumplen la regla de dominio. Notemos que cada
#                      iteracion tiene e cuenta lo hecho en las iteraciones anteriores para llegar al resultado.

conocidos1 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), 
              ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), 
              ('E', 'F'), ('E', 'G'), ('B', 'E'), ('D', 'A'), ('A', 'E')]
resultado1 = obtener_invitados(conocidos1)
print(f"{conocidos1} →  ¿{resultado1} == ['A', 'B', 'C', 'D', 'E']?\n")