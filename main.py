from clientes import ManejoClientes
from menu import ManejoMenu
from pedido import ManejoPedidos
"""En este modulo se define el menu principal de la aplicacion
Happy Burguer junto con sus 3 submenus correspondientes, se importan las clases:
ManejoClientes, ManejoMenu y ManejoPedidos donde se encuentran todas las operaciones 
para ser efectiva la aplicación
"""
class Menu:
    def __init__(self):
        self.menu()

    def menu(self):
        manejo_clientes = ManejoClientes()
        manejo_menu = ManejoMenu()
        manejo_pedidos = ManejoPedidos()

        salir = False
        print("--------------------------")
        print("Bienvenido a Happy Burguer")
        print("""
            1. Pedidos
            2. Clientes
            3. Menú
            4. Salir
        """)

        while not salir:
            opcion = int(input("Selecciona la opción deseada: "))

            if opcion == 1:
                print("Seleccionaste la opción Pedidos")
                sub_opcion_pedidos = 0
                while sub_opcion_pedidos != 3:
                    print("""
                    1. Crear pedido
                    2. Cancelar pedido
                    3. Volver al menu principal
                    """)

                    sub_opcion_pedidos = int(input("Selecciona una opción relacionada con los pedidos: "))

                    if sub_opcion_pedidos == 1:
                        manejo_pedidos.crear_pedido()
                    elif sub_opcion_pedidos == 2:
                        manejo_pedidos.cancelar_pedido()
                    elif sub_opcion_pedidos == 3:
                        print("Volviendo al menú principal")
                    else:
                        print("Selecciona una opción válida")

            elif opcion == 2:
                print("Seleccionaste la opción Clientes")
                sub_opcion_clientes = 0
                while sub_opcion_clientes != 4:
                    print("""
                    1. Agregar cliente
                    2. Eliminar cliente
                    3. Actualizar cliente
                    4. Volver al menú principal
                    """)

                    sub_opcion_clientes = int(input("Selecciona una opción relacionada con los clientes: "))

                    if sub_opcion_clientes == 1:
                        manejo_clientes.agregar_cliente()
                    elif sub_opcion_clientes == 2:
                        manejo_clientes.eliminar_cliente()
                    elif sub_opcion_clientes == 3:
                        manejo_clientes.actualizar_cliente()
                    elif sub_opcion_clientes == 4:
                        print("Volviendo al menú principal")
                    else:
                        print("Selecciona una opción válida")

            elif opcion == 3:
                print("Seleccionaste la opción Menú")
                sub_opcion_menu = 0
                while sub_opcion_menu != 4:
                    print("""
                    1. Agregar producto al menú
                    2. Eliminar producto del menú
                    3. Actualizar producto del menú
                    4. Volver al menú principal
                    """)

                    sub_opcion_menu = int(input("Selecciona una opción relacionada con el menú: "))

                    if sub_opcion_menu == 1:
                        manejo_menu.agregar_producto()
                    elif sub_opcion_menu == 2:
                        manejo_menu.eliminar_producto()
                    elif sub_opcion_menu == 3:
                        manejo_menu.actualizar_producto()
                    elif sub_opcion_menu == 4:
                        print("Volviendo al menú principal")
                    else:
                        print("Selecciona una opción válida")

            elif opcion == 4:
                print("Seleccionaste Salir")
                break

            else:
                print("Selecciona una opción válida")

menu = Menu()
