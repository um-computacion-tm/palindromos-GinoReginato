# README 

### AUTOR

#### Gino Reginato

## Descripción 

Este código en Python define una función llamada is_palindrome que toma una cadena de texto como entrada (mystring) y verifica si es un palíndromo, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda, ignorando los espacios y sin distinguir entre mayúsculas y minúsculas.

El proceso dentro de la función es el siguiente:

>1)- Primero, se limpia la cadena de texto eliminando los espacios y convirtiendo todas las letras a minúsculas utilizando el método replace y lower(). El resultado se guarda en la variable cleaned_string.

> 2)- Luego, se itera sobre la longitud de la cadena limpia (cleaned_string) utilizando un bucle for y el rango de números generados por range(len(cleaned_string)).

> 3)- En cada iteración, se compara el carácter en la posición actual (cleaned_string[indice]) con el carácter en la posición correspondiente desde el final de la cadena (cleaned_string[-(indice + 1)]). Si estos caracteres no son iguales, se imprime "no es" y la función devuelve False, indicando que la cadena no es un palíndromo.

> 4)- Si todas las comparaciones son iguales, es decir, si nunca se encontró una discrepancia entre los caracteres en posiciones opuestas, se imprime "es" y la función devuelve True, indicando que la cadena es un palíndromo.

En resumen, este código verifica si una cadena de texto es un palíndromo y devuelve True si lo es, o False si no lo es.