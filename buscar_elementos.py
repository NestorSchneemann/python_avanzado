"""
Ejercicio 8: Buscar elemento
Dada una lista, buscar un número específico y mostrar su posición. Usar break cuando se encuentre.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

buscado = int(input("Ingresa un número de 1 dígito para buscar: "))

pos = 0
for num in lista:
    if num == buscado:
        break
    else:
        pos += 1


print("el número buscado se encuentra en la posición", pos)