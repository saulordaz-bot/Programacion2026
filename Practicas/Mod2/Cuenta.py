'''
Created on feb, 2026
@author: SaulO
'''

class Cuenta:

    def __init__(self, ctd, t, titular):

        self.cantidad = ctd
        self.tipo = t
        self.titular = titular

    def imprimirDetalles(self):

        print("Desde el método")

        print("cantidad::", self.cantidad)
        print("tipo::", self.tipo)
        print("titular::", self.titular)
