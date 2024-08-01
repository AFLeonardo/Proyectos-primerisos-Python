""" def suma (**kwargs):

    total = 0

    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=2, y=45, u=9))
 """

# Definir una cadena de texto
cadena = "Hola, ¿cómo estás? Espero que bien."

# Dividir la cadena en una lista de palabras
palabras = cadena.split()

# Imprimir la lista de palabras
print(palabras)
