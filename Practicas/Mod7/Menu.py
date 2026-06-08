'''
Created on May, 2026
@author: SaulO
'''

import csv

from Cliente import Cliente
from CuentaDeAhorro import CuentaDeAhorro
from CuentaDeCredito import CuentaDeCredito


class Menu:

    def __init__(self):

        self.mensajeDeBienvenida = (
            "Bienvenido al Sistema Bancario"
        )

        self.cliente = self.cargarCliente()

        self.cargarCuentas()

    def cargarCliente(self):

        with open(
            "data/clientes.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            fila = next(lector)

            return Cliente(
                fila["nombre"],
                fila["direccion"],
                int(fila["edad"])
            )

    def cargarCuentas(self):

        with open(
            "data/cuentas.csv",
            "r",
            encoding="utf-8"
        ) as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                if fila["tipo"] == "Ahorro":

                    cuenta = CuentaDeAhorro(
                        float(fila["cantidad"])
                    )

                else:

                    cuenta = CuentaDeCredito(
                        float(fila["cantidad"]),
                        float(fila["limite"])
                    )

                self.cliente.agregarCuenta(
                    cuenta
                )

    def darBienvenida(self):

        print(self.mensajeDeBienvenida)

    def desplegarMenu(self):

        print("\n===== MENU =====")
        print("1. Mostrar cliente")
        print("2. Salir")

        return int(
            input("Seleccione una opcion: ")
        )

    def procesarOpcion(self, opcion):

        if opcion == 1:

            print()
            print(self.cliente)

        elif opcion == 2:

            print("Fin del sistema.")
