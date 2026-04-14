''' 
Created on Febrero,2026
@author: SaulOG

'''

from cuenta import Cuenta
from menu import Menu
from cliente import Cliente

class Main:
    pass


# ----- EJECUCIÓN -----

# Crear cliente
cliente1 = Cliente("Maria Hernandez", "CDMX", 25)

# Mostrar datos del cliente
cliente1.imprimirDetalles()

# Crear cuenta
cuenta1 = Cuenta(5000, 'D', cliente1.nombre)

# Crear menú
menu = Menu()
menu.darBienvenida()

opcion = ""

while opcion != "3":
    opcion = menu.despliegaMenu()
    menu.procesaOpcion(opcion, cuenta1)
