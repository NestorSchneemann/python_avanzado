"""
Ejercicio 3: Tabla de multiplicar avanzada
Mostrar las tablas de multiplicar del 1 al 10 usando ciclos anidados.
"""

for i in range(1, 11):
    print("----------------")
    print("Tabla del", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i*j)