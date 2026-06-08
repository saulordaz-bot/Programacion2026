
'''
Created on March, 2026
@author: SaulO
'''

from datetime import datetime

class Inversion:

    def __init__(self, capital, tasa):

        if capital <= 0:
            raise ValueError("El capital debe ser mayor que cero.")

        if tasa <= 0:
            raise ValueError("La tasa debe ser mayor que cero.")

        self.__capital = capital
        self.__tasa = tasa
        self.__fecha = datetime.now()

    # GETTERS
    def getCapital(self):
        return self.__capital

    def getTasa(self):
        return self.__tasa

    def getFecha(self):
        return self.__fecha

    # SETTERS
    def setCapital(self, capital):
        if capital > 0:
            self.__capital = capital

    def setTasa(self, tasa):
        if tasa > 0:
            self.__tasa = tasa

    def calcularGanancia(self):
        return self.__capital * (self.__tasa / 100)

    def montoFinal(self):
        return self.__capital + self.calcularGanancia()

    def __str__(self):
        return (
            f"Fecha: {self.__fecha.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Capital: {self.__capital}\n"
            f"Tasa: {self.__tasa}%\n"
            f"Ganancia: {self.calcularGanancia():.2f}\n"
            f"Monto final: {self.montoFinal():.2f}")
