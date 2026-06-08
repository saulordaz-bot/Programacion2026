'''
Created on May, 2026
@author: SaulO
'''

from Cuenta import Cuenta

class CuentaDeAhorro(Cuenta):

    def __init__(self, ctd):

        super().__init__(ctd, "Ahorro")
