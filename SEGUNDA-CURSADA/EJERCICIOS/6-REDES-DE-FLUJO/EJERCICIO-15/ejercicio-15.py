# En un hospital, se tiene un conjunto de médicos y un conjunto de pacientes. Cada médico tiene un horario con franjas horarias disponibles para citas médicas y su 
# área de especialidad, y cada paciente tiene sus franjas horaria disponibles para ir al médico, junto con la información de qué tipo de especialidad requiere. 

# Nuestro objetivo es emparejar médicos con pacientes de manera que se maximice el número total de citas médicas programadas. 

# Se puede asumir que cada visita médica dura una cuota de tiempo fija, y que los pacientes pueden ser a priori atendidos por cualquier médico que coincida con el 
# área de especialidad que requieren. 

# Implementar un algoritmo que resuelva dicho problema de manera eficiente. 

# Indicar y justificar la complejidad del algoritmo implementado.

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from grafo import Grafo
from ford_fulkerson import ford_fulkerson

MEDICO = 0
PACIENTE = 0
ESPECIALIDAD = 1
HORARIO = 2

def crear_grafo(medicos, pacientes):
    grafo = Grafo(True)

    for m in medicos:
        grafo.agregar_arista("S", f"{m[MEDICO]}-{m[ESPECIALIDAD]}-{m[HORARIO]}", 1)

    for p in pacientes:
        grafo.agregar_arista(f"{p[PACIENTE]}-{p[ESPECIALIDAD]}-{p[HORARIO]}", "T", 1)

    for medico in medicos:
        for paciente in pacientes:

            if (medico[ESPECIALIDAD] == paciente[ESPECIALIDAD]) and (medico[HORARIO] == paciente[HORARIO]):
                m = f"{medico[MEDICO]}-{medico[ESPECIALIDAD]}-{medico[HORARIO]}"
                p = f"{paciente[PACIENTE]}-{paciente[ESPECIALIDAD]}-{paciente[HORARIO]}"
                grafo.agregar_arista(m, p, 1)

    return grafo

def hospital(medicos, pacientes):
    red = crear_grafo(medicos, pacientes)
    flujo = ford_fulkerson(red, "S", "T")

    cantidad = 0
    citas = []

    for arista, flujo in flujo.items():

        if (arista[0][0] == "M") and (flujo > 0):
            citas.append(arista)
            cantidad += 1

    return cantidad, citas

medicos = [("M1", "Cardiologia", (9,10)), ("M1", "Cardiologia", (10,11)), ("M2", "Dermatologia", (9,10))]
pacientes = [("P1", "Cardiologia", (9,10)), ("P2", "Dermatologia", (9,10)), ("P3", "Cardiologia", (10,11))]

assert hospital(medicos, pacientes) == (3, [('M1-Cardiologia-(9, 10)', 'P1-Cardiologia-(9, 10)'), 
                                            ('M1-Cardiologia-(10, 11)', 'P3-Cardiologia-(10, 11)'), 
                                            ('M2-Dermatologia-(9, 10)', 'P2-Dermatologia-(9, 10)')])
