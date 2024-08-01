# Practica 2
def suma_menores(lista):
    suma = 0
    for n in lista:
        if n > 0 and n < 1000:
            suma += n
    return suma

#Practica 3
def cantidad_pares(lista):
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            pass
    return pares

