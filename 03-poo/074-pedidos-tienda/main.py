"""Proyecto 074: Tienda en línea con pedidos.

Una tienda con inventario, clientes y pedidos. Cada pedido descuenta
existencias, calcula el IVA y avanza por sus estados hasta entregarse.
"""

from dataclasses import dataclass
from enum import Enum

IVA = 0.16


class ErrorTienda(Exception):
    """Error base de la tienda."""


class ProductoNoEncontradoError(ErrorTienda):
    """No hay ningún producto con ese código."""


class StockInsuficienteError(ErrorTienda):
    """Se pidieron más piezas de las que hay en existencia."""

    # Las anotaciones de tipo (type hints) indican qué tipo de dato espera
    # cada parámetro: nombre: str significa "nombre debería ser un texto".
    # Documentan el código y ayudan al editor a detectar errores, pero
    # Python no las obliga: si pasas un número donde dice str, el programa
    # se ejecuta igual.
    def __init__(self, nombre: str, pedida: int, disponible: int):
        mensaje = f"Pediste {pedida} de {nombre} y solo hay {disponible}."
        super().__init__(mensaje)
        self.pedida = pedida
        self.disponible = disponible


class EstadoInvalidoError(ErrorTienda):
    """El pedido no puede hacer esa acción en su estado actual."""


class EstadoPedido(Enum):
    """Estados por los que pasa un pedido."""

    PENDIENTE = "pendiente"
    PAGADO = "pagado"
    ENVIADO = "enviado"
    ENTREGADO = "entregado"
    CANCELADO = "cancelado"


@dataclass
class Cliente:
    """Cliente de la tienda."""

    nombre: str
    correo: str


@dataclass
class Producto:
    """Producto del catálogo con código, nombre y precio sin IVA."""

    codigo: str
    nombre: str
    precio: float


@dataclass
class Renglon:
    """Un producto dentro de un pedido con su cantidad."""

    producto: Producto
    cantidad: int

    # -> float indica el tipo del valor que devuelve el método
    def importe(self) -> float:
        """Devuelve el precio por la cantidad."""
        return self.producto.precio * self.cantidad


class Inventario:
    """Guarda los productos y cuántas piezas hay de cada uno."""

    def __init__(self):
        # dict[str, Producto] dice que las llaves son textos y los valores
        # objetos Producto; list[Renglon], que es una lista de renglones
        self.productos: dict[str, Producto] = {}
        self.existencias: dict[str, int] = {}

    def agregar(self, producto: Producto, cantidad: int):
        """Da de alta un producto con sus existencias."""
        if cantidad < 0:
            raise ValueError("Las existencias no pueden ser negativas.")
        self.productos[producto.codigo] = producto
        self.existencias[producto.codigo] = cantidad

    def buscar(self, codigo: str) -> Producto:
        """Devuelve el producto. Lanza ProductoNoEncontradoError si no hay."""
        if codigo not in self.productos:
            raise ProductoNoEncontradoError(f"No existe el código {codigo}.")
        return self.productos[codigo]

    def retirar(self, codigo: str, cantidad: int):
        """Descuenta piezas. Lanza StockInsuficienteError si no alcanzan."""
        producto = self.buscar(codigo)
        disponible = self.existencias[codigo]
        if cantidad > disponible:
            raise StockInsuficienteError(producto.nombre, cantidad, disponible)
        self.existencias[codigo] = disponible - cantidad

    def devolver(self, codigo: str, cantidad: int):
        """Regresa piezas al inventario, por ejemplo al cancelar."""
        self.existencias[codigo] = self.existencias[codigo] + cantidad


class Pedido:
    """Pedido de un cliente con sus renglones y su estado."""

    total_pedidos = 0

    def __init__(self, cliente: Cliente):
        Pedido.total_pedidos = Pedido.total_pedidos + 1
        self.numero: int = Pedido.total_pedidos
        self.cliente = cliente
        self.renglones: list[Renglon] = []
        self.estado = EstadoPedido.PENDIENTE

    def revisar_estado(self, esperado: EstadoPedido, accion: str):
        """Lanza EstadoInvalidoError si el pedido no está en el estado."""
        if self.estado != esperado:
            actual = self.estado.value
            mensaje = f"El pedido {self.numero} está {actual}"
            raise EstadoInvalidoError(f"{mensaje}, no se puede {accion}.")

    def agregar(self, producto: Producto, cantidad: int):
        """Agrega un renglón. Solo se puede mientras está pendiente."""
        self.revisar_estado(EstadoPedido.PENDIENTE, "modificar")
        self.renglones.append(Renglon(producto, cantidad))

    def subtotal(self) -> float:
        """Devuelve la suma de los importes sin IVA."""
        suma = 0
        for renglon in self.renglones:
            suma = suma + renglon.importe()
        return suma

    def iva(self) -> float:
        """Devuelve el IVA del subtotal."""
        return self.subtotal() * IVA

    def total(self) -> float:
        """Devuelve el subtotal más el IVA."""
        return self.subtotal() + self.iva()

    def mostrar(self):
        """Muestra el detalle del pedido en columnas."""
        estado = self.estado.value
        print(f"Pedido {self.numero} de {self.cliente.nombre} ({estado})")
        for renglon in self.renglones:
            nombre = renglon.producto.nombre
            descripcion = f"{renglon.cantidad} x {nombre}"
            print(f"  {descripcion:<30} ${renglon.importe():>10.2f}")
        print(f"  {'Subtotal':<30} ${self.subtotal():>10.2f}")
        print(f"  {'IVA 16 %':<30} ${self.iva():>10.2f}")
        print(f"  {'Total':<30} ${self.total():>10.2f}")


