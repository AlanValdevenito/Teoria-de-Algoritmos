# Es el año 1700, y la pirata Barba-ra Verde atacó un barco de la Royal British Shipping & Something, que transportaba una importante 
# piedra preciosa de la corona británica. Al parecer, la escondieron en un cofre con muchas piedras preciosas falsas, en caso de un ataque. 
# Barba-ra Verde sabe que los refuerzos británicos no tardarán en llegar, y deben huir lo más rápido posible. El problema es que no pueden 
# llevarse el cofre completo por pesar demasiado. Necesita encontrar rápidamente la joya verdadera. La única forma de descubrir la joya 
# verdadera es pesando. Se sabe que la joya verdadera va a pesar más que las imitaciones, y que las imitaciones pesan todas lo mismo. 
# Cuenta con una balanza de platillos para poder pesarlas (es el 1700, no esperen una balanza digital).

# Función balanza: Se le deben pasar los dos conjuntos de joyas a verificar. La cantidad de joyas en cada conjunto debe ser la misma, para 
# que el resultado de la balanza de platillos nos dé información.
# - Si los dos platillos pesan lo mismo, balanza devuelve 0.
# - Si el primer platillo es más pesado, balanza devuelve 1.
# - Si el segundo platillo es más pesado, balanza devuelve -1.

JOYA = 1

def balanza(joya1, joya2):

    if (JOYA not in joya1) and (JOYA not in joya2):
        return 0
    
    return 1 if (JOYA in joya1) else -1

def _encontrar_joya(joyas, desde, hasta):

    if desde >= hasta:
        return desde

    medio = (desde + hasta) // 2

    conjunto1 = joyas[desde:medio+1]
    conjunto2 = joyas[medio+1:hasta+1]

    if len(conjunto1) != len(conjunto2):

        if len(conjunto1) > len(conjunto2):
            conjunto1 = conjunto1[:-1]

        elif len(conjunto2) > len(conjunto1):
            conjunto2 = conjunto2[:-1]

    peso = balanza(conjunto1, conjunto2)

    if peso == 0:
        return medio
    
    if peso == 1:
        return _encontrar_joya(joyas, desde, medio-1)
    
    return _encontrar_joya(joyas, medio+1, hasta)
    
def encontrar_joya(joyas):
    n = len(joyas)
    return _encontrar_joya(joyas, 0, n-1)

assert encontrar_joya([1, 0]) == 0
assert encontrar_joya([0, 1]) == 1
assert encontrar_joya([1, 0, 0]) == 0
assert encontrar_joya([0, 1, 0]) == 1
assert encontrar_joya([0, 0, 1]) == 2
assert encontrar_joya([0, 0, 1, 0]) == 2
assert encontrar_joya([0, 0, 1, 0, 0]) == 2
assert encontrar_joya([0, 0, 0, 0, 0, 1]) == 5
assert encontrar_joya([0, 0, 0, 0, 0, 0, 1]) == 6