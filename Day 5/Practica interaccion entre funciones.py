from random import *

numeros = list(range(1, 7))


# Arroja los dados
# Practica 1
def lanzar_dados():
    dado1 = choice(numeros)
    dado2 = choice(numeros)
    return dado1, dado2


dado_1, dado_2 = lanzar_dados()


# Evaluar jugada
def evaluar_jugada(dado_1, dado_2):
    suma = dado_1 + dado_2
    if suma <= 6:
        return f"La suma de tus dados es {suma}. Lamentable"
    elif suma > 6 and suma < 10:
        return f"La suma de tus dados es {suma}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma}. Parece una jugada ganadora"


evaluar_jugada(dado_1, dado_2)

# Practica 2
lista_numeros = [9, 9, 8, 6, 4, 2, 5, 645, 12, 23354, 6, 54, 45]


# def reducir_lista(lista):
#     i = 0
#     for n in range(0, len(lista)):
#         if n == lista[i]:
#             lista[i].pop(n)
#             i += 1
#         else:
#             pass
#     return lista
def reducir_lista(lista):
    lista = list(set(lista))
    lista.sort()  # Orden la lista en orden mayor a menor
    lista.pop(-1)
    return list(lista)


def promedio(lista_clean):
    prom = 0
    for n in lista_clean:
        prom += n
    prom /= len(lista_clean)
    return prom

# Practica 3
# from random import *


def lanzar_moneda():
    resultado = ['Cara', 'Cruz']
    resultado = choice(resultado)
    return resultado


def probar_suerte(lanzamiento_r, lista):
    if lanzamiento_r == "Cara":
        print("La lista se autodestruirá")
        lista = lista_d = []
        return lista
    else:
        print("La lista fue salvada")
        return lista


lista_numeros = [3, 5, 1, 32, 45, 23, 53, 543, 532, 55]