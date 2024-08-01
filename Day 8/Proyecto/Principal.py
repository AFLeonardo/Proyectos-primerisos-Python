"""
Codigo principal del programa.
"""
import os
import time
import Numeros


def inicio():
    """
    Funcion donde se inicia el programa.
    """

    while True:

        try:
            os.system('cls')
            print("**** LEONARDO TURNOS ****")
            print("Bienvenid@")
            print("""
    Servicios disponibles:
        1. Perfumeria
        2. Enfermeria
        3. Cosmestica""")

            op = int(input("Seleccione un servicio: "))

            if op == 1:
                Numeros.Mostrar_turno(op)
            elif op == 2:
                Numeros.Mostrar_turno(op)
            elif op == 3:
                Numeros.Mostrar_turno(op)
            else:
                raise ValueError('Opción no válida')

        except ValueError:
            os.system('cls')
            print('Servicio no existente. \nPor favor seleccione uno valido.')
            time.sleep(2)
            continue

        else:
            # VERIFICAR QUE SELECIONE UNA OPCION VALIDA
            while True:
                repetir = input('¿Quieres generar otro turno? (S/N)').lower()
                if repetir == 's' or repetir == 'n':
                    break

            if repetir == 's':
                continue
            else:
                break


inicio()
