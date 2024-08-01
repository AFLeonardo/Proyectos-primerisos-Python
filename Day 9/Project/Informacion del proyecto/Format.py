import math
from datetime import date, time, datetime


def Tiket(Nums_serie, Tiempo):

    """
        Funcion que imprime el ticket al usurio.
    """
    Today_Date = datetime.now()
    Today_Date = Today_Date.strftime('%d-%m-%y')

    print('-'*50)
    print('Fecha de busqueda: ', Today_Date)
    print('\nARCHIVO\t\t NUM. SERIE')
    print('-----\t\t -----', '\n')
    for Archivo, Numero in Nums_serie.items():
        print(Archivo, '\t', Numero)

    print('\nNumeros encontrados:', len(Nums_serie))
    print('Duracion de la busqueda:', math.ceil(Tiempo), 'segundos')
    print('-'*50)

