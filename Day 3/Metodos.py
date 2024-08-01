texto = "Este es el texto de Federico"

resultado = texto.upper()
resultado = texto.lower()
resultado = texto.split() # Separa el texto de acuerdo a su parametro.

resultado = texto.replace("e","x")
print(resultado)
"""
Práctica Métodos de String 3

Reemplaza en la siguiente frase:

"Si la implementación es difícil de explicar, puede que sea una mala idea."

los siguientes pares de palabras:

    "difícil" --> "fácil"

    "mala" --> "buena"

y muestra en pantalla la frase con ambas palabras modificadas.

Resultado: 
    e = "Si la implementación es difícil de explicar, puede que sea una mala idea."
    a = e.replace("difícil","fácil").replace("mala","buena")
    print(a)
    
"""