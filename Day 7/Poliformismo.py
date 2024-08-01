class Vaca:

    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuuu")


class Oveja:
    
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    
    def hablar(self):
        print(self.nombre + " dice beee")

vaca1 =  Vaca('Panzas')
oveja1 = Oveja('Lupatia')

vaca1.hablar()
oveja1.hablar()

# AMBAS TIENEN EL MISMO METODO PERO ACTUAN DE FORMA DISTINTA.

""" animales = [vaca1, oveja1]

for animal in animales:
    animal.hablar()
 """

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)