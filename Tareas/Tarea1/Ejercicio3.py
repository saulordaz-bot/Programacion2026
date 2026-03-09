# Ejercicio 3: Verificar si una palabra es palíndromo.
# Un palíndromo es una palabra que se lee igual de izquierda a derecha y viceversa.

palabra = input("Introduce una palabra: ")

# Normalizamos la palabra: quitamos espacios y la pasamos a minúsculas.
palabra = palabra.replace(" ", "").lower()

# Comparamos la palabra con su reverso.
if palabra == palabra[::-1]:
    print("La palabra es un palíndromo")
else:
    print("La palabra NO es un palíndromo")
