# Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo [a, b], y que en el punto a es positiva y en el 
# punto b es negativa (o viceversa), necesariamente debe haber (al menos) una raíz en dicho intervalo. 

# Implementar una función raiz que reciba una función (univariable) y los extremos mencionados a y b, y devuelva una raíz dentro de 
# dicho intervalo (si hay más de una, simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica del largo del 
# intervalo [a, b]. Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores: Se puede trabajar con 
# floats, y el algoritmo será equivalente, simplemente se plantea con ints para no generar confusiones con la complejidad. 

# Justificar la complejidad de la función implementada.

# Solucion: Metodo de biseccion.

def raiz(funcion, a, b):

    if funcion(a) == 0:
        return a
    
    if funcion(b) == 0:
        return b

    m = (a + b) // 2

    if funcion(m) == 0:
        return m

    if (funcion(a) * funcion(m) < 0):
        return raiz(funcion, a, m)
    
    return raiz(funcion, m, b)

# Justificacion: Teorema maestro

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2                                B
