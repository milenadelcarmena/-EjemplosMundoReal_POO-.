# Clase que representa un producto en la tienda
class Producto:
    def __init__(self, nombre, precio, stock):
        """
        Inicializa un nuevo producto con nombre, precio y cantidad en stock.
        :param nombre: Nombre del producto
        :param precio: Precio del producto
        :param stock: Cantidad disponible en stock
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad):
        """
        Vende una cantidad del producto.
        :param cantidad: Cantidad a vender
        :return: Mensaje sobre la venta
        """
        if cantidad <= self.stock:
            self.stock -= cantidad  # Reduce el stock disponible
            return f"Se han vendido {cantidad} unidades de '{self.nombre}'."
        else:
            return f"No hay suficiente stock para vender {cantidad} unidades de '{self.nombre}'."

    def reabastecer(self, cantidad):
        """
        Reabastece el stock del producto.
        :param cantidad: Cantidad a agregar al stock
        """
        self.stock += cantidad  # Aumenta el stock disponible
        return f"Se han añadido {cantidad} unidades de '{self.nombre}'. Stock actual: {self.stock}"


# Clase que representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre):
        """
        Inicializa un nuevo cliente con su nombre.
        :param nombre: Nombre del cliente
        """
        self.nombre = nombre


# Clase que representa la tienda
class Tienda:
    def __init__(self):
        """Inicializa la tienda con una lista vacía de productos."""
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un nuevo producto a la tienda."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra todos los productos disponibles en la tienda."""
        print("Productos disponibles:")
        for producto in self.productos:
            estado = "Agotado" if producto.stock == 0 else f"Stock: {producto.stock}"
            print(f"'{producto.nombre}' - Precio: ${producto.precio}, {estado}")

    def vender_producto(self, nombre_producto, cantidad):
        """Vende un producto específico."""
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                resultado = producto.vender(cantidad)
                print(resultado)
                return resultado
        print(f"El producto '{nombre_producto}' no se encuentra en la tienda.")


# Ejemplo de uso del sistema de gestión de la tienda
if __name__ == "__main__":
    # Crear instancias de la tienda y productos
    tienda = Tienda()

    # Agregar productos a la tienda
    tienda.agregar_producto(Producto("Camiseta", 20.0, 50))
    tienda.agregar_producto(Producto("Pantalón", 35.0, 30))
    tienda.agregar_producto(Producto("Chaqueta", 60.0, 10))

    # Mostrar productos disponibles en la tienda
    print("Antes de realizar ventas:")
    tienda.mostrar_productos()

    # Crear un cliente y realizar una compra
    cliente1 = Cliente("Carlos Pérez")
    print(f"\nCliente: {cliente1.nombre}")

    # Vender productos al cliente
    tienda.vender_producto("Camiseta", 5)

    # Mostrar productos después de la venta
    print("\nProductos después de la venta:")
    tienda.mostrar_productos()

    # Reabastecer un producto agotado
    for producto in tienda.productos:
        if producto.nombre == "Chaqueta":
            print(producto.reabastecer(5))  # Reabastecer chaquetas

    # Mostrar productos después del reabastecimiento
    print("\nProductos después del reabastecimiento:")
    tienda.mostrar_productos()
