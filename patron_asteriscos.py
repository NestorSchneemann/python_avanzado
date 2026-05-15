"""
Ejercicio 10: Patrón de asteriscos
Crear un programa que imprima un triángulo de asteriscos usando ciclos anidados.
"""

filas = 10

"""

for i in range(filas):
    espacios = filas - i - 1
    asteriscos = i * 2 + 1
    print(espacios * " ", asteriscos * "*")

"""

for i in range(filas):
    
    for j in range(filas - i - 1):
        print(" ", end="")
    
    for k in range(2 * i + 1):
        print("*", end="")

    print()