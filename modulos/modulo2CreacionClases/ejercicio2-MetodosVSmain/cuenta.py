''' 
Created on Feb, 2026
@author: SaulOG

'''
class Cuenta:

    def __init__(self, saldo, tipo, titular):
        self.saldo = saldo
        self.tipo = tipo
        self.titular = titular

    def depositar(self, cantidad):
        self.saldo += cantidad
        print("Depósito realizado. Nuevo saldo:", self.saldo)

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado. Nuevo saldo:", self.saldo)
        else:
            print("Fondos insuficientes")
