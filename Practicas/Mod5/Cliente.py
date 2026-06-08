'''
Created on april, 2026
@author: SaulO
'''

class Cliente:

    def __init__(self, nom, dir, edad):

        self.nombre = nom
        self.direccion = dir
        self.edad = edad

        self.cuentas = []

    def agregarCuenta(self, cuenta):

        self.cuentas.append(cuenta)

    def recuperarCuenta(self, posicion):

        if posicion >= 0 and posicion < len(self.cuentas):
            return self.cuentas[posicion]

        return None

    def borrarCuenta(self, posicion):

        if posicion >= 0 and posicion < len(self.cuentas):

            del self.cuentas[posicion]
            return True

        return False

    def __str__(self):

        salida = (
            "Nombre:: " + self.nombre +
            "\nDireccion:: " + self.direccion +
            "\nEdad:: " + str(self.edad)
        )

        salida += "\n\nCUENTAS DEL CLIENTE"

        for cuenta in self.cuentas:

            salida += "\n\n" + str(cuenta)

        return salida
