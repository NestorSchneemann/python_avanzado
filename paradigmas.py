# PARADIGMA IMPERATIVO
# Aquí damos instrucciones paso paso

placas = []
placas.append("ABC123")
placas.append("XYZ999")

print("Vehículos acutales: ", placas)

placas.remove("ABC123")

print("Después de salida", placas)


# PARADIGMA FUNCIONAL
# Usamos funciones para organizar el código

def registrar_entrada(lista, placa):
    # Agrega un vehículo a partir de su placa a la lista
    lista.append(placa)

def registrar_salida(lista, placa):
    # Elimina un vehículo si existe
    if placa in lista:
        lista.remove(placa)


vehiculos = []

registrar_entrada(vehiculos, "ABC123")
registrar_entrada(vehiculos, "XYZ213")

print(vehiculos)

registrar_salida(vehiculos, "ABC123")

print(vehiculos)