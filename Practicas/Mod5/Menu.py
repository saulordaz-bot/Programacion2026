'''
Created on april, 2026
@author: SaulO
'''

from Cliente import Cliente
from CuentaDeAhorro import CuentaDeAhorro
from CuentaDeCredito import CuentaDeCredito


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

            print("\n1. Cuenta de Ahorro")
            print("2. Cuenta de Credito")

            tipo = int(
                input("Tipo de cuenta: ")
            )

            cantidad = float(
                input("Cantidad inicial: ")
            )

            if tipo == 1:

                cuenta = CuentaDeAhorro(
                    cantidad
                )

            elif tipo == 2:

                limite = float(
                    input("Limite de credito: ")
                )

                cuenta = CuentaDeCredito(
                    cantidad,
                    limite
                )

            else:

                print("Tipo invalido.")
                return

            self.cliente.agregarCuenta(
                cuenta
            )

            print("Cuenta agregada.")

        elif opcion == 2:

            print()
            print(self.cliente)

        elif opcion == 3:

            print("Fin del sistema.")
