# Queremos determinar si un texto ininteligible, sin espacios, es en realidad un texto de un idioma, al que se le borraron los espacios
# (por ejemplo, "holaquehaces"). Contamos con un conjunto de las k palabras (muy cortas) del idioma en cuestión.

# Implementar un algoritmo que, utilizando programación dinámica, reciba el texto, y el conjunto de palabras del idioma, y determine si,
# en efecto, se trata de un texto del idioma, sin los espacios. 

# Por ejemplo, para "argentinacampeon" debe devolver true, mientras que para "awanteboke" debe devolver false. La resolución de este ejercicio puede 
# ser similar a la resolución del TP2 (curso regular)/Parte II (cursos anual y asincrónico). El ejercicio puede resolverse incluso de una forma 
# mejor (que a algunos puede resultarles más simple).

# Indicar y justificar la complejidad del algoritmo implementado.

# ¿Que tipo de problema es?. A diferencia de otros problemas de optimizacion donde nos piden maximizar/minimizar, este es un problema de decision ya
# que dado el listado de palabras, y una cadena desencriptada, nos piden determinar si es un posible mensaje.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad caracteres de la cadena desencriptada. El subproblema mas pequeño seria una cadena
# vacia.

# Ejemplo: Consideremos el listado de palabras ['argentina', 'hola', 'como', 'eso', 'es', 'zanahoria', 'andar', 'plancha', 'compra', 'reptiles', 'consistencia', 
# 'semana', 'votar', 'as', 'reto'] y la cadena desencriptada 'esandar'.

# OPT[0] = True (Caso base con una cadena vacia)

# OPT[1] = sum(OPT[j] and cadena[j:1] in palabras)
#          OPT[0] and cadena[0:1] in palabras = True and 'e' in palabras = True and False = False
# OPT[1] = 0 = False

# OPT[2] = sum(OPT[j] and cadena[j:2] in palabras)
#          OPT[0] and cadena[0:2] in palabras = True and 'es' in palabras = True and True = True
#          OPT[1] and cadena[1:2] in palabras = False and 's' in palabras = False and False = False
# OPT[2] = 1 + 0 = 1 = True

# OPT[3] = OPT[j] and cadena[j:3] in palabras
#          OPT[0] and cadena[0:3] in palabras = True and 'esa' in palabras = True and False = False
#          OPT[1] and cadena[1:3] in palabras = False and 'sa' in palabras = False and False = False
#          OPT[2] and cadena[2:3] in palabras = True and 'a' in palabras = True and False = False
# OPT[3] = 0 + 0 + 0 = False

# OPT[4] = OPT[j] and cadena[j:4] in palabras
#          OPT[0] and cadena[0:4] in palabras = True and 'esan' in palabras = True and False = False
#          OPT[1] and cadena[1:4] in palabras = False and 'san' in palabras = False and False = False
#          OPT[2] and cadena[2:4] in palabras = True and 'an' in palabras = True and False = False
#          OPT[3] and cadena[3:4] in palabras = False and 'n' in palabras = False and False = False
# OPT[4] = 0 + 0 + 0 + 0 = False

# OPT[5] = OPT[j] and cadena[j:5] in palabras
#          OPT[0] and cadena[0:5] in palabras = True and 'esand' in palabras = True and False = False
#          OPT[1] and cadena[1:5] in palabras = False and 'sand' in palabras = False and False = False
#          OPT[2] and cadena[2:5] in palabras = True and 'and' in palabras = True and False = False
#          OPT[3] and cadena[3:5] in palabras = False and 'nd' in palabras = False and False = False
#          OPT[4] and cadena[4:5] in palabras = False and 'd' in palabras = False and False = False
# OPT[5] = 0 + 0 + 0 + 0 + 0 = False

# OPT[6] = OPT[j] and cadena[j:6] in palabras
#          OPT[0] and cadena[0:6] in palabras = True and 'esanda' in palabras = True and False = False
#          OPT[1] and cadena[1:6] in palabras = False and 'sanda' in palabras = False and False = False
#          OPT[2] and cadena[2:6] in palabras = True and 'anda' in palabras = True and False = False
#          OPT[3] and cadena[3:6] in palabras = False and 'nda' in palabras = False and False = False
#          OPT[4] and cadena[4:6] in palabras = False and 'da' in palabras = False and False = False
#          OPT[5] and cadena[5:6] in palabras = False and 'a' in palabras = False and False = False
# OPT[6] = 0 + 0 + 0 + 0 + 0 + 0 = False

# OPT[7] = OPT[j] and cadena[j:7] in palabras
#          OPT[0] and cadena[0:7] in palabras = True and 'esandar' in palabras = True and False = False
#          OPT[1] and cadena[1:7] in palabras = False and 'sandar' in palabras = False and False = False
#          OPT[2] and cadena[2:7] in palabras = True and 'andar' in palabras = True and True = True
#          OPT[3] and cadena[3:7] in palabras = False and 'ndar' in palabras = False and False = False
#          OPT[4] and cadena[4:7] in palabras = False and 'dar' in palabras = False and False = False
#          OPT[5] and cadena[5:7] in palabras = False and 'ar' in palabras = False and False = False
#          OPT[6] and cadena[6:7] in palabras = False and 'r' in palabras = False and False = False
# OPT[7] = 0 + 0 + 1 + 0 + 0 + 0 + 0 = True

# OPT = [True, False, True, False, False, False, False, True]

# Ecuacion de recurrencia: OPT[i] = sum(OPT[j] and cadena[j:i] in palabras) para todo 0 <= j < i

def texto_dinamico(palabras, texto_ininteligible, n):
    mem = [True] * (n+1)

    for i in range(1, n+1):
        pertenece = 0
        # print("\n")
        for j in range(0, i):
            # print(f"OPT[{i}] = OPT[{j}] and cadena[{j}][{i}] in palabras = {mem[j]} and {texto_ininteligible[j:i] in palabras}")
            pertenece += mem[j] and texto_ininteligible[j:i] in palabras

        mem[i] = True if pertenece > 0 else False

    return mem

def texto(palabras, texto_ininteligible):
    n = len(texto_ininteligible)
    mem = texto_dinamico(palabras, texto_ininteligible, n)
    return mem[n]

# Complejidad

# Matriz de memorizacion: Para cada largo 0 < i <= n recorremos todas las subcadenas desde j hasta i con 0 <= j < i.

# La complejidad total resulta ser O(n^2) con n el largo del texto ininteligible.

assert texto({'argentina', 'hola', 'como', 'eso', 'es', 'zanahoria', 'andar', 
              'plancha', 'compra', 'reptiles', 'consistencia', 'semana', 'votar', 'as', 'reto'}, 'esandar') == True