import sqlite3
"""
        Inicializa una instancia de la clase Producto.

        Argumentos:
            clave (str): La clave del producto.
            nombre (str): El nombre del producto.
            precio (float): El precio del producto.
        """
class Producto:
    def __init__(self, clave, nombre, precio):
        self.clave = clave
        self.nombre = nombre
        self.precio = precio
#Crea una lista de productos y establece una conexión con la base de datos.
class ManejoMenu:
    def __init__(self):
        self.productos = []
        self.db = Database('mi_base_de_datos.db')
        self.db.crear_tabla_menu()

    def agregar_producto(self):
        clave = str(input("Ingrese la clave del producto: "))
        nombre = str(input("Ingrese el nombre del producto: "))
        precio = float(input("Ingrese el precio del producto: "))

        producto = Producto(clave, nombre, precio)
        self.productos.append(producto)
        self.db.agregar_producto(clave, nombre, precio)
        print("Producto agregado correctamente.")

    def eliminar_producto(self):
        clave = str(input("Ingrese la clave del producto que desea eliminar: "))
        self.db.eliminar_producto(clave)
        print("producto eliminado correctamente.")


    def actualizar_producto(self):
        clave = str(input("Ingrese la clave del producto que desea actualizar: "))
        nuevo_nombre = str(input("Ingrese el nuevo nombre del producto: "))            
        nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))

        for producto in self.productos:
            if producto.clave == clave:
                producto.nombre = nuevo_nombre
                producto.precio = nuevo_precio
                self.db.actualizar_producto(clave, nuevo_nombre, nuevo_precio)
                print("Producto actualizado correctamente.")
                return

    print("No se encontró ningún producto con esa clave.")
#Inicializa una instancia de la clase Database para las operaciones: agregar producto, eliminar producto
# y actualizar producto
class Database:
    def __init__(self, nombre_archivo):
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def crear_tabla_menu(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS menu (clave TEXT, nombre TEXT, precio REAL)")
        self.conexion.commit()

    def agregar_producto(self, clave, nombre, precio):
        consulta = "INSERT INTO menu VALUES (?, ?, ?)"
        datos = (clave, nombre, precio)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def eliminar_producto(self, clave):
        consulta = "DELETE FROM menu WHERE clave = ?"
        datos = (clave,)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def actualizar_producto(self, clave, nuevo_nombre, nuevo_precio):
        consulta = "UPDATE menu SET nombre = ?, precio = ? WHERE clave = ?"
        datos = (nuevo_nombre, nuevo_precio, clave)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()
