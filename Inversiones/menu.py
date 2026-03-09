from inversion import Inversion
from reporte import Reporte
from usuario import Usuario


class Menu:

    def iniciar(self):

        nombre = input("Ingresa tu nombre: ")
        capital = float(input("Ingresa el capital a invertir: "))
        tasa = float(input("Ingresa la tasa de interés (%): "))

        usuario = Usuario(nombre)
        inversion = Inversion(capital, tasa)
        reporte = Reporte()

        usuario.mostrarUsuario()
        reporte.mostrarResultados(inversion)
