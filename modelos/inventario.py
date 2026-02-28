"""
Módulo: inventario.py

Este módulo contiene la clase Inventario.
Se encarga de gestionar todos los productos utilizando
un diccionario para optimizar la búsqueda por ID.

También implementa almacenamiento persistente
usando archivos JSON.
"""

import json
from modelos.producto import Producto


class Inventario:
    """
    Clase que gestiona los productos del inventario.

    Utiliza un diccionario donde:
        - La clave es el ID del producto.
        - El valor es un objeto Producto.
    """

    def __init__(self):
        """
        Constructor de la clase Inventario.
        Inicializa el diccionario de productos.
        """
        self.productos = {}  # Diccionario para almacenamiento rápido

    # ==========================================
    # MÉTODOS DE GESTIÓN DE PRODUCTOS
    # ==========================================

    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al inventario.
        No permite IDs repetidos.
        """
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario por su ID.
        """
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza la cantidad o el precio de un producto.
        """
        if id_producto in self.productos:
            producto = self.productos[id_producto]

            if cantidad is not None:
                producto.set_cantidad(cantidad)

            if precio is not None:
                producto.set_precio(precio)

            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por nombre.
        Devuelve una lista de coincidencias.
        """
        resultados = []

        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)

        return resultados

    def mostrar_todos(self):
        """
        Muestra todos los productos del inventario.
        """
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    # ==========================================
    # MÉTODOS DE ARCHIVO (JSON)
    # ==========================================

    def guardar_en_archivo(self, nombre_archivo="inventario.json"):
        """
        Guarda todos los productos en un archivo JSON.
        """
        datos = []

        for producto in self.productos.values():
            datos.append(producto.to_dict())

        with open(nombre_archivo, "w") as archivo:
            json.dump(datos, archivo, indent=4)

        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="inventario.json"):
        """
        Carga los productos desde un archivo JSON.
        """
        try:
            with open(nombre_archivo, "r") as archivo:
                datos = json.load(archivo)

            for item in datos:
                producto = Producto.from_dict(item)
                self.productos[producto.get_id()] = producto

            print("Inventario cargado correctamente.")

        except FileNotFoundError:
            print("No existe archivo previo. Se creará uno nuevo al guardar.")