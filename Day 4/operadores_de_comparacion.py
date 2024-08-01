var = "Hola mundo"
print(var == 10)

#Nota: Los strings son sensibles a mayusculas.

#Ejercicio Operadores logicos 3
"""
Verifica si las palabras almacenadas en las siguientes variables:

palabra1 = "éxito", y
palabra2 = "tecnología" 

no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación
(un booleano) en una variable llamada mi_bool:

"Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades
de que salga bien no te acompañan"
Elon Musk
"""

#Respuesta
frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = palabra1 and palabra2 not in frase
print(mi_bool)
