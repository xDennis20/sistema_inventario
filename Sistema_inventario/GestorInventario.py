from Producto import Producto
class GestorInventario:
    def __init__(self) -> None:
        self.productos: dict[str, Producto] = {}

    def agregar_producto(self,nombre: str, precio: float, cantidad: int) -> bool:
        if nombre in self.productos:
            return False
        nuevo_producto = Producto(nombre,precio,cantidad)
        self.productos[nombre] = nuevo_producto
        return True

    def ver_inventario(self) -> None:
        if len(self.productos) == 0:
            print("Inventario Vacio")
        for producto in self.productos.values():
            print(producto)

tienda = GestorInventario()
tienda.agregar_producto("Manzanas",3.34,5)
tienda.agregar_producto("Peras",3.64,8)
tienda.ver_inventario()