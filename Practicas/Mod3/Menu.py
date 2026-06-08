'''
Created on March,2026
@author: SaulO
'''

from Cuenta import Cuenta
from Cliente import Cliente

class Menu:

    def __init__(self):

        self.mensajeDeBienvenida = (
            "Bienvenido al Sistema Bancario"
        )

        cuenta = Cuenta(5000, "D")

        self.cliente = Cliente(
            "Maria Hernandez",
            "Av. Juarez 123",
            25,
            cuenta
        )

    def darBienvenida(self):

        print(self.mensajeDeBienvenida)

    def desplegarMenu(self):

        print("\n===== MENU =====")
        print("1. Mostrar cliente")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Salir")

        return int(
            input("Seleccione una opcion: ")
        )

    def procesarOpcion(self, opcion):

        if opcion == 1:

            print()
            print(self.cliente)

        elif opcion == 2:

            monto = float(
                input("Monto a depositar: ")
            )

            resultado = (
                self.cliente.cuenta.depositar(
                    monto
                )
            )

            if resultado:
                print("Deposito realizado.")
            else:
                print("Monto invalido.")

        elif opcion == 3:

            monto = float(
                input("Monto a retirar: ")
            )

            resultado = (
                self.cliente.cuenta.retirar(
                    monto
                )
            )

            if resultado:
                print("Retiro realizado.")
            else:
                print(
                    "Saldo insuficiente o monto invalido."
                )

        elif opcion == 4:

            print("Fin del sistema.")
