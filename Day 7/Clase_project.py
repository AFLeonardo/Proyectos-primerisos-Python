import time
import os

class persona:
    def __init__(self, Nombre, Apellido):
        self.Nombre = Nombre
        self.Apellido = Apellido
 
class cliente(persona):
    def __init__(self, Nombre, Apellido,Num_cuenta, Balance):
        super().__init__(Nombre, Apellido)
        self.Num_cuenta = Num_cuenta
        self.Balance =  Balance

    def __str__(self):
        return f"\nCliente: {self.Nombre} {self.Apellido} \nNumero de cuenta: {self.Num_cuenta} \nBalance: {self.Balance}"

    def Depositar(self):
        try:
            Monto = float(input("Ingrese el monto a depositar: "))
        except ValueError:
            while Monto <= 0:
                print("Error. Verifique que el monto sea mayor a 0.")
        else:
            while Monto <= 0:
                print("Error. Verifique que el monto sea mayor a 0.")
                Monto = float(input("Ingrese el monto a depositar: "))
            # Agrego el monto al balance
            self.Balance += Monto
            print(f"Se han agregado ${Monto} al balance.")
            time.sleep(3)

    def Retirar(self):
        try:
            Monto = float(input("Ingrese el monto a retirar: "))
        except ValueError:
            print("Error. Intenta de nuevo")
        else:
            while Monto > self.Balance:
                print("Saldo insuficiente. Intenta de nuevo")
                time.sleep(2)
                Monto = float(input("Ingrese el monto a retirar: "))
            
            # RETIRAR AL BALANCE EL MONTO RETIRADO
            self.Balance -= Monto

            input("Tome su dinero... dando enter")
            print(f"Ha tomado ${Monto}")
            time.sleep(3)