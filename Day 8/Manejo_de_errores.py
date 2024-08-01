def suma():
    n1 = int(input("Input the numer one:"))
    n2 = int(input("Input the numer two:"))
    print(n1 + n2)
    print("Thanks for sum")


""" try:
    #Codigo que queremos probar
except:
    #Codigo a ejecutar si no hay un error
else:
    #Codigo a ejecutar si no hay un error.
finally:
    #Codigo que se va a ejecutar de todos modos """
""" 
try:
    suma()
except:
    print("Algo no ha salido bien")
else:
    print("Hicisite todo bien")
finally:
    print("Eso fue todo") """

def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero:"))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste un {numero}")
            break

    print("Gracias")

pedir_numero()