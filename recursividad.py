# Contar hacia atrás

def contar(numero):

    # caso base
    if numero == 0:
        print("final")
        return
    
    # mostrar
    print(numero)

    # llamada recursividad
    contar(numero-1)

contar(7)