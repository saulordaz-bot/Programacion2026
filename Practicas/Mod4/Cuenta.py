'''
Created on March, 2026
@author: SauulO
'''

class Cuenta:

    def __init__(self, ctd, t):

        self.__cantidad = ctd
        self.__tipo = t

    def depositar(self, monto):

        if monto <= 0:
            return False

        self.__cantidad += monto
        return True

    def retirar(self, monto):

        if monto <= 0:
            return False

        if monto > self.__cantidad:
            return False

        self.__cantidad -= monto
        return True

    def getCantidad(self):
        return self.__cantidad

    def getTipo(self):
        return self.__tipo

    def __str__(self):

        return (
            "Cantidad:: " + str(self.__cantidad) +
            "\nTipo:: " + self.__tipo
        )
