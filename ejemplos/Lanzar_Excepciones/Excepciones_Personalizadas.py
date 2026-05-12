class SaldoInsuficienteError(Exception):

    def __init__(self, saldo, cantidad):

        self.saldo = saldo
        self.cantidad = cantidad
        self.deficit = cantidad - saldo

        mensaje = (
            f"No hay suficiente saldo. "
            f"Saldo:{saldo}, "
            f"Cantidad solicitada:{cantidad}"
        )

        super().__init__(mensaje)

class Cuenta:

    def __init__(self, saldo):
        self.saldo = saldo

def retirar(cuenta, cantidad):

    if cantidad > cuenta.saldo:
        raise SaldoInsuficienteError(cuenta.saldo, cantidad)

    cuenta.saldo -= cantidad

    return cuenta.saldo

cuenta = Cuenta(100)

try:
    retirar(cuenta, 500)

except SaldoInsuficienteError as e:
    print(f"Error:{e}")