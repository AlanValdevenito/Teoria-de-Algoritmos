# Se tiene una colección de n libros con diferentes espesores, que pueden estar entre 1 y n (valores no necesariamente enteros). Tu objetivo es guardar esos libros 
# en la menor cantidad de cajas. Todas las cajas disponibles son de la misma capacidad L (se asegura que L >= n). Obviamente, no podés partir un libro para que vaya 
# en múltiples cajas, pero sí podés poner múltiples libros en una misma caja, siempre y cuando los espesores no superen esa capacidad L. 

# Implementar un algoritmo Greedy que obtenga las cajas, tal que se minimicen la cantidad de cajas a utilizar. 

# Indicar y justificar la complejidad del algoritmo implementado. 

# Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo propuesto encuentra siempre la solución óptima?. Justificar.

# ¿Qué cambios aplicarías si supieras que los espesores sólo fueran números enteros?. Describir cómo afecta a la complejidad, y a su optimalidad.

def cajas(capacidad, libros):
    libros_ordenados = sorted(libros)
    cajas = []

    for libro in libros_ordenados:
        colocado = False

        for caja in cajas:
            
            if (sum(caja) + libro <= capacidad):
                caja.append(libro)
                colocado = True
                break

        if not colocado:
            cajas.append([libro])

    return cajas

# Justificacion

# 1) Complejidad: Notemos que tenemos un ordenamiento con complejidad O(n log(n)) e iteramos la lista de elementos lo cual
#                 en el peor caso tiene una complejidad de O(n²). Ademàs, todas las operaciones restantes son O(1). Luego, la complejidad
#                 resultante es O(n²).

# 2) Algoritmo Greedy: Tenemos como regla sencilla quedarnos con el elemento cuyo espesor sea menor y que no supere la capacidad 
#                      de la caja actual. Luego, se aplica iterativamente esta regla con el objetivo de guardar aquellos libros
#                      que minimizan la cantidad de cajas.

#                      La solucion no es siempre optima. Veamos un contraejemplo.

#                      Libros: [2,2,2,2,3,3] con capacidad 7 → Solución: [[2,2,2], [2,3], [3]]

#                      La solución óptima seria [[3,2,2], [3,2,2]].

# 3) Si los espesores fueran solo numeros enteros no cambiaria la complejidad y la optimalidad. Esto podemos verlo en el ejercicio 11 de Greedy.

assert cajas(10, [2.4, 1, 1.6, 3, 4, 3.1]) == [[1, 1.6, 2.4, 3], [3.1, 4]]