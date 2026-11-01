"""Proyecto 061: Carrito de compras.

Un carrito que guarda productos con su cantidad, permite agregar y quitar,
aplica un descuento y muestra un ticket con las columnas alineadas.
"""

DESCUENTO_MAXIMO = 50


class Producto:
    """Producto de la tienda con nombre y precio unitario."""

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Renglon:
    """Un renglón del carrito: un producto y cuántas piezas lleva."""

    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        """Devuelve el precio del producto por la cantidad."""
        return self.producto.precio * self.cantidad


class Carrito:
    """Carrito de compras formado por renglones."""

    def __init__(self):
        # La composición es cuando un objeto está formado por otros objetos
        # que guarda en sus atributos. El carrito no hereda de Renglon: lo
        # contiene. Él crea sus renglones, los cuida y, si el carrito deja
        # de existir, sus renglones también. La relación se lee "tiene un",
        # a diferencia de la herencia, que se lee "es un".
        self.renglones = {}
        self.descuento = 0

    def agregar(self, producto, cantidad):
        """Agrega piezas de un producto. Devuelve True si se pudo."""
        if cantidad <= 0:
            print(f"La cantidad de {producto.nombre} debe ser mayor que 0.")
            return False

        # Si el producto ya está en el carrito, solo crece su cantidad
        if producto.nombre in self.renglones:
            renglon = self.renglones[producto.nombre]
            renglon.cantidad = renglon.cantidad + cantidad
        else:
            self.renglones[producto.nombre] = Renglon(producto, cantidad)
        print(f"Agregaste {cantidad} x {producto.nombre}.")
        return True

    def quitar(self, nombre, cantidad):
        """Quita piezas de un producto. Devuelve True si se pudo."""
        if nombre not in self.renglones:
            print(f"{nombre} no está en el carrito.")
            return False

        renglon = self.renglones[nombre]
        if cantidad >= renglon.cantidad:
            del self.renglones[nombre]
            print(f"Quitaste {nombre} del carrito.")
        else:
            renglon.cantidad = renglon.cantidad - cantidad
            print(f"Quitaste {cantidad} x {nombre}.")
        return True

    def subtotal(self):
        """Devuelve la suma de los subtotales de todos los renglones."""
        suma = 0
        for renglon in self.renglones.values():
            suma = suma + renglon.subtotal()
        return suma

    def aplicar_descuento(self, porcentaje):
        """Guarda el descuento si es válido. Devuelve True si se aplicó."""
        if porcentaje < 0 or porcentaje > DESCUENTO_MAXIMO:
            print(f"El descuento debe estar entre 0 y {DESCUENTO_MAXIMO} %.")
            return False
        self.descuento = porcentaje
        print(f"Se aplicó un descuento del {porcentaje} %.")
        return True

    def total(self):
        """Devuelve el subtotal menos el descuento."""
        rebaja = self.subtotal() * self.descuento / 100
        return self.subtotal() - rebaja

    def mostrar_ticket(self):
        """Muestra cada renglón y los totales en columnas alineadas."""
        # El ancho fijo, como en el proyecto 058, reserva siempre el mismo
        # espacio: :<20 para el nombre a la izquierda y :>10.2f para los
        # importes a la derecha, así las columnas quedan derechas
        print(f"{'Producto':<20} {'Cant':>4} {'Precio':>10} {'Importe':>10}")
        for renglon in self.renglones.values():
            nombre = renglon.producto.nombre
            cantidad = renglon.cantidad
            precio = renglon.producto.precio
            importe = renglon.subtotal()
            producto = f"{nombre:<20} {cantidad:>4}"
            print(f"{producto} {precio:>10.2f} {importe:>10.2f}")
        rebaja = self.subtotal() - self.total()
        print(f"{'Subtotal':<36} {self.subtotal():>10.2f}")
        print(f"{'Descuento':<36} {rebaja:>10.2f}")
        print(f"{'Total':<36} {self.total():>10.2f}")


def main():
    """Llena un carrito, lo modifica y muestra el ticket."""
    leche = Producto("Leche", 28.50)
    pan = Producto("Pan de caja", 45)
    huevo = Producto("Huevo (12 piezas)", 52)
    cafe = Producto("Café molido", 98.90)

    carrito = Carrito()
    carrito.agregar(leche, 2)
    carrito.agregar(pan, 1)
    carrito.agregar(huevo, 1)
    carrito.agregar(cafe, 1)
    carrito.agregar(leche, 1)
    carrito.agregar(pan, 0)
    print()

    carrito.quitar("Café molido", 1)
    carrito.quitar("Tortillas", 1)
    carrito.aplicar_descuento(80)
    carrito.aplicar_descuento(10)
    print()

    carrito.mostrar_ticket()


if __name__ == "__main__":
    main()
