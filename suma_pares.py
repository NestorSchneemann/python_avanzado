"""
Ejercicio 9: Suma de valores pares
Dada una lista de números, sumar solo los pares usando ciclos.
"""

lista = [45, 65, 85, 7, 9 ,87, 2, 21, 74, 16, 8, 16, 60]

suma = 0
for i in lista:
    if i%2 == 0:
        suma = suma + i

print(suma)