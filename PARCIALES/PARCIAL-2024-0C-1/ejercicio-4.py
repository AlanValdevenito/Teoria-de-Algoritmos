# Implementar un algoritmo que resuelva el problema de 3-SAT: determinar si, dado un grupo de cláusulas de 3 términos
# (pudiendo ser complementos de variables), existe alguna asignación de valores de las variables tal que la disyunción de
# todas las cláusulas (que son todas conjunciones) evalúan a true.

def asignacion_valida(clausulas, asignacion):

    for clausula in clausulas:
        clausula_valida = False 

        # Para cada clausula buscamos que al menos una variable tenga valor 'True'
        for variable in clausula:

            if variable.startswith('-'):
                valor = asignacion.get(variable[1:], None)

                if not valor:
                    clausula_valida = True
                    break

            else:
                valor = asignacion.get(variable, None)

                if valor:
                    clausula_valida = True
                    break

        if not clausula_valida:
            # print(f"Asignacion invalida: {asignacion}")
            return False

    # print(f"Asignacion valida: {asignacion}\n")
    return True

def backtracking(variables, clausulas, asignacion, actual):
    
    # print(f"Variables: {variables} - Valores: {valores}\n")

    if len(variables) == actual:
        return asignacion_valida(clausulas, asignacion)
    
    v = variables[actual]
    
    asignacion[v] = True
    if backtracking(variables, clausulas, asignacion, actual + 1):
        return True
    
    asignacion[v] = False
    if backtracking(variables, clausulas, asignacion, actual + 1):
        return True
    
    del asignacion[v]
    return False

def sat(variables, clausulas):
    return backtracking(variables, clausulas, {}, 0)

variables = ["x1", "x2", "x3", "x4", "x5"]

clausulas = [
    ["x1", "x2", "-x3"],
    ["-x1", "x3", "x4"],
    ["x2", "-x4", "-x5"],
]

assert sat(variables, clausulas) == True

variables = ["x1", "x2", "x3", "x4", "x5"]

clausulas = [
    ["x1", "x2", "-x3"],
    ["-x1", "-x3", "-x4"],
    ["x2", "-x4", "-x5"],
]

assert sat(variables, clausulas) == True

variables = ["x1", "x2", "x3"]

clausulas = [
    ["x1", "x2", "-x3"],
    ["-x1", "-x2", "-x3"],
    ["x1", "-x2", "x3"],
    ["-x1", "x2", "-x3"],
]

assert sat(variables, clausulas) == True

variables = ["x1", "x2", "x3"]

clausulas = [
    ["x1", "x2", "x3"],
    ["x1", "x2", "-x3"],
    ["x1", "-x2", "x3"],
    ["-x1", "x2", "x3"],
    ["-x1", "-x2", "-x3"],
]

assert sat(variables, clausulas) == True

variables = ["x1", "x2", "x3"]

clausulas = [
    ["x1", "x2", "x3"],
    ["x1", "x2", "-x3"],
    ["x1", "-x2", "x3"],
    ["-x1", "x2", "x3"],
    ["-x1", "-x2", "-x3"],
    ["-x1", "-x2", "x3"]
]

assert sat(variables, clausulas) == True