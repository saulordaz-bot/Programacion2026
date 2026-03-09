# Ejercicio 5: Verificar si un número es primo y mostrar los primeros N primos.
# Función para verificar si un número es primo.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # solo hasta la raíz cuadrada.
        if n % i == 0:
            return False
    return True

# Parte i: Verificar si un número es primo.
num = int(input("Introduce un número entero: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} NO es primo")

# Parte ii: Mostrar los primeros N números primos.
N = int(input("¿Cuántos números primos quieres ver?: "))
contador = 0
numero = 2
print(f"Los primeros {N} números primos son:")
while contador < N:
    if es_primo(numero):
        print(numero, end=" ")
        contador += 1
    numero += 1
