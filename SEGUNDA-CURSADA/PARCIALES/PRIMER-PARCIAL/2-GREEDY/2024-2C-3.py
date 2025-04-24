# Dada una expresión representada por una cadena con aperturas y cierres de paréntesis, es sencillo implementar un
# algoritmo que, utilizando una pila, determine si la expresión se encuentra balanceada, o no (esto es un algoritmo sencillo
# de la materia anterior). Por ejemplo, la secuencia ()(), se encuentra balanceada, así como (()) también lo está, pero
# ((), no lo está, ni )()(. 

# Implementar un algoritmo greedy que reciba una cadena y determine el largo del prefijo balanceado más largo (es decir, el largo de la subsecuencia balanceada 
# más larga que sí o sí comienza en el inicio de la cadena). 

# Indicar y justificar la complejidad del algoritmo. Indicar por qué se trata, en efecto, de un algoritmo greedy.

# El algoritmo, ¿es óptimo? si lo es, justificar brevemente, sino dar un contraejemplo.

# Ejemplo: para ()())(())()((), la respuesta es 4.

APERTURA = '('
CIERRE = ')'

def largo_prefijo_balanceado(expresion):
    largo = 0
    balanceado = 0

    for c in expresion:

        if (c == APERTURA): 
            balanceado += 1

        elif (c == CIERRE): 
            
            if (balanceado == 0): 
                return largo

            balanceado -= 1

        largo += 1

    return largo

# Complejidad

# El algoritmo recorre cada caracter de la expresion con lo cual la complejidad resulta ser O(C) con C la cantidad de caracteres de la expresion.

# Algoritmo Greedy

# El algoritmo Greedy tiene como regla sencilla recorrer cada caracter de la expresion manteniendo un contador que indique si la expresion se encuentra 
# balanceada y en cada iteracion aumentar en 1 el largo del prefijo balanceado mientras la expresion se encuentre balanceada:
# - Si el caracter es APERTURA se incrementa el balance.
# - Si el caracter es CIERRE se decrementa el balance (intenta cerrarlo) y si balance es igual a cero (no hay apertura) se detiene porque se rompe el balance.

# Es decir, nuestro algoritmo Greedy avanza aumentando el largo del prefijo siempre que se pueda mantener la validez del balance y cortar en el momento
# que esto no sea posible.

# Luego, se aplica esta regla de forma iterativa.

# ¿El algoritmo es optimo?. Si, el algoritmo es optimo debido a la regla del enunciado que nos indica que el largo de la subsecuencia balanceada más larga 
# debe sí o sí comenzar en el inicio de la cadena.

# Nuestro algoritmo encuentra el mayor valor de k tal que expresion[0:k] es balanceado.

# Si nuestro algoritmo devuelve k es porque expresion[0:k] nunca tuvo mas CIERRES que APERTURAS.

# Supongamos que existe un prefijo mas largo s[0:k'] con k' > k que esta balanceado. Esto no es posible porque:
# - Nuestro algoritmo se detiene en k justo cuando el contador es 0 antes de decrementarlo ya que indica que tenemos un caracter de cierre sin apertura.
# - Si tenemos un CIERRE y el contador es igual a 0, eso significa que en expresion[0:k] tenemos un caracter de cierre sin apertura, con lo cual ningun prefijo
#   mas largo puede ser balanceado.

assert largo_prefijo_balanceado("()())(())()(()") == 4
