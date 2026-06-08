'''
Created on March, 2026
@author: SaulO
'''

from Cuenta import Cuenta
from Cliente import Cliente


class Menu:

    def __init__(self):

        self.mensajeDeBienvenida = (
            "Bienvenido al Sistema Bancario"
        )

        self.cliente = Cliente(
            "Maria Hernandez",
            "Av. Juarez 123",
            25
        )

    def darBienvenida(self):

        print(self.mensajeDeBienvenida)

    def desplegarMenu(self):

        print("\n===== MENU =====")
        print("1. Agregar cuenta")
        print("2. Mostrar cliente")
        print("3. Salir")

        return int(
            input("Seleccione una opcion: ")
        )

    def procesarOpcion(self, opcion):

        if opcion == 1:

            cantidad = float(
                input("Cantidad inicial: ")
            )

            tipo = input(
                "Tipo (D/C): "
            )

            cuenta = Cuenta(
                cantidad,
                tipo
            )

            self.cliente.agregarCuenta(
                cuenta
            )

            print("Cuenta agregada.")

        elif opcion == 2:

            print()
            print(self.cliente)

        elif opcion == 3:

            print("Fin del sistema.")
