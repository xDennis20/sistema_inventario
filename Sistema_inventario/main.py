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
                pass
            case 7:
                print("Saliendo del Sistema")
                salir = True
            case _:
                print("Opcion no valida. Escoja de las opciones correcta")
