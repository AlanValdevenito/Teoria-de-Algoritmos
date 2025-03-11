# Se tiene una lista de materias que deben ser cursadas en el mismo cuatrimestre, cada materia está representada con una lista de cursos/horarios posibles a 
# cursar (solo debe elegirse un horario por cada curso). Cada materia puede tener varios cursos. 

# Implementar un algoritmo de backtracking que devuelva un listado con todas las combinaciones posibles que permitan asistir a un curso de cada materia sin 
# que se solapen los horarios. 

# Considerar que existe una función son_compatibles(curso_1, curso_2) que dados dos cursos devuelve un valor booleano que indica si se pueden cursar al mismo tiempo.

def son_compatibles(curso_1, curso_2):
    inicio_1, fin_1 = curso_1["horario"]
    inicio_2, fin_2 = curso_2["horario"]
    return fin_1 <= inicio_2 or fin_2 <= inicio_1

def combinacion_compatible(combinacion_actual, curso):

    for c in combinacion_actual:

        if not son_compatibles(c, curso):
            return False
        
    return True

def _obtener_combinaciones(materias, combinacion_actual, combinaciones, actual):

    if (actual == len(materias)):
        combinaciones.append(combinacion_actual[:])
        return

    for curso in materias[actual]:

        if combinacion_compatible(combinacion_actual, curso):
            combinacion_actual.append(curso)
            _obtener_combinaciones(materias, combinacion_actual, combinaciones, actual + 1)
            combinacion_actual.pop()

def obtener_combinaciones(materias):
    combinaciones = []
    _obtener_combinaciones(materias, [], combinaciones, 0)
    return combinaciones

materias = [
    [
        {"id": "M1_C1", "horario": (9, 11)},
        {"id": "M1_C2", "horario": (11, 13)},
        {"id": "M1_C3", "horario": (14, 16)}
    ],
    [
        {"id": "M2_C1", "horario": (10, 12)},
        {"id": "M2_C2", "horario": (13, 15)}
    ],
    [
        {"id": "M3_C1", "horario": (8, 10)},
        {"id": "M3_C2", "horario": (15, 17)}
    ]
]

resultado = [[{'id': 'M1_C1', 'horario': (9, 11)}, {'id': 'M2_C2', 'horario': (13, 15)}, {'id': 'M3_C2', 'horario': (15, 17)}], 
             [{'id': 'M1_C2', 'horario': (11, 13)}, {'id': 'M2_C2', 'horario': (13, 15)}, {'id': 'M3_C1', 'horario': (8, 10)}], 
             [{'id': 'M1_C2', 'horario': (11, 13)}, {'id': 'M2_C2', 'horario': (13, 15)}, {'id': 'M3_C2', 'horario': (15, 17)}], 
             [{'id': 'M1_C3', 'horario': (14, 16)}, {'id': 'M2_C1', 'horario': (10, 12)}, {'id': 'M3_C1', 'horario': (8, 10)}]]

assert len(obtener_combinaciones(materias)) == len(resultado)