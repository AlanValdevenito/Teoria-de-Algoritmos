# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número n, en 
# tiempo O(log n). 

# Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe devolver 5. 

# Justificar el orden del algoritmo.

# Aclaración: No se requiere el uso de ninguna librería de matemática que calcule la raíz cuadrada, ni de forma exacta ni aproximada.

def _parte_entera_raiz(n, inicio, fin):

    medio = (inicio + fin) // 2

    if (n == medio**2):
        return medio
    
    if (inicio >= fin):
        return inicio - 1

    if (n > medio**2):
        return _parte_entera_raiz(n, medio+1, fin)
    
    return _parte_entera_raiz(n, inicio, medio) 

def parte_entera_raiz(n):
    return _parte_entera_raiz(n, 0, n)

# Complejidad

# A: 1 (Si bien hay escritos dos llamados recursivos, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0 (Costo de partir y juntar)

# T(n) = A T(n/B) + O(n^C) = 2 T(n/2) + O(1)

# log (1) = 0 ￫ T(n) = O(n^C log (n)) = O(n^C log (n)) = O(n^0 log (n)) = O(log(n))
#    2                          B 

assert parte_entera_raiz(0) == 0
assert parte_entera_raiz(1) == 1
assert parte_entera_raiz(10) == 3
assert parte_entera_raiz(25) == 5