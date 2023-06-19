import sqlite3
"""
        Se crea instancia de la clase Cliente con los datos proporcionados.

        Argumentos:
            clave (str): La clave del cliente.
            nombre (str): El nombre del cliente.
            direccion (str): La dirección del cliente.
            correo_electronico (str): El correo electrónico del cliente.
            telefono (str): El teléfono del cliente.
        """
class Cliente:

    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono
#Se crea la clase Manejo Clientes para las operaciones relacionadas con los clientes
class ManejoClientes:
    def __init__(self):
        self.clientes = []
        self.db = Database('mi_base_de_datos.db')
        self.db.crear_tabla_clientes()

    def agregar_cliente(self):
        clave = str(input("Ingrese la clave del cliente: "))
        nombre = str(input("Ingrese el nombre del cliente: "))
        direccion = str(input("Ingrese la dirección del cliente: "))
        correo_electronico = str(input("Ingrese el correo electrónico del cliente: "))
        telefono = str(input("Ingrese el teléfono del cliente: "))

        cliente = Cliente(clave, nombre, direccion, correo_electronico, telefono)
        self.db.agregar_cliente(clave, nombre, direccion, correo_electronico, telefono)
        print("Cliente agregado correctamente.")
        
    def eliminar_cliente(self):
        clave = input("Ingrese la clave del cliente que desea eliminar: ")
        self.db.eliminar_cliente(clave)
        print("Cliente eliminado correctamente.")



    def actualizar_cliente(self):
        clave = input("Ingrese la clave del cliente que desea actualizar: ")

        nuevo_nombre = input("Ingrese el nuevo nombre del cliente (dejar en blanco si no desea actualizar): ")
        nueva_direccion = input("Ingrese la nueva dirección del cliente (dejar en blanco si no desea actualizar): ")
        nuevo_correo = input("Ingrese el nuevo correo electrónico del cliente (dejar en blanco si no desea actualizar): ")
        nuevo_telefono = input("Ingrese el nuevo teléfono del cliente (dejar en blanco si no desea actualizar): ")

        cliente_actualizado = {}
        if nuevo_nombre:
            cliente_actualizado["nombre"] = nuevo_nombre
        if nueva_direccion:
            cliente_actualizado["direccion"] = nueva_direccion
        if nuevo_correo:
            cliente_actualizado["correo_electronico"] = nuevo_correo
        if nuevo_telefono:
            cliente_actualizado["telefono"] = nuevo_telefono

        if cliente_actualizado:
            self.db.actualizar_cliente(clave, cliente_actualizado)
            print("Cliente actualizado correctamente.")
        else:
            print("No se realizaron cambios en el cliente.")
#Se crea la base de datos para la manipulacion de los datos de los clientes
class Database:
    def __init__(self, nombre_archivo):
        self.conexion = sqlite3.connect(nombre_archivo)
        self.cursor = self.conexion.cursor()

    def crear_tabla_clientes(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS clientes (clave TEXT, nombre TEXT, direccion TEXT, correo_electronico TEXT, telefono TEXT)")
        self.conexion.commit()

    def agregar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        consulta = "INSERT INTO clientes VALUES (?, ?, ?, ?, ?)"
        datos = (clave, nombre, direccion, correo_electronico, telefono)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def eliminar_cliente(self, clave):
        consulta = "DELETE FROM clientes WHERE clave = ?"
        datos = (clave,)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()

    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        # Construir la consulta SQL dinámicamente
        sql = "UPDATE clientes SET"
        parametros = []

        if nombre:
            sql += " nombre = ?,"
            parametros.append(nombre)
        if direccion:
            sql += " direccion = ?,"
            parametros.append(direccion)
        if correo_electronico:
            sql += " correo_electronico = ?,"
            parametros.append(correo_electronico)
        if telefono:
            sql += " telefono = ?,"
            parametros.append(telefono)

    
        sql = sql.rstrip(',')

        
        sql += " WHERE clave = ?"
        parametros.append(clave)

    
        self.cursor.execute(sql, parametros)
        self.conexion.commit()

    def cerrar_conexion(self):
        self.conexion.close()