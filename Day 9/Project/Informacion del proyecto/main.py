import re
import os
import pathlib
import time
import datetime
from Format import Tiket

pattern = r'N\D{3}-\d{5}'
Nums_serie = {}

# Recorriendo el arbol de carpetas
ruta = 'Day 9\\Project\\Informacion del proyecto\\Mi_Gran_Directorio'
tiempo_i = time.time()

for carpeta, subcarpeta, archivo in os.walk(ruta):
    for arch in archivo:
        
        ruta = pathlib.Path(carpeta, arch) # Crea la ruta del archivo txt
        info = open(ruta)  # Muestra el texto que tiene el archivo txt.

        texto = info.read()

        existe_patron = re.search(pattern, texto) # Hay que buscar la coincidencia con el patron
        
        if existe_patron != None:
            Nums_serie[arch] = existe_patron.group()

tiempo_f = time.time()

Tiempo = tiempo_f - tiempo_i

Tiket(Nums_serie, Tiempo)
        


# Ver como es que funciona xq no tengo ni puta idea.