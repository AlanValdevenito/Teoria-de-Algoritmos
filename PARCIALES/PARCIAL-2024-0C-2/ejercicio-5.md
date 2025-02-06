# Enunciado

Indicar si las siguientes afirmaciones sobre Redes de Flujo son verdaderas o falsas, justificando detalladamente.

a. Si aumentamos la capacidad de todas las aristas por una constante K, implicará que el flujo máximo aumente en
[K × min (grado_salida[fuente], grado_entrada[sumidero])] unidades.

b. En el caso del flujo máximo de la red, aumentarle la capacidad a una arista cuya capacidad no fue consumida no
tienen ningún efecto sobre el flujo máximo.

c. Eliminar una arista al azar del grafo puede no afectar el flujo máximo, pero si eliminamos una arista que es parte
del corte mínimo, entonces obligatoriamente sí afectará al flujo máximo.

# Solucion

a. Falso. El flujo máximo está limitado por el corte mínimo, es decir, la menor capacidad total de un conjunto de aristas que separa la fuente del sumidero. La ecuación dada es incorrecta, ya que el flujo máximo depende de las aristas con baja capacidad en la red, y no simplemente del grado de los vértices.

Si la red tiene una arista con baja capacidad, incrementar todas las capacidades en K no cambiará el flujo si dicha arista sigue restringiendo el paso del flujo.

Basicamente el grado de salida/entrada de la fuente y el sumidero no influyen en el flujo maximo. Lo que influye en el flujo maximo es la capacidad de las aristas, no la cantidad de ellas.

b. Verdadero. Aumentar su capacidad no cambiará el flujo máximo, ya que el flujo está limitado por otras aristas más restrictivas en el camino entre la fuente y el sumidero. Si en un flujo máximo tenemos una arista de capacidad 10 pero solo se está usando 5, aumentarla a 15 no cambiará nada porque el flujo ya estaba limitado en otro punto de la red.

Otro ejemplo seria si tuviesesmos 2 aristas con capacidad 1, aunque aumentaramos la capacidad de alguna de ellas a 1000
solamente podria fluir 1 de flujo.

c. Verdadero. No todas las aristas afectan el flujo máximo; eliminar una arista no utilizada o con capacidad sobrante no cambia el flujo máximo. Sin embargo, si eliminamos una arista del corte mínimo, forzosamente reduciremos la capacidad del corte mínimo y, por lo tanto, el flujo máximo disminuirá.

¿Por que?. Esto se debe a que el teorema $max flow min cut$ establece que el flujo máximo es igual a la capacidad del corte mínimo.

Supongamos que el corte mínimo de una red tiene capacidad 20, y que una de sus aristas tiene capacidad 5. Si eliminamos esa arista, la capacidad del corte se reduce a 15, y el flujo máximo también disminuye a ≤ 15.