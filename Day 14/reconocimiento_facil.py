import cv2
import face_recognition as fr

# Carga imagenes
foto_control = fr.load_image_file("Day 14\FotoA.jpg")
foto_prueba = fr.load_image_file("Day 14\FotoB.jpg")

foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)