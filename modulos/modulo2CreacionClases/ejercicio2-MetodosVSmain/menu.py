''' 
Created on Febrero,2019 
@author: SaulOG

'''
class Menu:

    def __init__(self):
        self.mensajeDeBienvenida = "Bienvenido al sistema bancario"

    def darBienvenida(self):
        print(self.mensajeDeBienvenida)

    def despliegaMenu(self):
        print("\n--- MENÚ ---")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        return opcion

    def procesaOpcion(self, opcion, cuenta):

        if opcion == "1":
            cantidad = float(input("Cantidad a depositar: "))
            cuenta.depositar(cantidad)

        elif opcion == "2":
            cantidad = float(input("Cantidad a retirar: "))
            cuenta.retirar(cantidad)

        elif opcion == "3":
            print("Gracias por usar el sistema")

        else:
            print("Opción inválida")
