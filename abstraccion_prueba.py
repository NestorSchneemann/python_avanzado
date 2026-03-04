class Carro:
    def encender(self):
        self.revisar_motor()
        print("Carro encendido")

    def __revisar_motor(self):
        print("motor revisado interno")

    def __inyectar_combustible(self):
        print("Combustible")

carro1 = Carro()
carro1.encender()