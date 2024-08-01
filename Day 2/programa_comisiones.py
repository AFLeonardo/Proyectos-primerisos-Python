nombre = input("Hola, como deseas que te llame: ")
producto_vendido = int(input("{}, Cual es la cantidad de ventas que obtuviste ?\n".format(nombre)))
dinero_generado = (producto_vendido * 13 / 100)

print(f"Exelente {nombre}. \nEste mes has generado ${round(dinero_generado,2)}")