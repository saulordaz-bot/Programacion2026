'''
Created on March, 2026
@author: SaulO

'''

class Reporte:

    def mostrarResultados(self, inversion):
        print("Ganancia:", inversion.calcularGanancia())
        print("Monto final:", inversion.montoFinal())

    # usando método compuesto
    def mostrarResumen(self, inversion):
        print(inversion.resumen())
