'''
Created on March,2026
@author: SaulO
'''

class Cliente:

    def __init__(self, nom, dir, edad, cuenta):

        self.nombre = nom
        self.direccion = dir
        self.edad = edad
        self.cuenta = cuenta

    def __str__(self):

        return (
            "Nombre:: " + self.nombre +
            "\nDireccion:: " + self.direccion +
            "\nEdad:: " + str(self.edad) +
            "\n\nDATOS DE LA CUENTA\n" +
            str(self.cuenta)
        )
