class cuenta:
    def __init__(self, numero_cuenta, propietario, saldo):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.saldo = saldo

    
    def deposito(self):
        monto_depositado = int(input("Digite el monto a depositar: "))
        self.saldo += monto_depositado
        print("Deposito realizado por", monto_depositado)
        print("Nuevo saldo en tu cuenta", self.numero_cuenta, ":", self.saldo)

    def retiro(self):
        monto_retirado = int(input("Cuanto deseas retirar? "))
        if monto_retirado > self.saldo * 1.004:
            print("No cuentas con los fondos suficientes para esta transacción")
            print("Saldo actual de tu cuenta", self.saldo)
        else:
            self.saldo -= monto_retirado
            print("Retiro realizado por", monto_retirado)
            print("Nuevo saldo en tu cuenta", self.numero_cuenta, ":", self.saldo)

    def transferencia(self):
        destino = input("Indique el número de la cuenta destino: ")
        monto_transferido = int(input("Digite el monto a transferir: "))
        if monto_transferido > self.saldo * 1.004:
            print("No cuentas con los fondos suficientes para esta transacción")
            print("Saldo actual de tu cuenta", self.saldo)
        else:
            self.saldo -= monto_transferido
            print("Transferencia realizada por", monto_transferido, "a la cuenta", destino)
            print("Nuevo saldo en tu cuenta", self.numero_cuenta, ":", self.saldo)

# Instancias
cuenta1 = cuenta("936046711", "Patricio Star", 3500000)

cuenta1.deposito()
cuenta1.retiro()
cuenta1.transferencia()
cuenta1.transferencia()
