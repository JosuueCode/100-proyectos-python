"""Proyecto 066: Excepciones personalizadas.

Una cuenta bancaria que avisa de sus errores lanzando excepciones propias
en lugar de devolver False. Quien usa la cuenta decide cómo atenderlas.
"""


# Una excepción propia es una clase que hereda de Exception, la clase base
# de casi todos los errores de Python. Así se puede lanzar y atrapar igual
# que ValueError o TypeError. El docstring basta como cuerpo de la clase:
# no necesita nada más porque hereda todo de Exception.
class ErrorCuenta(Exception):
    """Error base para cualquier problema con una cuenta."""


# Las dos excepciones heredan de ErrorCuenta. Con esta jerarquía se puede
# atrapar un error concreto o, con except ErrorCuenta, cualquiera de ellos.
class MontoInvalidoError(ErrorCuenta):
    """La cantidad de la operación es cero o negativa."""


class SaldoInsuficienteError(ErrorCuenta):
    """El retiro es mayor que el saldo disponible."""

    def __init__(self, saldo, cantidad):
        # super().__init__() guarda el mensaje que se ve al imprimir el
        # error. Los atributos extra dan detalles a quien lo atrape.
        super().__init__(f"Saldo insuficiente: tienes ${saldo:.2f}.")
        self.saldo = saldo
        self.faltante = cantidad - saldo


class CuentaBancaria:
    """Cuenta con titular y saldo protegido."""

    def __init__(self, titular, saldo_inicial):
        if saldo_inicial < 0:
            # raise lanza una excepción: detiene el método en ese punto y
            # el error sube hasta el try que lo atrape. Si nadie lo atrapa,
            # el programa se detiene y muestra el error.
            raise MontoInvalidoError("El saldo inicial no puede ser negativo.")
        self.titular = titular
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        """Devuelve el saldo actual."""
        return self.__saldo

    def depositar(self, cantidad):
        """Suma la cantidad al saldo. Lanza MontoInvalidoError si no vale."""
        if cantidad <= 0:
            raise MontoInvalidoError("El depósito debe ser mayor que cero.")
        self.__saldo = self.__saldo + cantidad

    def retirar(self, cantidad):
        """Resta la cantidad. Lanza una excepción si no se puede."""
        if cantidad <= 0:
            raise MontoInvalidoError("El retiro debe ser mayor que cero.")
        if cantidad > self.__saldo:
            raise SaldoInsuficienteError(self.__saldo, cantidad)
        self.__saldo = self.__saldo - cantidad


def hacer_retiro(cuenta, cantidad):
    """Intenta un retiro y muestra qué pasó."""
    print(f"Retiro de ${cantidad:.2f}:")
    try:
        cuenta.retirar(cantidad)
    except SaldoInsuficienteError as error:
        print(f"  {error}")
        print(f"  Te faltan ${error.faltante:.2f}.")
    except MontoInvalidoError as error:
        print(f"  {error}")
    # else se ejecuta solo si el try terminó sin ninguna excepción
    else:
        print("  Retiro hecho.")
    # finally se ejecuta siempre, haya error o no. Sirve para lo que debe
    # pasar en cualquier caso, como mostrar el saldo o cerrar un archivo.
    finally:
        print(f"  Saldo: ${cuenta.saldo:.2f}")


def main():
    """Hace operaciones válidas e inválidas con una cuenta."""
    cuenta = CuentaBancaria("Ana", 1000)
    print(f"Cuenta de {cuenta.titular} con ${cuenta.saldo:.2f}")
    print()

    hacer_retiro(cuenta, 300)
    hacer_retiro(cuenta, 2000)
    hacer_retiro(cuenta, -50)
    print()

    # Con la excepción base se atrapan todos los errores de la cuenta en un
    # solo except, sin importar cuál fue
    for cantidad in [500, 0]:
        try:
            cuenta.depositar(cantidad)
            print(f"Depositaste ${cantidad:.2f}.")
        except ErrorCuenta as error:
            print(f"No se pudo depositar: {error}")
    print()

    try:
        CuentaBancaria("Luis", -100)
    except MontoInvalidoError as error:
        print(f"No se creó la cuenta de Luis: {error}")


if __name__ == "__main__":
    main()
