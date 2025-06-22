# Demostracion

Para demostrar que el problema de X es un problema NP-Completo debemos:
- Demostrar que el problema se encuentra en NP
- Reducir el problema de Y al problema de X: Y $\leq_P$ X

Nota: Para la segunda demostracion es importante demostrar que nuestra reduccion es correcta demostrando la doble implicacion.

La segunda demostracion nos indica que el problema de X es al menos tan dificil de resolver como el problema de Y. Esto significa que resolver el problema de Y puede ser transformado en resolver el problema de X.

## Demostracion I: El problema se encuentra en NP

Para que el problema se encuentre en NP, debe haber un verificador eficiente.

En otras palabras, debe haber un verificador que ejecute en tiempo polinomial.

Verificador: Recibe una instancia del problema y una solucion.

```py
def verificador(solucion):
    pass
```

Complejidad: ...

Luego, se ejecuta en tiempo polinomial, lo cual quiere decir que el problema se encuentra en NP.

## Demostracion II: Reduccion de un problema NP-Completo

Debemos demostrar que Y $\leq_P$ X.

### Reduccion planteada

¿Podemos resolver el problema de Y utilizando la solucion del problema de X?.

Vamos a utilizar una caja negra que resuelve el problema de X para resolver el problema de Y.

El problema de Y recibe...

Transformacion del problema: Transformamos la entrada del problema de Y en una entrada del problema X
- ...

Esta transformacion requiere una cantidad de pasos polinomiales.

A continuacion, para demostrar que la reduccion es correcta, debemos demostrar que:

Hay solucion de Y, si y solo si, hay solucion para el problema de X.

Para demostrar ambas implicaciones tenemos dos opciones:
- Metodo directo, asumiendo para cada una que la hipotesis es cierta.
- Metodo por absurdo.

### Si hay Y, entonces hay X

Hipotesis: ...
Tesis: ...

Nota: No estamos cualquier instancia posible de X, sino una que resulta de la reduccion planteada.

### Si hay X, entonces hay Y

Hipotesis: ...
Tesis: ...

Nota: No estamos cualquier instancia posible de X, sino una que resulta de la reduccion planteada.

# Conclusion

Habiendo demostrado que la reduccion es correcta, queda demostrado tambien que el problema de X es un problema NP-Completo.