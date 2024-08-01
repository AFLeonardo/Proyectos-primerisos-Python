import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2024/07/por-que-se-utiliza-python-en-ciencia-de.html')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

columna_lateral = sopa.select('p')

for p in columna_lateral:
    print(p.getText())
