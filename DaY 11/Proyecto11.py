import bs4
import requests

# URL base sin número de página
url = 'http://books.toscrape.com/catalogue/category/books_1/page-{}.html'

# Lista para almacenar títulos con rating alto
Titulos = []

# Iterar sobre las páginas
for pagina in range(1, 51):
    try:
        # Hacer solicitud HTTP
        resultado = requests.get(url.format(pagina))
        resultado.raise_for_status()  # Verificar que la solicitud sea exitosa
    except requests.RequestException as e:
        print(f"Error al acceder a la página {pagina}: {e}")
        continue

    # Crear sopa de BeautifulSoup
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de libros
    libros = sopa.select('.product_pod')

    for libro in libros:
        # Verificar si el libro tiene una calificación de 4 o 5 estrellas
        rating = libro.select_one('.star-rating')['class']
        if 'Four' in rating or 'Five' in rating:
            # Extraer y guardar el título del libro
            Titulo_libro = libro.h3.a['title']
            Titulos.append(Titulo_libro)

# Imprimir títulos de libros con 4 o 5 estrellas
for titulo in Titulos:
    print(titulo)
