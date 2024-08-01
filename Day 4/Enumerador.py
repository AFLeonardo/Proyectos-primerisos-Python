# Practica 1
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

# Practica 2
lista = list("Python")
print(lista)

# Practica 3
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for i,n in enumerate(lista_nombres):
    if n[0] == "M":
        print(i)
    else:
        pass