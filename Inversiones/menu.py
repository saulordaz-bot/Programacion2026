'''
Created on March, 2026
@author: SaulO

'''

from inversion import Inversion
from usuario import Usuario


class Menu:

    def iniciar(self):

        nombre = input("Ingresa tu nombre: ")
        usuario = Usuario(nombre)

        cantidad = int(input("¿Cuántas inversiones deseas registrar? "))

        for i in range(cantidad):
            print(f"\n---- Inversión {i+1} ----")
            capital = float(input("Capital: "))
            tasa = float(input("Tasa (%): "))

            inversion = Inversion(capital, tasa)
            usuario.agregarInversion(inversion)

        print("\n")
        print(usuario)

        print("\n--- Lista de Inversiones ---")
        usuario.mostrarInversiones()

        print("\n--- Mejor Inversión ---")
        usuario.compararInversiones()
