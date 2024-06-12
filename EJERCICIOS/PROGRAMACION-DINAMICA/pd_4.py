# Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias, pero no quiere trabajar dos días seguidos. 
# Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación dinámica, el máximo monto a ganar, sabiendo que 
# no aceptará trabajar dos días seguidos. 

# Hacer una reconstrucción para verificar qué días debe trabajar. 
# Indicar y justificar la complejidad del algoritmo implementado.

# Ejemplo: Consideremos el arreglo [100, 20, 30, 70, 50] de ganancias. La ganancia maxima obtenible seria 180 atracando
#          las casas [0, 2, 4].

# OPT(0) = 0
# OPT(1) = 100
# OPT(2) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{0+20, 100} = 100
# OPT(3) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{100+30, 100} = 130
# OPT(4) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{70+100, 130} = 170
# OPT(5) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{130+50, 170} = 180
# OPT(6) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{5+170, 180} = 180

# Ecuacion de recurrencia: OPT(i) = max{robar esta casa y no la anterior, no robar esta casa y si la anterior} = max{OPT(i-2) + gi, OPT(i-1)} para i >=2.

def juan_el_vago_dinamico(trabajos, n):
    mem = [0] * (n)
    mem[0] = trabajos[0]
    mem[1] = max(trabajos[0], trabajos[1])

    for i in range(2, n):
        mem[i] = max(trabajos[i] + mem[i-2], mem[i-1])

    return mem

def juan_el_vago_solucion(mem, trabajos, dia):
    solucion = []

    while (dia >= 0):
        trabajar = (mem[dia-2] if dia > 1 else 0) + trabajos[dia]
        no_trabajar = mem[dia-1] if dia > 0 else 0

        if (trabajar >= no_trabajar):
            solucion.append(dia)
            dia -= 2
        else:
            dia -= 1

    solucion.reverse()
    return solucion

def juan_el_vago(trabajos):
    n = len(trabajos)

    if n == 0:
        return []
    
    if n == 1:
        return [0]
    
    if n == 2:
        return [0] if (trabajos[0] >= trabajos[1]) else [1]

    mem = juan_el_vago_dinamico(trabajos, n)
    return juan_el_vago_solucion(mem, trabajos, n-1)

# Complejidad: Tenemos O(n) por calcular la matriz de memorizacion y O(n) por recuperar la solucion. Luego, la 
#              complejidad total es O(n).

assert juan_el_vago([100,20,30,70,50]) == [0,2,4]
assert juan_el_vago([100,20,30,70,20]) == [0,3]