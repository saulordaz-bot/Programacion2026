'''
Created on March, 2026
@author: SaulO

'''

'''
Clase Inversion
Se encarga de los cálculos de una inversión
'''

class Inversion:

    def __init__(self, capital, tasa):
        self.capital = capital
        self.tasa = tasa

    def calcularGanancia(self):
        return self.capital * (self.tasa / 100)

    def montoFinal(self):
        return self.capital + self.calcularGanancia()

    def compararInversion(self, otraInversion):
        # Método compuesto porque usa otros métodos
        
        mi_monto = self.montoFinal()
        otro_monto = otraInversion.montoFinal()

        if mi_monto > otro_monto:
            diferencia = mi_monto - otro_monto
            return f"La inversión 1 es mejor por {diferencia}"
        elif mi_monto < otro_monto:
            diferencia = otro_monto - mi_monto
            return f"La inversión 2 es mejor por {diferencia}"
        else:
            return "Ambas inversiones son iguales"

    def __str__(self):
        return (f"Capital: {self.capital}\n"
                f"Tasa: {self.tasa}%\n"
                f"Ganancia: {self.calcularGanancia()}\n"
                f"Monto final: {self.montoFinal()}")
