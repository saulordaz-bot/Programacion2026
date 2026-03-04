# Saul Ordaz Gonzalez

class Cuenta:
    # Método constructor: se ejecuta cuando se crea un objeto Cuenta
    def __init__(self, valor1, valor2, valor3):
        self.saldo = valor1          # Guarda el saldo inicial
        self.tipo = valor2           # Guarda el tipo de cuenta
        self.fechaCreacion = valor3  # Guarda la fecha de creación

    def depositar(self, cantidad):
        # Suma la cantidad al saldo actual
        self.saldo = self.saldo + cantidad

    def retirar(self, cantidad):
        # Resta la cantidad al saldo actual
        self.saldo = self.saldo - cantidad

    def informacion(self):
        # Muestra toda la información de la cuenta
        print("Saldo..", self.saldo)
        print("Tipo..", self.tipo)
        print("Fecha Creacion..", self.fechaCreacion)


class Menu:

    # El método debe estar alineado dentro de la clase, por eso no corría
    def __init__(self, mensaje):
        self.mensajeBienvenida = mensaje

    def darBienvenida(self):

        print(self.mensajeBienvenida)

    def mostrarMenu(self):

        print("\n===== MENU =====")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Ver información de la cuenta")
        print("4. Salir")



print("Desde el Menu")

menu = Menu("Hola, bienvenido al sistema")
menu.darBienvenida()
menu.mostrarMenu()

# Creamos un objeto Cuenta
cuenta1 = Cuenta(3000, "D", "2023-01-01")

print(f"Saldo inicial: {cuenta1.saldo}")
print(f"Tipo de cuenta: {cuenta1.tipo}")

# Probamos el depósito
cuenta1.depositar(5000)
print("probando el deposito")
print(f"Nuevo saldo: {cuenta1.saldo}")

# Probamos el retiro
cuenta1.retirar(1200)
print("probando el retiro")
print(f"Nuevo saldo: {cuenta1.saldo}")

# Mostramos toda la información
cuenta1.informacion()


