'''
Created on May, 2026
@author: SaulO
'''

class Cuenta:

    def __init__(self, ctd, t):

        self._cantidad = ctd
        self._tipo = t

    def depositar(self, monto):

        if monto <= 0:
            return False

        self._cantidad += monto
        return True

    def retirar(self, monto):

        if monto <= 0:
            return False

        if monto > self._cantidad:
            return False

        self._cantidad -= monto
        return True

    def __str__(self):

        return (
            "Cantidad:: " + str(self._cantidad) +
            "\nTipo:: " + self._tipo
        )
