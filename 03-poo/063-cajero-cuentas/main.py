"""Proyecto 063: Cajero con varias cuentas.

Un cajero automático con varias cuentas guardadas por número. Pide el PIN
con un máximo de tres intentos y deja consultar, depositar, retirar y
transferir dinero entre cuentas.
"""

MAX_INTENTOS = 3


class Cuenta:
    """Cuenta bancaria con número, titular, PIN y saldo protegidos."""

    def __init__(self, numero, titular, pin, saldo_inicial):
        self.numero = numero
        self.titular = titular
        # El PIN y el saldo son privados, como el saldo del proyecto 052:
        # nadie los lee ni los cambia sin pasar por los métodos
        self.__pin = pin
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        """Devuelve el saldo actual."""
        return self.__saldo

    def verificar_pin(self, pin):
        """Devuelve True si el PIN es correcto, sin revelar el PIN real."""
        return pin == self.__pin

    def depositar(self, cantidad):
        """Suma la cantidad al saldo."""
        self.__saldo = self.__saldo + cantidad

    def retirar(self, cantidad):
        """Resta la cantidad si alcanza el saldo. Devuelve True si se pudo."""
        if cantidad > self.__saldo:
            return False
        self.__saldo = self.__saldo - cantidad
        return True


class Cajero:
    """Cajero que guarda las cuentas en un diccionario por número."""

    def __init__(self):
        # La llave es el número de cuenta y el valor es el objeto Cuenta,
        # así se encuentra cualquier cuenta sin recorrerlas todas
        self.cuentas = {}

    def agregar_cuenta(self, cuenta):
        """Registra una cuenta en el cajero."""
        self.cuentas[cuenta.numero] = cuenta

    def iniciar_sesion(self):
        """Pide número y PIN. Devuelve el número, o "" si no entra."""
        numero = input("Número de cuenta: ").strip()
        if numero not in self.cuentas:
            print("Esa cuenta no existe.")
            return ""

        cuenta = self.cuentas[numero]
        for intento in range(1, MAX_INTENTOS + 1):
            pin = input("PIN: ").strip()
            if cuenta.verificar_pin(pin):
                print(f"Hola, {cuenta.titular}.")
                return numero
            restantes = MAX_INTENTOS - intento
            if restantes == 1:
                print("PIN incorrecto. Te queda 1 intento.")
            elif restantes > 1:
                print(f"PIN incorrecto. Te quedan {restantes} intentos.")

        print("PIN incorrecto. Superaste los intentos y se retuvo la tarjeta.")
        return ""

    def transferir(self, origen, numero_destino, cantidad):
        """Pasa dinero de una cuenta a otra. Devuelve True si se hizo."""
        if numero_destino not in self.cuentas:
            print("La cuenta de destino no existe.")
            return False
        if numero_destino == origen.numero:
            print("No puedes transferir a tu propia cuenta.")
            return False
        if not origen.retirar(cantidad):
            print(f"Saldo insuficiente. Tienes ${origen.saldo:.2f}.")
            return False

        destino = self.cuentas[numero_destino]
        destino.depositar(cantidad)
        print(f"Transferiste ${cantidad:.2f} a {destino.titular}.")
        return True


def pedir_cantidad(mensaje):
    """Pide una cantidad mayor que cero hasta que sea válida."""
    while True:
        # float() lanza un ValueError si el texto no es un número, como en
        # el proyecto 047; el except lo atrapa y se vuelve a preguntar
        try:
            cantidad = float(input(mensaje))
            if cantidad > 0:
                return cantidad
            print("La cantidad debe ser mayor que cero.")
        except ValueError:
            print("Escribe solo números.")


def pedir_opcion():
    """Muestra el menú y devuelve la opción elegida como entero."""
    print()
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Transferir")
    print("5. Salir")
    while True:
        try:
            return int(input("Elige una opción: "))
        except ValueError:
            print("Escribe el número de la opción.")


def atender(cajero, cuenta):
    """Repite el menú hasta que el usuario elige salir."""
    while True:
        opcion = pedir_opcion()
        if opcion == 1:
            print(f"Tu saldo es ${cuenta.saldo:.2f}.")
        elif opcion == 2:
            cantidad = pedir_cantidad("Cantidad a depositar: ")
            cuenta.depositar(cantidad)
            print(f"Depositaste ${cantidad:.2f}.")
        elif opcion == 3:
            cantidad = pedir_cantidad("Cantidad a retirar: ")
            if cuenta.retirar(cantidad):
                print(f"Retiraste ${cantidad:.2f}.")
            else:
                print(f"Saldo insuficiente. Tienes ${cuenta.saldo:.2f}.")
        elif opcion == 4:
            destino = input("Cuenta de destino: ").strip()
            cantidad = pedir_cantidad("Cantidad a transferir: ")
            cajero.transferir(cuenta, destino, cantidad)
        elif opcion == 5:
            print(f"Hasta luego, {cuenta.titular}.")
            return
        else:
            print("Esa opción no existe.")


def main():
    """Crea el cajero con sus cuentas y atiende a un usuario."""
    cajero = Cajero()
    cajero.agregar_cuenta(Cuenta("1001", "Ana", "1234", 5000))
    cajero.agregar_cuenta(Cuenta("1002", "Luis", "4321", 1200))
    cajero.agregar_cuenta(Cuenta("1003", "Sofía", "0000", 800))

    print("Cajero automático")
    numero = cajero.iniciar_sesion()
    if numero != "":
        atender(cajero, cajero.cuentas[numero])


if __name__ == "__main__":
    main()
