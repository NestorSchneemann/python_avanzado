# Clase padre
class Carro:
    def __init__(self, marca):
        self.marca = marca


    def conducir(self):
        print("El carro está conduciendo")

# Clases hijas
class CarroElectrico(Carro):

    def cargar_bateria(self):
        print("Cargando batería")

    def mover(self):
        print("usa electricidad")

        
class CarroGasolinero(Carro):

    def mover(self):
        print("usa gasolina")


carro1 = CarroElectrico("Tesla")
carro1.conducir()
carro1.cargar_bateria()
carro1.mover()

carro2 = CarroGasolinero("Lincoln")
carro2.conducir()
carro2.mover()