import zipfile

archivo = zipfile.ZipFile('Comprimiendso.zip', 'w')

archivo.write('Day 9\\fecha_hora.py')
archivo.write('Day 9\\os_shiltil.py')

archivo.close()