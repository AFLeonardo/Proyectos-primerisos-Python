import os

print(os.walk(os.getcwd()))

ruta = os.getcwd()

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f'En carpeta {carpeta}')
    print(f'Las subcarpetas son : ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        print(f'\t{arch}')