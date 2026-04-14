'''
Created on March, 2026
@author: SaulO

'''

'''
Clase Inversion
Se encarga de los cálculos de una inversión
'''

class Inversion:

    def __init__(self, capital, tasa):
        self.__capital = capital   # privado
        self.__tasa = tasa         # privado

    # GETTERS
    def getCapital(self):
        return self.__capital

    def getTasa(self):
        return self.__tasa

    # SETTERS
    def setCapital(self, capital):
        self.__capital = capital

    def setTasa(self, tasa):
        self.__tasa = tasa

    def calcularGanancia(self):
        return self.__capital * (self.__tasa / 100)

    def montoFinal(self):
        return self.__capital + self.calcularGanancia()

    def __str__(self):
        return (f"Capital: {self.__capital}\n"
                f"Tasa: {self.__tasa}%\n"
                f"Ganancia: {self.calcularGanancia()}\n"
                f"Monto final: {self.montoFinal()}")
                f"Tasa: {self.tasa}%\n"
                f"Ganancia: {self.calcularGanancia()}\n"
                f"Monto final: {self.montoFinal()}")
