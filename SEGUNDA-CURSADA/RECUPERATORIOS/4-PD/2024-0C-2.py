# El papá de Pepe le dió n monedas para repartir entre él y su hermanito. El padre puso las monedas formando una única fila. Cada moneda tiene con diferente 
# valor vi. El padre de Pepe le dice que primero debe elegir una para él, y que sólo puede elegir la primera o la última de la fila. Luego, debe elegir una 
# para su hermano menor siguiendo la misma regla, luego otra para él, y así.

# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor máximo que pueda quedarse Pepe dadas estas condiciones (asumamos que usará 
# parte de sus ganancias para comprarle un chocolate a su hermano).

# Importante: antes de escribir código, plantear y explicar la ecuación de recurrencia correspondiente.

# ¿Que tipo de problema es?. Es un problema de maximizacion ya que nos puden obtener el valor maximo que pueda quedarse Pepe.

# ¿Que define si un subproblema es mas grande o pequeño?. La cantidad de monedas.

# Ejemplo: Consideremos el conjunto de monedas [2, 7, 4, 6].

# OPT[0,1] = max(2,7) = 7
# OPT[1,2] = max(7,4) = 7
# OPT[2,3] = max(4,6) = 6

# OPT[0,2] = max(2 + 7, 4 + 7) = max(2 + 7, 4 + 7) = max(9, 11) = 11
# OPT[1,3] = max(7 + 6, 6 + 7) = max(7 + 6, 6 + 7) = max(13, 13) = 13

# OPT[0,3] = max(2 + OPT[2,3], 2 + OPT[1,2], 6 + OPT[1,2], 6 + OPT[0,1]) = max(2 + 6, 2 + 7, 6 + 7, 6 + 7) = max(8, 9, 13, 13) = 13

# ¿Como se componen estos subproblemas para solucionar subproblemas mas grandes?.

# Casos:
# 1) Pepe elige la moneda de la izquierda (m_i) y su hermano elige la moneda de la izquierda (m_i+1)
# 2) Pepe elige la moneda de la izquierda (m_i) y su hermano elige la moneda de la derecha (m_d)
# 3) Pepe elige la moneda de la derecha (m_d) y su hermano elige la moneda de la izquierda (m_i)
# 4) Pepe elige la moneda de la derecha (m_d) y su hermano elige la moneda de la derecha (m_d-1) 

# Ecuacion de recurrencia: OPT[m_i, m_d] = max(monedas[m_i] + OPT[m_i+2, m_d],
#                                              monedas[m_i] + OPT[m_i+1, m_d-1],
#                                              monedas[m_d] + OPT[m_i+1, m_d-1],
#                                              monedas[m_d] + OPT[m_i, m_d-2])

# Restricciones:
# 1) m_i+2 < m_d
# 2) m_i+1 < m_d-1
# 3) m_i+1 < m_d-1
# 4) m_i < m_d-2

# Casos base:
# 1) Cuando no hay monedas
# 2) Cuando hay 1 moneda
# 3) Cuando hay 2 monedas

def juego_dinamico(monedas, n):
    mem = [[0 for _ in range(n)] for _ in range(n)]

    # Caso base 1
    for i in range(n):
        mem[i][i] = monedas[i]

    # Caso base 2
    for i in range(n-1):
        mem[i][i+1] = max(monedas[i], monedas[i+1])
    
    for ventana in range(2, n):
        for m_i in range(0, n - ventana):
            m_d = m_i + ventana

            # 1) Pepe elige la moneda de la izquierda (m_i) y elige la moneda de la izquierda (m_i+1) para su hermano
            opcion_1 = monedas[m_i] + mem[m_i+2][m_d] * (monedas[m_i+1] <= monedas[m_d] if m_i+2 <= m_d else 0)

            # 2) Pepe elige la moneda de la izquierda (m_i) y elige la moneda de la derecha (m_d) para su hermano
            opcion_2 = monedas[m_i] + mem[m_i+1][m_d-1] * (monedas[m_i+1] >= monedas[m_d] if m_i+1 <= m_d-1 else 0)

            # 3) Pepe elige la moneda de la derecha (m_d) y elige la moneda de la izquierda (m_i) para su hermano
            opcion_3 = monedas[m_d] + mem[m_i+1][m_d-1] * (monedas[m_i] <= monedas[m_d-1] if m_i+1 <= m_d-1 else 0)

            # 4) Pepe elige la moneda de la derecha (m_d) y elige la moneda de la derecha (m_d-1)  para su hermano
            opcion_4 = monedas[m_d] + mem[m_i][m_d-2] * (monedas[m_i] >= monedas[m_d-1] if m_i <= m_d-2 else 0)

            mem[m_i][m_d] = max(opcion_1, opcion_2, opcion_3, opcion_4)

    return mem

def juego(monedas):
    n = len(monedas)
    mem = juego_dinamico(monedas, n)
    return mem[0][n-1]

assert juego([2, 7, 4, 6]) == 13

assert juego([406,691,451,628,950,324,906,34,345,647,589,585,728,338,598,362,999,227,248,863,852,344,166,153,778]) == 9635

assert juego([96,594,437,674,950]) == 2218

assert juego([1,1,1,1,1,1,1,1,1,1]) == 5
assert juego([1,2,3,4,5,5,4,3,2,1]) == 15