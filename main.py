"""
Archivo: main.py

Este archivo contiene el menú interactivo del sistema
de gestión de inventario.

Se encarga de:
- Mostrar opciones al usuario
- Recibir datos por consola
- Llamar a los métodos de la clase Inventario
- Guardar y cargar datos desde archivo
"""

from modelos.producto import Producto
from modelos.inventario import Inventario


def mostrar_menu():
    """
    Muestra las opciones disponibles del sistema.
    """
    print("\n===== SISTEMA DE GESTIÓN DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Salir")


def main():
    """
    Función principal del programa.
    Controla el flujo del menú interactivo.
    """

    inventario = Inventario()

    # Intentar cargar datos existentes
    inventario.cargar_desde_archivo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        # ==============================
        # OPCIÓN 1: Agregar producto
        # ==============================
        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID: "))
                nombre = input("Ingrese nombre: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("Error: Datos inválidos. Intente nuevamente.")

        # ==============================
        # OPCIÓN 2: Eliminar producto
        # ==============================
        elif opcion == "2":
            try:
                id_producto = int(input("Ingrese ID del producto a eliminar: "))
                inventario.eliminar_producto(id_producto)
            except ValueError:
                print("Error: ID inválido.")

        # ==============================
        # OPCIÓN 3: Actualizar producto
        # ==============================
        elif opcion == "3":
            try:
                id_producto = int(input("Ingrese ID del producto a actualizar: "))

                nueva_cantidad = input("Nueva cantidad (Enter para omitir): ")
                nuevo_precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(nueva_cantidad) if nueva_cantidad else None
                precio = float(nuevo_precio) if nuevo_precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            except ValueError:
                print("Error: Datos inválidos.")

        # ==============================
        # OPCIÓN 4: Buscar por nombre
        # ==============================
        elif opcion == "4":
            nombre = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)

            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos.")

        # ==============================
        # OPCIÓN 5: Mostrar todos
        # ==============================
        elif opcion == "5":
            inventario.mostrar_todos()

        # ==============================
        # OPCIÓN 6: Guardar inventario
        # ==============================
        elif opcion == "6":
            inventario.guardar_en_archivo()

        # ==============================
        # OPCIÓN 7: Salir
        # ==============================
        elif opcion == "7":
            inventario.guardar_en_archivo()
            print("Inventario guardado. Saliendo del sistema...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    main()