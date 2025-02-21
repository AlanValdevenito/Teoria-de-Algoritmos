# Resolver el problema anterior, pero esta vez para encontrar el largo de la subsecuencia balanceada más larga de
# una expresión (en este caso, no necesariamente comenzando en el inicio). Para esto, utilizar programación dinámica. La
# solución a este problema no dista mucho al planteo de la parte 2 del TP. 

# Escribir y describir la ecuación de recurrencia de la solución, e indicar y justificar la complejidad del algoritmo implementado.

# Ejemplo: para ()())(())()((), la respuesta es 6 (comenzando en la posición 5).

#                                     { 0                           si i >= j
# Ecuacion de recurrencia: OPT(i,j) = { max{OPT(i+1,j), OPT(i,j-1)} si cadena[i] y cadena[j] no forman un par balanceado
#                                     { 2 + OPT(i+1.j-1)            si cadena[i] y cadena[j] forman un par balanceado
#                                     { 2 + OPT(i+2.j)              si cadena[i] y cadena[i+1] forman un par balanceado
#                                     { 2 + OPT(i.j-2)              si cadena[j] y cadena[j-1] forman un par balanceado

def largo_subsecuencia_balanceada_dinamico(cadena, n):
    mem = [[0 for _ in range(n)] for _ in range(n)]

    for ventana in range(2, n):
        # print("")
        for i in range(n - ventana):
            j = i + ventana

            if (cadena[i] == '(') and (cadena[j] == ')'):
                mem[i][j] = 2 + (mem[i+1][j-1] if i+1 < j-1 else 0)

                # print(f"Cadena: {cadena[i:j+1]} → Caso 2 → OPT({i}, {j}) = 2 + {(mem[i+1][j-1] if i+1 < j-1 else 0)}")

            else:
                op1 = mem[i+1][j] if i < j else 0
                op2 = mem[i][j-1] if i < j else 0

                mem[i][j] = max(op1, op2)

                # print(f"Cadena: {cadena[i:j+1]} → Caso 1 → OPT({i}, {j}) = max({op1}, {op2}) = {mem[i][j]}")

    return mem

def largo_subsecuencia_balanceada(cadena):
    n = len(cadena)

    mem = largo_subsecuencia_balanceada_dinamico(cadena, n)

    return mem[0][n-1]

assert largo_subsecuencia_balanceada("()())(())()(()") == 6

# Seguimiento: "()())(())()(()"

# Cadena: ()( → Caso 1 → OPT(0, 2) = max(0, 0) = 0
# Cadena: )() → Caso 1 → OPT(1, 3) = max(0, 0) = 0
# Cadena: ()) → Caso 2 → OPT(2, 4) = 2 + 0
# Cadena: ))( → Caso 1 → OPT(3, 5) = max(0, 0) = 0
# Cadena: )(( → Caso 1 → OPT(4, 6) = max(0, 0) = 0
# Cadena: (() → Caso 2 → OPT(5, 7) = 2 + 0
# Cadena: ()) → Caso 2 → OPT(6, 8) = 2 + 0
# Cadena: ))( → Caso 1 → OPT(7, 9) = max(0, 0) = 0
# Cadena: )() → Caso 1 → OPT(8, 10) = max(0, 0) = 0
# Cadena: ()( → Caso 1 → OPT(9, 11) = max(0, 0) = 0
# Cadena: )(( → Caso 1 → OPT(10, 12) = max(0, 0) = 0
# Cadena: (() → Caso 2 → OPT(11, 13) = 2 + 0

# Cadena: ()() → Caso 2 → OPT(0, 3) = 2 + 0
# Cadena: )()) → Caso 1 → OPT(1, 4) = max(2, 0) = 2
# Cadena: ())( → Caso 1 → OPT(2, 5) = max(0, 2) = 2
# Cadena: ))(( → Caso 1 → OPT(3, 6) = max(0, 0) = 0
# Cadena: )(() → Caso 1 → OPT(4, 7) = max(2, 0) = 2
# Cadena: (()) → Caso 2 → OPT(5, 8) = 2 + 0
# Cadena: ())( → Caso 1 → OPT(6, 9) = max(0, 2) = 2
# Cadena: ))() → Caso 1 → OPT(7, 10) = max(0, 0) = 0
# Cadena: )()( → Caso 1 → OPT(8, 11) = max(0, 0) = 0
# Cadena: ()(( → Caso 1 → OPT(9, 12) = max(0, 0) = 0
# Cadena: )(() → Caso 1 → OPT(10, 13) = max(2, 0) = 2

