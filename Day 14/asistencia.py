import cv2
import face_recognition as fr
import os
import numpy as np
from datetime import datetime

# Creamos base de datos
ruta = 'Day 14\\Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}\\{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imagnes
def codificar(imagenes):
    # Crear lista nueva
    lista_codificada = []

    # Pasar img a RGB
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # Codificar
        codificado = fr.face_encodings(imagen)[0]

        # Agregamos a la lista
        lista_codificada.append(codificado)

    # Devolver lista 
    return lista_codificada

lista_empleados_codificada = codificar(mis_imagenes)

# Registrar los ingresos
def registrar_ingresos(persona):
    f = open('Day 14\\registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')
    f.close()

# Tomar una imagen de cámara
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Leer imagen de cámara
exito, imagen = captura.read()

if not exito:
    print("No se pudo tomar la imagen")
else:
    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancia = fr.face_distance(lista_empleados_codificada, caracodif)
        print(distancia)
        indice_coincidencia = np.argmin(distancia)

        if distancia[indice_coincidencia] < 0.6:
            nombre = nombres_empleados[indice_coincidencia]
            print(nombre)

            # Mostrar el nombre de la persona
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registrar_ingresos(nombre)

            # Mostrar imagen obtenida
            cv2.imshow("Imagen", imagen)

            # Mantener ventana abierta
            cv2.waitKey(0)
        else:
            print("No coincide")

captura.release()
cv2.destroyAllWindows()
