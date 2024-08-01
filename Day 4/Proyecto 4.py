# Juego
# Tienes 8 intentos para adivinar el numero
# Opciones de respuesta:
# 1. Si el input es menor a 1 o superior a 100 - El sistema dice elegio un numero no permitido.
# 2. El input es menor - El sistema dice que el numero es menor y que esta incorrecto.
# 3. Input mayor - El sistema dice que el numero es mayor y esta incorrecto.
# 4. Input correcto - El sistema dice que ha ganado y la cantidad de intentos que le ha tomado.
# 5. Si se acaban los intentos, se le dice game over

#Librerias
from random import *
numero = randint(1,101)
intentos = 1
numero_usuario = 0

nombre = input("Hola soy XRobot, Cual es tu nombre?\n")
print(f"Ok {nombre}, vamos a jugar un juego muy DIVERTIDO :D\n")
print("#################\n      Reglas\n#################\n1. Solo tienes 8 intentos. \n2. No se introducen numeros menores a 0. \n3. Diviertete y no chille princesa.")
print("\nEMPEZAMOOOOOS!")

while numero != numero_usuario:
    print(f"\n##############INTENTO {intentos}##############")
    numero_usuario = int(input("Ingresa el numero que creas que es: "))

    if intentos <= 9:
        if numero_usuario < 1 or numero_usuario > 100:

            print("Nooop 🔫. TE DIJE QUE NO SE VALEN NUMERO MENORES A 1 O MAYORES A 100!. Intenta de nuevo.")
            intentos += 1

        elif numero_usuario > numero:

            print("Mi numero es menor. Intenta de nuevo.")
            intentos += 1

        elif numero_usuario < numero:

            print("Mi numero es mayor. Intenta de nuevo.")
            intentos += 1

        elif numero_usuario == numero:
            print(f"\nWOOOOOOOOOOOW has acertadooo! 😯🥳\nFelicitaciones has ganado el juego. \n##############Estadisticas##############\n * Intentos: {intentos}")
            print(f"\nEl numero correcto es: {numero}")
            break
    else:
        print("\nLo sentimos has perdido.")
        print(f"\n###### Estadisticas ######\n * Intentos: {intentos}")
        print(f"\nEl numero correcto era: {numero}")
        break