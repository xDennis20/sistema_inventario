class Producto:
    def __init__(self,nombre: str,precio: float,cantidad: int) -> None:
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_stock(self,cantidad: int) -> bool:
        nuevo_total = self.cantidad + cantidad
        if nuevo_total < 0:
            return False
        self.cantidad = nuevo_total
        return True

    def __str__(self) -> str:
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.cantidad}"