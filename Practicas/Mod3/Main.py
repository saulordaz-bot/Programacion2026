'''
Created on March,2026
@author: SaulO
'''

from Menu import Menu

class Main:
    pass

menu = Menu()

menu.darBienvenida()

opcion = 0

while opcion != 4:

    opcion = menu.desplegarMenu()

    menu.procesarOpcion(opcion)
