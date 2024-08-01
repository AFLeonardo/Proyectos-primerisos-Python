# Descomprimir archivo.
""" import shutil

shutil.unpack_archive('Day 9\Project.zip', 'Prueba') """

import zipfile

zip = zipfile.ZipFile('Day 9\Project.zip', 'r')

zip.extractall()