'''
Created on March, 2026
@author: SaulO

'''

from inversion import Inversion
from usuario import Usuario


class Menu:

    def iniciar(self):

        nombre = input("Ingresa tu nombre: ")

        print("---- Inversión 1 ----")
        capital1 = float(input("Capital: "))
        tasa1 = float(input("Tasa (%): "))

        print("---- Inversión 2 ----")
        capital2 = float(input("Capital: "))
        tasa2 = float(input("Tasa (%): "))

        usuario = Usuario(nombre)
        inv1 = Inversion(capital1, tasa1)
        inv2 = Inversion(capital2, tasa2)

        print("\n")
        print(usuario)

        print("\n--- Inversión 1 ---")
        print(inv1)

        print("\n--- Inversión 2 ---")
        print(inv2)

        print("\n--- Comparación ---")
        print(inv1.compararInversion(inv2))
