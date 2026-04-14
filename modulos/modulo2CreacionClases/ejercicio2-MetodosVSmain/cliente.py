
''' 
Created on Febrero,2019 
@author: SaulOG

'''
class Cliente:

    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def imprimirDetalles(self):
        print("Nombre:", self.nombre)
        print("Dirección:", self.direccion)
        print("Edad:", self.edad)
