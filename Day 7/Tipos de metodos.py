class Pajaro():
	
		
    @classmethod
    def poner_huevo(cls, cantidad):
        print(f"Puso {cantidad} heuvos.")

    @staticmethod
    def mirar():
        print("El pajaro mirar.")
        
Mi_pajaro = Pajaro()

Mi_pajaro.poner_huevo(5)
Mi_pajaro.mirar()

