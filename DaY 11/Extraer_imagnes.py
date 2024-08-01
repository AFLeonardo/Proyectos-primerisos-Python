import bs4
import requests
import os

# Verificar si la carpeta 'imagenes' existe, de lo contrario, crearla
if not os.path.exists('imagenes'):
    os.makedirs('imagenes')

# Obtener el contenido de la página
url = requests.get('https://mx.ebay.com/')
sopa = bs4.BeautifulSoup(url.text, 'lxml')
imagenes = sopa.select('img')

# Iterar sobre cada imagen encontrada
for img in imagenes:
    # Obtener el atributo src
    src = img.get('src')
    
    # Asegurarse de que el src sea una URL completa
    if src and src.startswith('//'):
        src = 'https:' + src
    elif not src.startswith('http'):
        continue  # Saltar si la URL no es válida
    
    # Realizar la solicitud para obtener la imagen
    imagen_d = requests.get(src)
    
    # Obtener el nombre de archivo de la URL y abrir el archivo en modo binario
    filename = os.path.basename(src)
    filepath = os.path.join('imagenes', filename)
    
    with open(filepath, 'wb') as f:
        f.write(imagen_d.content)

    print(f"Imagen guardada en {filepath}")
