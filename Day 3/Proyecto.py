# Analizador de texto
""""
Ingresa un texto
Pide al usuario ingresar 3 letras

El programa devuelve:
1 - Cuantas veces apararece cada letra
2 - Cuantas palabras hay en total
3 - Primera y ultima letra
4 - Como queda el texto si se invierte el orden de las palabras.
5 - Verificar si la palabra Python aparece dentro del texto.
"""

print("### Python analiza tu texto...\n")
texto = input("Ingresa un texto:\n").lower()
lista_letras = [
    input("Ingresa una primera letra: ").lower(),
    input("Ingresa una segunda letra: ").lower(),
    input("Ingresa una tercera letra: ").lower()]

# Proceso para ver las veces que aparece x letra en el texto.
cantidad_letra1 = texto.count(lista_letras[0])
cantidad_letra2 = texto.count(lista_letras[1])
cantidad_letra3 = texto.count(lista_letras[2])

# Proceso para saber la cantidad de palabras en total
palabras_totales = len(texto.split())

# Proceso para saber primera y ultima letra
primeraletra = texto[0]
ultimaletra = texto[-1]

# Invertir el orden
texto_invertido = texto[::-1]

# Python aparece?
aparece_python = 'python' in texto
dic_Python = {True: 'Si existe en el texto', False: 'No existe en el texto'}

print("\n### Resultados ###\n".upper())
print(f"1.\nLa letra {lista_letras[0]} esta presente en el texto", cantidad_letra1, "veces.")
print(f"La letra {lista_letras[1]} esta presente en el texto", cantidad_letra2, "veces.")
print(f"La letra {lista_letras[2]} esta presente en el texto", cantidad_letra3, "veces.")

print("\n2.\nLa cantidad de palabras totales son: ", palabras_totales)
print(f"\n3. \nLa primera letra del texto es : {primeraletra} \nLa ultima letra es : {ultimaletra}")
print("\n4. \nEl orden del texto invertido es: ", texto_invertido)
print("\n5. \nPython aparece en el texto? ".upper(), '\n', dic_Python[aparece_python])
