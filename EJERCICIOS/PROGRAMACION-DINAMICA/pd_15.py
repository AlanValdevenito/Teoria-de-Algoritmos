# Dada una soga de n metros (n mayor o igual a 2) implementar un algoritmo que, utilizando programación dinámica, permita 
# cortarla (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. 

# El algoritmo debe devolver el valor del producto máximo alcanzable. Tener en cuenta que la soga puede cortarse varias veces, como 
# se muestra en el ejemplo con n = 10.

# Indicar y justificar la complejidad del algoritmo.

# Ejemplos:
# n = 2 ⇾ Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 ⇾ Debe devolver 2 (producto máximo es 2 * 1)
# n = 4 ⇾ Debe devolver 4 (producto máximo es 2 * 2)
# n = 5 ⇾ Debe devolver 6 (producto máximo es 2 * 3)
# n = 6 ⇾ Debe devolver 9 (producto máximo es 3 * 3)
# n = 7 ⇾ Debe devolver 12 (producto máximo es 3 * 4)
# n = 10 ⇾ Debe devolver 36 (producto máximo es 3 * 3 * 4)

# Ecuacion de recurrencia:

# OPT(n) = max{no subdividir, subdividir el lado derecho, subdividir el lado izquierdo, subdividir ambos lados} =
#        = max(max{i * (n-i), i * OPT(n-i), OPT(i) * (n-i), OPT(i) * OPT(n-i)}) para todo corte i perteneciente a [1, n-1]

# OPT(n) = max(max{no subdividir el lado izquierdo, subdividir el lado izquierdo} * max{no subdividir el lado derecho, subdividir el lado derecho}) = 
#   = max(max{i, OPT(i)} * max{n-i, OPT(n-i)}) para todo corte i perteneciente a [1, n-1]

def problema_soga_dinamico(n):
    mem = [0] * (n+1)

    for i in range(2, n+1):

        cortes = []
        for j in range(1, n):
            cortes.append(max(j, mem[j]) * max(i-j, mem[i-j]))

        mem[i] = max(cortes)
    
    return mem

def problema_soga(n):
    mem = problema_soga_dinamico(n)
    print(mem)
    return mem[n]

# Complejidad: Tenemos O(n^2) por calcular la matriz de memorizacion.

assert problema_soga(2) == 1
assert problema_soga(3) == 2
assert problema_soga(4) == 4
assert problema_soga(5) == 6
assert problema_soga(6) == 9
assert problema_soga(7) == 12
assert problema_soga(10) == 36

# Tests RPL

assert problema_soga(2) == 1
assert problema_soga(3) == 2
assert problema_soga(5) == 6
assert problema_soga(6) == 9
assert problema_soga(7) == 12
assert problema_soga(8) == 18
assert problema_soga(9) == 27
assert problema_soga(10) == 36
assert problema_soga(11) == 54
assert problema_soga(12) == 81
assert problema_soga(30) == 59049