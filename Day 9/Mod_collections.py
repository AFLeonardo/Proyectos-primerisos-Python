""" from collections import Counter

frase = 'Hola brou esto es un ejemplo'

print(Counter(frase.split())) """

# This do error because the key don't exits in the dictionary. So we can fix uses a defaultdict
# mi_dict = {'one': 'green', 'two': 'blue', 'three': 'red'}
# print(mi_dict['four'])

# Uses defaultdict
""" from collections import defaultdict

dict = defaultdict(lambda : 'Not found.')\
# Add a value
dict['Five'] = 'Brown'

print(dict['Six']) """

from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
Ariel = Persona('Ariel', 1.76, 50)

print(Ariel.altura, ' ', Ariel.peso )

