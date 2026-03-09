#Ejercicio 2:Desarrollar un programa que calcule la suma de los dígitos de cualquier número entero positivo introducido por el usuario.
# Pedimos el número al usuario
numero = int(input("Ingresa un número entero positivo: "))

suma = 0

# Repetimos hasta que el número sea 0
while numero != 0:
    suma += numero % 10   # obtenemos el último dígito y lo sumamos
    numero = numero // 10 # quitamos el último dígito

print("La suma de los dígitos es:", suma)
