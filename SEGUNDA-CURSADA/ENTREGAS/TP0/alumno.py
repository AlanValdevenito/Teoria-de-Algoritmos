# La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. 
# En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado 
# un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

# Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

# Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos que represente dicha fila, devuelva 
# el índice del alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el 
# alumno más bajo es aquel con altura 0.98.

# Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos y un índice, valide (devuelva True 
# o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse 
# en tiempo constante).

# Los alumnos son de la forma:

# alumno {
#     nombre (string)
#     altura (float)
# }

# Se puede acceder a la altura de un alumno haciendo variable_tipo_alumno.altura.

alumnos = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23]

def validar_mas_bajo(alumnos, indice):
    return (alumnos[indice-1] > alumnos[indice]) and (alumnos[indice] < alumnos[indice+1])

# Complejidad

# La complejidad es O(1) ya que acceder a un elemento es O(1) y solo estamos accediendo a tres elementos. Ademas, las comparaciones 
# hechas tambien son O(1).

assert validar_mas_bajo(alumnos, 5) == True

def _indice_mas_bajo(alumnos, inicio, fin):

    if (inicio >= fin):
        return inicio
    
    medio = (inicio + fin) // 2

    if validar_mas_bajo(alumnos, medio):
        return medio
    
    # Si las alturas son decrecientes, entonces el mas bajo debe estar en el lado derecho
    if (alumnos[medio-1] > alumnos[medio]):
        return _indice_mas_bajo(alumnos, medio+1, fin)
    
    # Si las alturas son crecientes, entonces el mas bajo debe estar en el lado izquierdo
    return _indice_mas_bajo(alumnos, inicio, medio-1)

def indice_mas_bajo(alumnos):
    return _indice_mas_bajo(alumnos, 0, len(alumnos)-1)

# Complejidad

# A: 1 (Si bien hay escritos dos llamados recursivos, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0 (Costo de partir y juntar)

# T(n) = A T(n/B) + O(n^C) = 2 T(n/2) + O(1)

# log (1) = 0 ￫ T(n) = O(n^C log (n)) = O(n^C log (n)) = O(n^0 log (n)) = O(log(n))
#    2                          B 

assert indice_mas_bajo(alumnos) == 5