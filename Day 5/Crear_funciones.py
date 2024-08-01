def saludo(nombre):
    """
    Esta funcion sirve para saludar a las personas.
    """
    print("Hola", nombre)


saludo('Jker')


# Funcion Return

def multiplicar(numero1, numero2):
    return numero1 * numero2


resultado = multiplicar(6, 7)
print(resultado)

# Practica Return 3
def invertir_palabra(texto):
    t = texto[::-1].upper()
    return t


palabra = "Hola"
