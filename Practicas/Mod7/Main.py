'''
Created on May, 2026
@author: SaulO
'''

from Menu import Menu

menu = Menu()

menu.darBienvenida()

opcion = 0

while opcion != 2:

    opcion = menu.desplegarMenu()

    menu.procesarOpcion(opcion)
