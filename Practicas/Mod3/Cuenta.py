'''
Created on March,2026
@author: SaulO
'''

class Cuenta:

    def __init__(self, ctd, t):

        self.cantidad = ctd
        self.tipo = t

    def depositar(self, monto):

        if monto <= 0:
            return False

        self.cantidad += monto
        return True

    def retirar(self, monto):

        if monto <= 0:
            return False

        if monto > self.cantidad:
            return False

        self.cantidad -= monto
        return True

    def __str__(self):

        return (
            "Cantidad:: " + str(self.cantidad) +
            "\nTipo:: " + self.tipo
        )