class Tienda:
    """Tienda que conecta el inventario con los pedidos."""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.inventario = Inventario()
        self.pedidos: list[Pedido] = []

    def crear_pedido(self, cliente: Cliente) -> Pedido:
        """Abre un pedido nuevo para el cliente."""
        pedido = Pedido(cliente)
        self.pedidos.append(pedido)
        return pedido

    def agregar_al_pedido(self, pedido: Pedido, codigo: str, cantidad: int):
        """Aparta las piezas del inventario y las agrega al pedido."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        pedido.revisar_estado(EstadoPedido.PENDIENTE, "modificar")
        # Primero se descuenta del inventario: si no alcanza, la excepción
        # sale aquí y el pedido no cambia
        self.inventario.retirar(codigo, cantidad)
        pedido.agregar(self.inventario.buscar(codigo), cantidad)
        print(f"Pedido {pedido.numero}: {cantidad} x {codigo} agregado.")

    def pagar(self, pedido: Pedido):
        """Marca como pagado un pedido pendiente con productos."""
        pedido.revisar_estado(EstadoPedido.PENDIENTE, "pagar")
        if len(pedido.renglones) == 0:
            raise EstadoInvalidoError("No se puede pagar un pedido vacío.")
        pedido.estado = EstadoPedido.PAGADO
        print(f"Pedido {pedido.numero} pagado: ${pedido.total():.2f}")

    def enviar(self, pedido: Pedido):
        """Marca como enviado un pedido pagado."""
        pedido.revisar_estado(EstadoPedido.PAGADO, "enviar")
        pedido.estado = EstadoPedido.ENVIADO
        print(f"Pedido {pedido.numero} enviado a {pedido.cliente.correo}.")

    def entregar(self, pedido: Pedido):
        """Marca como entregado un pedido enviado."""
        pedido.revisar_estado(EstadoPedido.ENVIADO, "entregar")
        pedido.estado = EstadoPedido.ENTREGADO
        print(f"Pedido {pedido.numero} entregado.")

    def cancelar(self, pedido: Pedido):
        """Cancela un pedido pendiente y regresa las piezas al inventario."""
        pedido.revisar_estado(EstadoPedido.PENDIENTE, "cancelar")
        for renglon in pedido.renglones:
            codigo = renglon.producto.codigo
            self.inventario.devolver(codigo, renglon.cantidad)
        pedido.estado = EstadoPedido.CANCELADO
        print(f"Pedido {pedido.numero} cancelado.")

    def mostrar_existencias(self):
        """Muestra cuántas piezas quedan de cada producto."""
        print("Existencias:")
        for codigo, producto in self.inventario.productos.items():
            cantidad = self.inventario.existencias[codigo]
            print(f"  {codigo} {producto.nombre:<22} {cantidad:>3}")


def intentar(accion):
    """Ejecuta una acción de la tienda y muestra el error si lo hay."""
    try:
        accion()
    except ErrorTienda as error:
        print(f"Error: {error}")
    except ValueError as error:
        print(f"Error: {error}")


def main():
    """Simula varios pedidos con errores incluidos."""
    tienda = Tienda("TecnoMarket")
    tienda.inventario.agregar(Producto("A1", "Audífonos inalámbricos", 899), 5)
    tienda.inventario.agregar(Producto("T2", "Teclado mecánico", 1250), 2)
    tienda.inventario.agregar(Producto("M3", "Mouse ergonómico", 450), 10)

    ana = Cliente("Ana", "ana@correo.com")
    luis = Cliente("Luis", "luis@correo.com")

    # Una lambda sin parámetros guarda la llamada completa para que
    # intentar() la ejecute dentro de su try
    pedido_ana = tienda.crear_pedido(ana)
    intentar(lambda: tienda.agregar_al_pedido(pedido_ana, "A1", 2))
    intentar(lambda: tienda.agregar_al_pedido(pedido_ana, "T2", 1))
    intentar(lambda: tienda.pagar(pedido_ana))
    intentar(lambda: tienda.enviar(pedido_ana))
    intentar(lambda: tienda.agregar_al_pedido(pedido_ana, "M3", 1))
    print()

    pedido_luis = tienda.crear_pedido(luis)
    intentar(lambda: tienda.agregar_al_pedido(pedido_luis, "T2", 3))
    intentar(lambda: tienda.agregar_al_pedido(pedido_luis, "X9", 1))
    intentar(lambda: tienda.agregar_al_pedido(pedido_luis, "M3", 4))
    intentar(lambda: tienda.agregar_al_pedido(pedido_luis, "M3", 0))
    intentar(lambda: tienda.entregar(pedido_luis))
    intentar(lambda: tienda.cancelar(pedido_luis))
    print()

    pedido_ana.mostrar()
    print()
    tienda.mostrar_existencias()


if __name__ == "__main__":
    main()
