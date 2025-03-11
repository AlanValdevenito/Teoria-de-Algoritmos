# Dada una expresión representada por una cadena con aperturas y cierres de paréntesis, es sencillo implementar un
# algoritmo que, utilizando una pila, determine si la expresión se encuentra balanceada, o no (esto es un algoritmo sencillo
# de la materia anterior). Por ejemplo, la secuencia ()(), se encuentra balanceada, así como (()) también lo está, pero
# ((), no lo está, ni )()(. 

# Implementar un algoritmo greedy que reciba una cadena y determine el largo del prefijo balanceado más largo (es decir, el 
# largo de la subsecuencia balanceada más larga que sí o sí comienza en el inicio de la cadena). 

# Indicar y justificar la complejidad del algoritmo. 

# Indicar por qué se trata, en efecto, de un algoritmo greedy.

# El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.

# Ejemplo: para ()())(())()((), la respuesta es 4.

def largo_prefijo_balanceado(cadena):
    contador = 0
    largo = 0

    for c in cadena:

        if (c == '('):
            contador += 1
            largo += 1

        elif (c == ')'):

            if (contador == 0):
                return largo
            
            contador -= 1
            largo += 1
        
    return largo

# Complejidad

# Iteramos cada caracter de la cadena y en cada iteracion realizamos operaciones O(1).

# Luego, la complejidad resulta ser O(C) con C la cantidad de caracteres de la cadena.

# Algoritmo Greedy

# El algoritmo tiene como regla sencilla en cada iteracion incrementar o decrementar un contador dependiendo del caracter actual.
# Si el caracter actual es una apertura, se incrementa el contador.
# Si el caracter actual es un cierre, se decrementa el contador. Si el contador era 0 antes de decrementarlo, entonces tenemos un caracter de cierre sin apertura.

# Luego, se aplica esta regla de forma iterativa.

# ¿El algoritmo es optimo?. Si, el algoritmo es optimo debido a la regla del enunciado que nos indica que el largo de la 
# subsecuencia balanceada más larga debe sí o sí comenzar en el inicio de la cadena.

assert largo_prefijo_balanceado("()())(())()(()") == 4