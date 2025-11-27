inventario = {}

def agregar_producto():
    producto = input("Ingrese el nombre del producto: ").strip().capitalize()
    if producto in inventario:
        print("Este producto ya se encuentra en el inventario.")
        return
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio < 0:
            print("Error: No se permiten numeros negativos")
            return
        cantidad = int(input("Ingrese la cantidad a ingresar del producto: "))
        if cantidad < 0:
            print("Error: No se permiten numeros negativos")
            return
        inventario[producto] = {"precio": precio, "cantidad": cantidad}
        print(f"Producto '{producto}' Guardado con exito.")
    except ValueError:
        print("Error: Tipo de datos invalidos. (Ingrese valores numericos)")

def ver_inventario():
    print("---- Inventario ----")
    if len(inventario) == 0:
        print("No hay productos en el inventario")
        return
    for nombre,detalles in inventario.items():
        print(f"- {nombre} | ${detalles.get("precio")} | Stock: {detalles.get("cantidad")} | Valor total: {detalles.get("cantidad") * detalles.get("precio")}")
    return

def actualizar_stock():
    producto = input("Ingrese el producto que quiere actualizar el stock: ").strip().capitalize()
    if producto in inventario:
        stock = inventario.get(producto)
        print(f"Stock actual de {producto}: {stock.get("cantidad")}")
        cantidad_actual = stock.get("cantidad")
        try:
            stock_nuevo = int(input("Ingrese la cantidad a ingresar del stock entrante: "))
            while stock_nuevo + cantidad_actual < 0:
                print("Error: Ingrese de nuevo una cantidad adecuada")
                stock_nuevo = int(input("Ingrese la cantidad a ingresar del stock entrante: "))
            stock["cantidad"] += stock_nuevo
            print(f"Stock actualizado correctamente, Stock actual: {stock.get("cantidad")}")
            return
        except ValueError:
            print("Error: Tipo de dato incorrecto (Ingrese un valor numerico entero)")
    else:
        print("Producto no encontrado en el inventario")
        return

def eliminar_producto():
    producto = input("Ingrese el producto que quiere eliminar del inventario: ").strip().capitalize()
    confirmadores = {"si","y","yes"}
    if not producto in inventario:
        print("Error: Producto no encontrado en el inventario")
        return
    confirmador = input(f"¿Esta seguro que quiere eliminar el producto [{producto}] (si/no)?").lower().strip()
    if confirmador in confirmadores:
        del inventario[producto]
        print(f"El producto '{producto}' se elimino del inventario")
    else:
        print("Operacion cancelada")
        return

def actualizar_precio():
    producto = input("Ingrese el producto que quiere actualizar el precio: ").strip().capitalize()
    if not producto in inventario:
        print("Producto no encontrado en el inventario")
        return
    detalles = inventario.get(producto)
    precio_actual = detalles.get("precio")
    print(f"Precio actual ${precio_actual} del producto '{producto}'")
    try:
        precio_nuevo = float(input(f"Ingrese el nuevo precio del producto '{producto}'"))
        while precio_nuevo < 0:
            print("Precio invalido, coloque un valor positivo")
            precio_nuevo = float(input(f"Ingrese el nuevo precio del producto '{producto}'"))
        detalles["precio"] = precio_nuevo
        print(f"Precio actualizado del producto '{producto}', Precio actual: {precio_nuevo}")
    except ValueError:
        print("Error: Tipo de dato invalido, Ingrese un valor numerico")
    return

def stock_bajo():
    print("Productos Con Bajo Stock")
    if len(inventario) == 0:
        print("---- Inventario vacio ----")
        return
    for nombre,detalles in inventario.items():
        stock_actual = detalles.get("cantidad")
        if stock_actual <= 5:
            print(f"- {nombre} | ${detalles.get("precio")} | Stock: {stock_actual} | Valor total: {stock_actual * detalles.get("precio")}\n")
    return
def main():
    salir = False
    while not salir:
        print(f"""----- Sistema Inventario -----
        1. Agregar Producto Nuevo
        2. Ver Inventario Completo
        3. Actualizar Stock
        4. Actualizar Precio
        5. Reporte de Bajo Stock
        6. Eliminar Producto
        7. Salir""")
        try:
            opcion = int(input("Escoja una opcion (1-7): "))
        except ValueError:
            print("Error: Coloque un valor entero")
            continue
        match opcion:
            case 1:
                agregar_producto()
            case 2:
                ver_inventario()
            case 3:
                actualizar_stock()
            case 4:
                actualizar_precio()
            case 5:
                stock_bajo()
            case 6:
                eliminar_producto()
            case 7:
                print("Saliendo del Sistema")
                salir = True
            case _:
                print("Opcion no valida. Escoja de las opciones correcta")

if __name__ == '__main__':
    main()