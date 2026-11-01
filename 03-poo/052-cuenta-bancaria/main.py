"""Proyecto 052: Cuenta bancaria.

Una cuenta bancaria que protege su saldo: solo cambia al depositar o retirar,
y cada operación revisa que la cantidad sea válida.
"""


class CuentaBancaria:
    """Cuenta con titular y saldo protegido."""

    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # Dos guiones bajos al inicio hacen que el atributo sea privado: no
        # se puede usar como cuenta.__saldo desde fuera de la clase. Esto es
        # el encapsulamiento: el objeto protege sus datos y solo deja
        # cambiarlos a través de sus métodos, que revisan cada operación.
        # Si el saldo se pudiera modificar directo, cualquier parte del
        # programa podría dejarlo negativo o inventar dinero.
        self.__saldo = 0
        if saldo_inicial > 0:
            self.__saldo = saldo_inicial

    # Un decorador es una línea que empieza con @ y va justo arriba de un
    # def. Modifica el comportamiento de la función que tiene debajo.
    # @property convierte el método en un atributo de solo lectura: se usa
    # como cuenta.saldo, sin paréntesis, y no se le puede asignar un valor.
    @property
    def saldo(self):
        """Devuelve el saldo actual de la cuenta."""
        return self.__saldo

    def depositar(self, cantidad):
        """Suma la cantidad al saldo. Devuelve True si se pudo."""
        if cantidad <= 0:
            print("El depósito debe ser mayor que cero.")
            return False
        self.__saldo = self.__saldo + cantidad
        print(f"Depositaste ${cantidad:.2f}. Saldo: ${self.__saldo:.2f}")
        return True

    def retirar(self, cantidad):
        """Resta la cantidad si alcanza el saldo. Devuelve True si se pudo."""
        if cantidad <= 0:
            print("El retiro debe ser mayor que cero.")
            return False
        if cantidad > self.__saldo:
            print(f"Saldo insuficiente. Tienes ${self.__saldo:.2f}.")
            return False
        self.__saldo = self.__saldo - cantidad
        print(f"Retiraste ${cantidad:.2f}. Saldo: ${self.__saldo:.2f}")
        return True


def main():
    """Hace varias operaciones y muestra cómo se protege el saldo."""
    cuenta = CuentaBancaria("Ana", 1000)
    print(f"Cuenta de {cuenta.titular} con ${cuenta.saldo:.2f}")
    print()

    cuenta.depositar(500)
    cuenta.retirar(200)
    # Los métodos devuelven True o False, así quien los llama puede saber
    # si la operación se hizo y decidir qué hacer
    se_pudo = cuenta.retirar(5000)
    print(f"¿Se hizo el retiro de $5000? {se_pudo}")
    cuenta.depositar(-50)
    print()

    # Intentar cambiar el saldo a mano provoca un AttributeError, porque
    # saldo es una propiedad sin forma de asignarle valor
    try:
        cuenta.saldo = 1000000
    except AttributeError:
        print("No puedes cambiar cuenta.saldo directamente.")

    # El atributo privado tampoco se puede leer desde fuera de la clase
    try:
        print(cuenta.__saldo)
    except AttributeError:
        print("Tampoco puedes leer cuenta.__saldo desde fuera.")

    print()
    print(f"Saldo final de {cuenta.titular}: ${cuenta.saldo:.2f}")


if __name__ == "__main__":
    main()
