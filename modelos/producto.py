"""
Módulo: producto.py

Este módulo contiene la clase Producto, la cual representa
un producto dentro del sistema de gestión de inventario.

La clase incluye:
- Encapsulamiento de atributos
- Métodos getters y setters
- Validaciones básicas
- Conversión a diccionario para almacenamiento en JSON
- Reconstrucción desde diccionario
"""


class Producto:
    """
    Clase que representa un producto del inventario.

    Atributos:
        __id (int): Identificador único del producto.
        __nombre (str): Nombre del producto.
        __cantidad (int): Cantidad disponible en inventario.
        __precio (float): Precio unitario del producto.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        Parámetros:
            id_producto (int): ID único del producto.
            nombre (str): Nombre del producto.
            cantidad (int): Cantidad disponible.
            precio (float): Precio del producto.
        """
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # ==============================
    # MÉTODOS GETTERS
    # ==============================

    def get_id(self):
        """Devuelve el ID del producto."""
        return self.__id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self.__nombre

    def get_cantidad(self):
        """Devuelve la cantidad disponible."""
        return self.__cantidad

    def get_precio(self):
        """Devuelve el precio del producto."""
        return self.__precio

    # ==============================
    # MÉTODOS SETTERS
    # ==============================

    def set_nombre(self, nombre):
        """Modifica el nombre del producto."""
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        """
        Modifica la cantidad del producto.
        No permite cantidades negativas.
        """
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print("Error: La cantidad no puede ser negativa.")

    def set_precio(self, precio):
        """
        Modifica el precio del producto.
        No permite precios negativos.
        """
        if precio >= 0:
            self.__precio = precio
        else:
            print("Error: El precio no puede ser negativo.")

    # ==============================
    # MÉTODOS PARA ARCHIVOS
    # ==============================

    def to_dict(self):
        """
        Convierte el objeto Producto en un diccionario.
        Esto permite guardar la información en un archivo JSON.
        """
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }

    @staticmethod
    def from_dict(data):
        """
        Crea un objeto Producto a partir de un diccionario.
        Se utiliza al cargar los datos desde un archivo JSON.
        """
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    # ==============================
    # MÉTODO ESPECIAL
    # ==============================

    def __str__(self):
        """
        Devuelve una representación en texto del producto.
        Se utiliza al imprimir el objeto en consola.
        """
        return f"ID: {self.__id} | Nombre: {self.__nombre} | Cantidad: {self.__cantidad} | Precio: ${self.__precio}"