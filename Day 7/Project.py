import Clase_project as Clase
import os 

# FUNCIONES
def Inicio():
    print("*" * 30)
    print("Cuenta Bancaria")
    print("*" * 30)

    Nombre = input("Ingresa tu nombre: ")
    Apellido = input("Ingresa tu apellido: ")
    Num_cuenta = int(input("Ingresa tu numero de cuenta: "))
    Balance = float(input("Ingresa tu balance: "))
    
    
    Cliente = Crear_cliente(Nombre,Apellido,Num_cuenta,Balance)
    while True:
        os.system('cls')
        print(f"""Bienvenido {Cliente}
    1. Depositar
    2. Retirar
    3. Salir""")

        Op = int(input("Seleccionó: "))

        match(Op):
            case 1:
                Cliente.Depositar()
            case 2:
                Cliente.Retirar()
            case 3:
                break

    print(f"Le deseamos un buen día {Nombre}.")
        

def Crear_cliente(Nombre,Apellido,Num_cuenta,Balance):
    Cliente = Clase.cliente(Nombre,Apellido,Num_cuenta,Balance)
    return Cliente

Inicio()