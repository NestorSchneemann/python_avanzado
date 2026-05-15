"""
Ejercicio 1: Números primos
Mostrar todos los números primos entre 1 y 100 usando ciclos.
"""

for i in range (1, 101):
    if i > 1:
        for j in range (2, i):
            if (i % j) == 0:
                break
        else:
            print(i)