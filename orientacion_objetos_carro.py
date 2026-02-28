class carro:
    def __init__(self, marca, modelo, combustible, velocidad):
        self.combustible = combustible
        self.velocidad = velocidad
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        if self.combustible > 0:
            self.velocidad += 10
            if self.modelo < 2000:
                self.combustible -= self.velocidad/100
            else:
                self.combustible -= self.velocidad/150
            print("El", self.marca, "va a", self.velocidad, "km/h")
            print("Te quedan", max(self.combustible, 0), "litros de combustible")
        else:
            print("Te quedaste sin combustible")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -=10
        print("El", self.marca, "va a", self.velocidad, "km/h")

# Instanciar
carro1 = carro("Kia", 2015, 10, 0)
carro2 = carro("Volkswagen", 1997, 2, 40)

carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.acelerar()
carro2.frenar()
carro2.frenar()