from Producto import Producto

class GestorInventario:
    def __init__(self) -> None:
        self.productos: dict[str, Producto] = {}

    def buscar_producto(self,nombre: str) -> bool:
        return nombre in self.productos

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

    def actualizar_stock(self,nombre:str,cantidad: int) -> str:
        if not self.buscar_producto(nombre):
            return "NO_EXISTE"
        product = self.productos.get(nombre)
        exito = product.actualizar_stock(cantidad)
        if exito:
            return "OK"
        else:
            return "INVALIDO"

    def actualizar_precio(self,nombre: str, precio: float) -> str:
       if not self.buscar_producto(nombre):
            return "NO_EXISTE"
       product = self.productos.get(nombre)
       exito = product.actualizar_precio(precio)
       if exito:
           return "OK"
       else:
           return "INVALIDO"

    def eliminar_producto(self,nombre: str) -> str :
        if not self.buscar_producto(nombre):
            return "NO_EXISTE"
        del self.productos[nombre]
        return "OK"

    def reporte_bajo_stock(self) -> None:
        if len(self.productos) == 0:
            print("Inventario Vacio")
            return
        for producto in self.productos.values():
            if producto.cantidad <= 5:
                print(producto)