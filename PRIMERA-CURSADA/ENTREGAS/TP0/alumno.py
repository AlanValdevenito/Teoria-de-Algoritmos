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

# Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

alumnos = [1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23]

def _indice_mas_bajo(alumnos, desde, hasta):
    
    if (desde == hasta):
        return desde

    medio = (desde + hasta) // 2

    if (alumnos[medio-1] > alumnos[medio]) and (alumnos[medio+1] > alumnos[medio]):
        return medio

    if (alumnos[medio-1] > alumnos[medio]):
        return _indice_mas_bajo(alumnos, medio+1, hasta)
    
    return _indice_mas_bajo(alumnos, desde, medio)

def indice_mas_bajo(alumnos):
    n = len(alumnos) # Operacion O(1)
    return _indice_mas_bajo(alumnos, 0, n-1)

# Justificacion: Teorema maestro

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2                            B

resultado = indice_mas_bajo(alumnos)
print(f"El indice del alumno mas bajo es: {resultado}")

def validar_mas_bajo(alumnos, indice):
    return (alumnos[indice-1] > alumnos[indice]) and (alumnos[indice+1] > alumnos[indice])

# Justificacion: La complejidad es O(1) ya que acceder a un elemento es O(1) y solo estamos accediendo a 
# tres elementos. Ademas, las comparaciones hechas tambien son O(1).

indice = 5
resultado = validar_mas_bajo(alumnos, indice)
print(f"¿El indice {indice} se corresponde al del alumno mas bajo de la fila?: {resultado}")