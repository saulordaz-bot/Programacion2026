# Ejercicio 4:Elabora un programa que genere una sucesión de números aleatorios en el intervalo [0.01,0.20], cuya suma sea menor que 1.50
import random

suma = 0

while suma < 1.50:
    numero = random.uniform(0.01, 0.20)  # genera número aleatorio entre 0.01 y 0.20
    
    if suma + numero < 1.50:  # verificamos que la suma siga siendo menor que 1.50
        print(numero)
        suma += numero
    else:
        break

print("Suma total:", suma)
