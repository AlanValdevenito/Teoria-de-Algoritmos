# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la 
# raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3, y para n = 25 debe 
# devolver 5. 

# Justificar el orden del algoritmo.

def _parte_entera_raiz(n, desde, hasta):
    mitad = (desde + hasta) // 2
    mitad_al_cuadrado = mitad**2

    if (mitad_al_cuadrado == n):
        return mitad

    if (desde == hasta):
        return desde-1

    if (mitad_al_cuadrado > n):
        return _parte_entera_raiz(n, desde, mitad)

    return _parte_entera_raiz(n, mitad+1, hasta)

def parte_entera_raiz(n):
    return _parte_entera_raiz(n, 0, n)

# Justificacion: Teorema maestro

# A: 1 (Si bien hay escritos dos llamados, en cada ejecucion se llama a uno u otro)
# B: 2 (Se divide al problema en dos)
# C: 0

# T(n) = A.T(n/B) + O(n^C) = T(n/2) + O(n^0) = T(n/2) + O(1)

# log (A) = log (1) = 0 = C → T(n) = O(n^C . log (n)) = O(n^C . log(n)) = O(n^0 . log(n)) = O(log(n))
#    B         2                                B

resultado = parte_entera_raiz(10)
print(f"La parte entera de la raiz de 10 es: {resultado}")