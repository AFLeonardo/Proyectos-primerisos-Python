import os
from pathlib import Path
ruta = os.chdir("D:\\alfonso\\Escritorio\\a")
archivo = open('Alterno.txt')
print(archivo.read())


#USANDO PATH

Carpeta = Path('/alfonso/Escritorio/a')
archivo = Carpeta / 'Alterno.txt'

arc = open(archivo)
print(arc.read())