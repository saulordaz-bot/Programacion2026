''' 
Created on March, 2026
@author: SaulOG

'''
from Cuenta import *
from Menu import *

class Main:
	pass


menu = Menu("Bienvenidos al Banco Pato")
menu.darBienvenida()
opcion = menu.despliegaMenu()
menu.procesaOpcion(opcion)
