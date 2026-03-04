# Defino una clase llamada Inversion, que me servirá como molde
# para crear objetos que representen una inversión.
class Inversion:
    
    # Este es el método constructor.
    # Se ejecuta automáticamente cuando creo un objeto de esta clase.
    # Recibe el capital y la tasa de interés.
    def __init__(self, capital, tasa):
        
        # Aquí guardo el capital dentro del objeto.
        # Uso self.capital para que el valor pertenezca al objeto.
        self.capital = capital
        
        # Aquí guardo la tasa de interés dentro del objeto.
        self.tasa = tasa

    # Este método calcula la ganancia que obtengo con la inversión.
    # No recibe parámetros porque usa los datos que ya tiene el objeto.
    def calcularGanancia(self):
        
        # Aplico la fórmula del interés simple:
        # ganancia = capital * (tasa / 100)
        return self.capital * (self.tasa / 100)

    # Este método calcula el monto final después de ganar intereses.
    def montoFinal(self):
        
        # Al capital le sumo la ganancia.
        # Llamo al método calcularGanancia() para no repetir código.
        return self.capital + self.calcularGanancia()


# Aquí le pido al usuario que ingrese el capital.
# Uso float() para convertir el dato a número decimal.
capital = float(input("Ingresa el capital a invertir: "))

# Aquí le pido al usuario que ingrese la tasa de interés.
# También lo convierto a decimal.
tasa = float(input("Ingresa la tasa de interés (%): "))

# Aquí creo un objeto llamado inv1 usando la clase Inversion.
# Le paso como argumentos el capital y la tasa que ingresó el usuario.
inv1 = Inversion(capital, tasa)

# Aquí imprimo la ganancia llamando al método del objeto.
print("Ganancia:", inv1.calcularGanancia())

# Aquí imprimo el monto final llamando al otro método.
print("Monto final:", inv1.montoFinal())
