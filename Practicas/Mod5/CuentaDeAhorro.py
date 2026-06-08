'''
Created on November, 2018
@author: lunysska
'''

from Cuenta import Cuenta

class CuentaDeAhorro(Cuenta):

    def __init__(self, ctd):

        super().__init__(ctd, "Ahorro")
