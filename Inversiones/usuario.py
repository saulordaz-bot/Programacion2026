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
        self.nombre = nombre

    def __str__(self):
        # Define cómo se muestra el usuario
        return f"Usuario: {self.nombre}"
