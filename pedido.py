import sqlite3
import os
"""
        Inicializa una instancia de la clase Pedido con los datos proporcionados.

        Argumentos:
            codigo_pedido (int): El código del pedido.
            codigo_cliente (str): El código del cliente que realiza el pedido.
            codigo_producto (str): El código del producto solicitado.
            cantidad (int): La cantidad del producto solicitada.
        """
#Clase Pedido que maneja las operaciones relaciondas con los pedidos
class Pedido:
    def __init__(self, codigo_pedido, codigo_cliente, codigo_producto, cantidad):
        self.codigo_pedido = codigo_pedido
        self.codigo_cliente = codigo_cliente
        self.codigo_producto = codigo_producto
        self.cantidad = cantidad
#Se crea la clase ManejoPedidos para las operaciones relacionadas con el manejo y operacion de los clientes
class ManejoPedidos:
    def __init__(self):
        self.pedidos = []
        self.db = Database('mi_base_de_datos.db')
        self.db.crear_tabla_pedidos()

    def crear_pedido(self):
        codigo_pedido = int(input("Ingrese el código del pedido: "))
        codigo_cliente = str(input("Ingrese el código del cliente: "))
        codigo_producto = str(input("Ingrese el código del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))

        pedido = Pedido(codigo_pedido, codigo_cliente, codigo_producto, cantidad)
        self.db.crear_pedido(codigo_pedido, codigo_cliente, codigo_producto, cantidad)
        print("Pedido creado correctamente.")
        
        # Generar el contenido del ticket
        ticket_content = f"""TICKET DE PEDIDO
    --------------------
    Código del pedido: {codigo_pedido}
    Código del cliente: {codigo_cliente}
    Código del producto: {codigo_producto}
    Cantidad: {cantidad}
    --------------------
    ¡Gracias por su pedido!

    """

        # Ruta y nombre del archivo del ticket
        ticket_path = f"tickets/pedido_{codigo_pedido}.txt"

        # Guardar el ticket en un archivo de texto
        with open(ticket_path, "a") as file:
            file.write(ticket_content)

        print("Pedido creado correctamente.")

    def cancelar_pedido(self):
        codigo_pedido = input("Ingrese el código del pedido que desea cancelar: ")
        self.db.cancelar_pedido(codigo_pedido)
        print("Pedido cancelado correctamente.")
#Se crea la base de datos para la manipulacion de los datos de los pedidos
class Database:
    def __init__(self, nombre_archivo):
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def crear_tabla_pedidos(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS pedidos (codigo_pedido TEXT, codigo_cliente TEXT, codigo_producto TEXT, cantidad INTEGER)")
        self.conexion.commit()

    def crear_pedido(self, codigo_pedido, codigo_cliente, codigo_producto, cantidad):
        consulta = "INSERT INTO pedidos VALUES (?, ?, ?, ?)"
        datos = (codigo_pedido, codigo_cliente, codigo_producto, cantidad)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def cancelar_pedido(self, codigo_pedido):
        consulta = "DELETE FROM pedidos WHERE codigo_pedido = ?"
        datos = (codigo_pedido,)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()
    
    def consultar_pedido(self, codigo_pedido):
        consulta = "SELECT * FROM pedidos WHERE codigo_pedido = ?"
        datos = (codigo_pedido,)
        self.cursor.execute(consulta, datos)
        pedido = self.cursor.fetchone()

        if pedido:
            datos_pedido = {
                'codigo_pedido': pedido[0],
                'codigo_cliente': pedido[1],
                'codigo_producto': pedido[2],
                'cantidad': pedido[3]
            }
            return datos_pedido
        else:
            return None

    def cerrar_conexion(self):
        self.conexion.close()