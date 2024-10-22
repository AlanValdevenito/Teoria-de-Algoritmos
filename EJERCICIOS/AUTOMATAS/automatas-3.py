def es_parte_lenguaje(cadena):

    if len(cadena) < 2:
        return False

    if (cadena[0] == 'a') and (cadena[1] == 'c'):
        return True

    if cadena[-2] == 'a' and (cadena[-1] == 'b'):
        return True 
    
    return False