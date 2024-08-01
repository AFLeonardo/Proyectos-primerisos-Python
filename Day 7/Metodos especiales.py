class CD:
    def __init__(self, autor, titulo, canciones) -> None:
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self) -> str:
        return f"Album: {self.titulo} de {self.autor}"
    
    #DEFINO COMO QUIERO QUE FUNCIONE LA FUNCION LEN CUANDO LA MANDE A LLAMAR
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print(f"Se ha eliminado {self.titulo}")

mi_cd = CD('Elton Jonh','I am Still Standing',4)
del mi_cd