# Cadena: ()()) → Caso 2 → OPT(0, 4) = 2 + 0
# Cadena: )())( → Caso 1 → OPT(1, 5) = max(2, 2) = 2
# Cadena: ())(( → Caso 1 → OPT(2, 6) = max(0, 2) = 2
# Cadena: ))(() → Caso 1 → OPT(3, 7) = max(2, 0) = 2
# Cadena: )(()) → Caso 1 → OPT(4, 8) = max(2, 2) = 2
# Cadena: (())( → Caso 1 → OPT(5, 9) = max(2, 2) = 2
# Cadena: ())() → Caso 2 → OPT(6, 10) = 2 + 0
# Cadena: ))()( → Caso 1 → OPT(7, 11) = max(0, 0) = 0
# Cadena: )()(( → Caso 1 → OPT(8, 12) = max(0, 0) = 0
# Cadena: ()(() → Caso 2 → OPT(9, 13) = 2 + 0

# Cadena: ()())( → Caso 1 → OPT(0, 5) = max(2, 2) = 2
# Cadena: )())(( → Caso 1 → OPT(1, 6) = max(2, 2) = 2
# Cadena: ())(() → Caso 2 → OPT(2, 7) = 2 + 0
# Cadena: ))(()) → Caso 1 → OPT(3, 8) = max(2, 2) = 2
# Cadena: )(())( → Caso 1 → OPT(4, 9) = max(2, 2) = 2
# Cadena: (())() → Caso 2 → OPT(5, 10) = 2 + 2
# Cadena: ())()( → Caso 1 → OPT(6, 11) = max(0, 2) = 2
# Cadena: ))()(( → Caso 1 → OPT(7, 12) = max(0, 0) = 0
# Cadena: )()(() → Caso 1 → OPT(8, 13) = max(2, 0) = 2

# Cadena: ()())(( → Caso 1 → OPT(0, 6) = max(2, 2) = 2
# Cadena: )())(() → Caso 1 → OPT(1, 7) = max(2, 2) = 2
# Cadena: ())(()) → Caso 2 → OPT(2, 8) = 2 + 2
# Cadena: ))(())( → Caso 1 → OPT(3, 9) = max(2, 2) = 2
# Cadena: )(())() → Caso 1 → OPT(4, 10) = max(4, 2) = 4
# Cadena: (())()( → Caso 1 → OPT(5, 11) = max(2, 4) = 4
# Cadena: ())()(( → Caso 1 → OPT(6, 12) = max(0, 2) = 2
# Cadena: ))()(() → Caso 1 → OPT(7, 13) = max(2, 0) = 2

# Cadena: ()())(() → Caso 2 → OPT(0, 7) = 2 + 2
# Cadena: )())(()) → Caso 1 → OPT(1, 8) = max(4, 2) = 4
# Cadena: ())(())( → Caso 1 → OPT(2, 9) = max(2, 4) = 4
# Cadena: ))(())() → Caso 1 → OPT(3, 10) = max(4, 2) = 4
# Cadena: )(())()( → Caso 1 → OPT(4, 11) = max(4, 4) = 4
# Cadena: (())()(( → Caso 1 → OPT(5, 12) = max(2, 4) = 4
# Cadena: ())()(() → Caso 2 → OPT(6, 13) = 2 + 0

# Cadena: ()())(()) → Caso 2 → OPT(0, 8) = 2 + 2
# Cadena: )())(())( → Caso 1 → OPT(1, 9) = max(4, 4) = 4
# Cadena: ())(())() → Caso 2 → OPT(2, 10) = 2 + 2
# Cadena: ))(())()( → Caso 1 → OPT(3, 11) = max(4, 4) = 4
# Cadena: )(())()(( → Caso 1 → OPT(4, 12) = max(4, 4) = 4
# Cadena: (())()(() → Caso 2 → OPT(5, 13) = 2 + 2

# Cadena: ()())(())( → Caso 1 → OPT(0, 9) = max(4, 4) = 4
# Cadena: )())(())() → Caso 1 → OPT(1, 10) = max(4, 4) = 4
# Cadena: ())(())()( → Caso 1 → OPT(2, 11) = max(4, 4) = 4
# Cadena: ))(())()(( → Caso 1 → OPT(3, 12) = max(4, 4) = 4
# Cadena: )(())()(() → Caso 1 → OPT(4, 13) = max(4, 4) = 4

# Cadena: ()())(())() → Caso 2 → OPT(0, 10) = 2 + 4
# Cadena: )())(())()( → Caso 1 → OPT(1, 11) = max(4, 4) = 4
# Cadena: ())(())()(( → Caso 1 → OPT(2, 12) = max(4, 4) = 4
# Cadena: ))(())()(() → Caso 1 → OPT(3, 13) = max(4, 4) = 4

# Cadena: ()())(())()( → Caso 1 → OPT(0, 11) = max(4, 6) = 6
# Cadena: )())(())()(( → Caso 1 → OPT(1, 12) = max(4, 4) = 4
# Cadena: ())(())()(() → Caso 2 → OPT(2, 13) = 2 + 4

# Cadena: ()())(())()(( → Caso 1 → OPT(0, 12) = max(4, 6) = 6
# Cadena: )())(())()(() → Caso 1 → OPT(1, 13) = max(6, 4) = 6

# Cadena: ()())(())()(() → Caso 2 → OPT(0, 13) = 2 + 4
