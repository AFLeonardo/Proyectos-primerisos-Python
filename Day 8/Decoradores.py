# def cambia_letras(tipo):
#
#
#     def mayuscula(texto):
#         print(texto.upper())
#
#
#     def minuscula(texto):
#         print(texto.lower())
#
#     if tipo == 'may':
#         return mayuscula
#     elif tipo == 'min':
#         return minuscula
#
# op = cambia_letras('min')
#
# op("palabra")

# TODO EN PYTHON SON OBJETOS

def Decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')

    return otra_funcion

@Decorar_saludo
def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())

minuscula('Hola')