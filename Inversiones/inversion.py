class Inversion:

    def __init__(self, capital, tasa):
        self.capital = capital
        self.tasa = tasa

    def calcularGanancia(self):
        return self.capital * (self.tasa / 100)

    def montoFinal(self):
        return self.capital + self.calcularGanancia()
