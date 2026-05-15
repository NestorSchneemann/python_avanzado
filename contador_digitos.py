"""
Ejercicio 4: Contador de dígitos
Solicitar un número y contar cuántos dígitos tiene utilizando un ciclo while.
"""

numero = int(input("Digita un número: "))

division = 1
divisor = 1
digitos = 0

while division > 0:
    division = numero // divisor
    divisor *= 10
    digitos += 1

print("tu número tiene", digitos - 1, "dígitos")