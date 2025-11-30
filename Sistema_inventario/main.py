from GestorInventario import GestorInventario

def main():
    gestor_inventario = GestorInventario()
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
                nombre = input("Ingrese el nombre del producto").strip().lower().capitalize()
                try:
                    precio = float(input("Ingrese el precio del producto: "))
                    cantidad = int(input("Ingrese la cantidad del producto: "))
                    exito = gestor_inventario.agregar_producto(nombre,precio,cantidad)
                    if exito:
                        print("✅ Producto Agregado Correctamente")
                    else:
                        print("❌ Error: El producto ya existe en el inventario")
                except ValueError:
                    print("Error: Ingrese valores numericos")
            case 2:
                gestor_inventario.ver_inventario()
            case 3:
                nombre = input("Ingresar el nombre del producto").strip().lower().capitalize()
                try:
                    cantidad = int(input("Ingrese el stock nuevo del producto"))
                    resultado = gestor_inventario.actualizar_stock(nombre,cantidad)
                    match resultado:
                        case "OK":
                            print(f"El stock se actualizo correctamente")
                        case "NO_EXISTE":
                            print(f"El producto no existe en el inventario")
                        case "INVALIDO":
                            print(f"Cantidad Invalida")
                except ValueError:
                    print("Error: Ingrese valor numerico entero")
            case 4:
                nombre = input("Ingrese el nombre del producto ").strip().lower().capitalize()
                try:
                    precio = float(input(f"Ingrese el nuevo precio del producto {nombre}: "))
                    resultado = gestor_inventario.actualizar_precio(nombre,precio)
                    match resultado:
                        case "OK":
                            print(f"El precio se actualizo correctamente")
                        case "NO_EXISTE":
                            print(f"El producto no existe en el inventario")
                        case "INVALIDO":
                            print(f"Precio Invalido")
                except ValueError:
                    print("Error: Ingrese un valor numerico")
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Saliendo del Sistema")
                salir = True
            case _:
                print("Opcion no valida. Escoja de las opciones correcta")

if __name__ == '__main__':
    main()