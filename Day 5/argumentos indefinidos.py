# Practica 1
def suma_cuadrados(*args):
    total = 0
    for b in args:
        total += b**2
    return total


# Practica 2
def suma_absolutos(*args):
    suma = 0
    for n in args:
        suma += abs(n)
    return suma


# Practica 3
def numeros_persona(nombre,*args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    return f"{nombre}, la suma de tus números es {suma_numeros}"


# Practica **kargs 3
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")

    for k, v in kwargs.items():
        print(f"{k}: {v}")