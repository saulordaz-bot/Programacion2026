'''
Created on March, 2026
@author: SaulO
'''

from inversion import Inversion
from usuario import Usuario
import os

class Menu:

    def leerEntero(self, mensaje):

        while True:
            try:
                numero = int(input(mensaje))

                if numero <= 0:
                    print("Debe ser mayor que cero.")
                else:
                    return numero

            except ValueError:
                print("Error: ingresa un número entero válido.")

    def leerFloatPositivo(self, mensaje):

        while True:
            try:
                numero = float(input(mensaje))

                if numero <= 0:
                    print("Debe ser mayor que cero.")
                else:
                    return numero

            except ValueError:
                print("Error: ingresa un número válido.")

    def iniciar(self):

        print("===== SISTEMA DE INVERSIONES =====")

        usuario = None

        if os.path.exists("usuario.dat"):

            opcion = input(
                "Existe un usuario guardado. "
                "¿Deseas cargarlo? (s/n): "
            ).lower()

            if opcion == "s":
                try:
                    usuario = Usuario.cargar()
                    print("\nUsuario cargado correctamente.")
                    print(usuario)

                except Exception as error:
                    print("Error al cargar archivo:", error)

        if usuario is None:

            nombre = input("Ingresa tu nombre: ")
            usuario = Usuario(nombre)

            cantidad = self.leerEntero(
                "¿Cuántas inversiones deseas registrar? "
            )

            for i in range(cantidad):

                print(f"\n---- Inversión {i+1} ----")

                capital = self.leerFloatPositivo("Capital: ")
                tasa = self.leerFloatPositivo("Tasa (%): ")

                try:
                    inversion = Inversion(capital, tasa)
                    usuario.agregarInversion(inversion)

                except ValueError as error:
                    print(error)

            try:
                usuario.guardar()
                print("\nDatos guardados correctamente.")

            except Exception as error:
                print("Error al guardar:", error)

        print("\n")
        print(usuario)

        print("\n--- Lista de Inversiones ---")
        usuario.mostrarInversiones()

        print("\n--- Mejor Inversión ---")
        usuario.compararInversiones()
