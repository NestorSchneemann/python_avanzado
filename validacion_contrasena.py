"""
Ejercicio 5: Validación con intentos
Crear un programa que permita máximo 3 intentos para ingresar una contraseña correcta. Usar break.
"""

password = "laclave"

i = 3
while i > 0:
    valor_ingresado = input("Digite su contraseña: ")
    if valor_ingresado == password:
        i = 0
        print("Acceso permitido")
    else:
        i -= 1
        if i == 0:
            print("Demasiados intentos fallidos. Su acceso será restringido por 2 horas")
        else:
            print("Contraseña incorrecta. Intente de nuevo")