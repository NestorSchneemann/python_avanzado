# Crear la clase
class perro:
    # Creacion de los atributos de la clase
    def __init__(self, edad, raza, velocidad):
        self.edad = edad
        self.raza = raza
        self.velocidad = velocidad

    # Creación de las acciones de la clase
    def ladrar(self):
        if self.raza == "pincher":
            print("guararararararararaarararara")
        else:
            print("woof!")

    def correr(self):
        if self.edad > 15:
            print("Este perro ya no corre")
        else:
            self.velocidad += 1
            print("Tu", self.raza, "va a", self.velocidad, "metros por segundo")

    def frenar(self):
        if self.velocidad > 0:
            self.velocidad -= 1
        print("Tu", self.raza, "va a", self.velocidad, "metros por segundo")


# Instanciar
zeus = perro(16, "french poodle", 0)
monita = perro(7, "pitbull", 0)
satanas = perro(10, "pincher", 0)

# Ejecutar los métodos
zeus.ladrar()
satanas.ladrar()

monita.correr()
monita.correr()
monita.frenar()
monita.frenar()
monita.frenar()
