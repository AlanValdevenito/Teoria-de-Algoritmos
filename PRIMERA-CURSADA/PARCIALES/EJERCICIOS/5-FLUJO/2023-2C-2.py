# En un hospital, se tiene un conjunto de médicos y un conjunto de pacientes. Cada médico tiene un horario con franjas
# horarias disponibles para citas médicas. Nuestro objetivo es emparejar médicos con pacientes de manera que se maximice
# el número total de citas médicas programadas. 

# Implementar un algoritmo que resuelva dicho problema de manera eficiente. 

# Indicar y justificar la complejidad del algoritmo implementado.

# Modelado:
# - Modelamos cada medico como una fuente
# - Modelamos cada paciente como un sumidero
# - Definimos una super fuente conectada a cada medico con flujo infinito
# - Definomos un super sumidero conectado a cada paciente con flujo 1
# - Conectamos cada medico con cada paciente segùn los horarios coincidentes. El flujo de cada arista sera 1

from grafo import Grafo
from ford_fulkerson import ford_fulkerson

def crear_grafo(medicos, pacientes, citas):
    grafo = Grafo(True)

    for m in medicos:
        grafo.agregar_arista("F", m, 1000)

    for p in pacientes:
        grafo.agregar_arista(p, "S", 1)

    for medico, pacientes in citas.items():
        for p in pacientes:
            grafo.agregar_arista(medico, p, 1)

    return grafo

def hospital(medicos, pacientes, citas):
    grafo = crear_grafo(medicos, pacientes, citas)
    flujo = ford_fulkerson(grafo, "F", "S")

    cantidad = 0
    citas = []

    for arista, flujo in flujo.items():

        if (arista[0][0] == "M" or arista[0][0] == "M") and (flujo > 0):
            citas.append(arista)
            cantidad += 1

    return cantidad, citas

# Complejidad

# La construccion del grafo tiene una complejidad de O(M + P + C) donde M es la cantidad de medicos, P la cantidad de pacientes y C la cantidad de citas.

# El algoritmo de Ford Fulkerson tiene una complejidad de O(V x E²) donde V es la cantidad de vertices y E la cantidad de aristas.

# Luego, el algoritmo tiene una complejidad de O(V x E²).

assert hospital(["M1", "M2", "M3"], ["P1", "P2", "P3", "P4"], {"M1": ["P1", "P2"], "M2": ["P2", "P3"], "M3": ["P2", "P4"]}) == (4, [('M1', 'P1'), ('M1', 'P2'), ('M2', 'P3'), ('M3', 'P4')])