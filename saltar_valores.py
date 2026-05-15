"""
Ejercicio 6: Saltar valores
Imprimir los números del 1 al 50, pero saltar los múltiplos de 5 usando continue.
"""

for i in range(50):
    if i%5 == 0:
        continue
    else:
        print(i)