'''
Created on May, 2026
@author: SaulO
'''

from Cuenta import Cuenta


class CuentaDeCredito(Cuenta):

    def __init__(self, ctd, limite):

        super().__init__(ctd, "Credito")

        self.limite = limite

    def retirar(self, monto):

        if monto <= 0:
            return False

        if monto > (self._cantidad + self.limite):

            print("No se pudo realizar el retiro.")
            return False

        self._cantidad -= monto

        return True
