'''
Created on March, 2026
@author: SaulO
'''

import pickle

class Usuario:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__inversiones = []

    def getNombre(self):
        return self.__nombre

    def agregarInversion(self, inversion):
        self.__inversiones.append(inversion)

    def mostrarInversiones(self):

        if not self.__inversiones:
            print("No hay inversiones registradas.")
            return

        for i, inv in enumerate(self.__inversiones, start=1):
            print(f"\n--- Inversión {i} ---")
            print(inv)

    def compararInversiones(self):

        if len(self.__inversiones) < 2:
            print("Se necesitan al menos 2 inversiones para comparar.")
            return

        mejor = max(self.__inversiones, key=lambda inv: inv.montoFinal())

        print("\nLa mejor inversión es:")
        print(mejor)

    def guardar(self):

        with open("usuario.dat", "wb") as archivo:
            pickle.dump(self, archivo)

    @staticmethod
    def cargar():

        with open("usuario.dat", "rb") as archivo:
            return pickle.load(archivo)

    def __str__(self):
        return (f"Usuario: {self.__nombre}\n"
                f"Inversiones registradas: {len(self.__inversiones)}")
