class Reporte:

    def mostrarResultados(self, inversion):
        print("Ganancia:", inversion.calcularGanancia())
        print("Monto final:", inversion.montoFinal())
