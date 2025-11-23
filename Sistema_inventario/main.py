inventario = {}

def agregar_producto():
    producto = input("Ingrese el nombre del producto: ").strip().capitalize()
    precio = 0
    cantidad = 0
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

def main():
    salir = False
    opcion = 0
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
        match opcion:
            case 1:
                agregar_producto()
            case 2:
                ver_inventario()
            case 7:
                print("Saliendo del Sistema")
                salir = True
            case _:
                print("Opcion no valida. Escoja de las opciones correcta")
if __name__ == '__main__':
    main()