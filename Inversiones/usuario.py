'''
Created on March, 2026
@author: SaulO

'''
'''
Clase Usuario
Representa al usuario del sistema
'''

class Usuario:

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__inversiones = []   # lista de cuentas/inversiones

    def agregarInversion(self, inversion):
        self.__inversiones.append(inversion)

    def mostrarInversiones(self):
        for i, inv in enumerate(self.__inversiones, start=1):
            print(f"\n--- Inversión {i} ---")
            print(inv)

    def compararInversiones(self):
        if len(self.__inversiones) < 2:
            print("Se necesitan al menos 2 inversiones para comparar.")
            return

        mejor = self.__inversiones[0]
        for inv in self.__inversiones[1:]:
            if inv.montoFinal() > mejor.montoFinal():
                mejor = inv

        print("\nLa mejor inversión es:")
        print(mejor)

    def __str__(self):
        return f"Usuario: {self.__nombre}"
