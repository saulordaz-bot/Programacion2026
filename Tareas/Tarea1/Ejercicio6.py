#Ejercicio 6: Haz un programa que te regrese los primeros 100 términos de la sucesión de Fibonacci (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, · · ·)
# Primeros 100 términos de la sucesión de Fibonacci

a = 1
b = 1

print(a)
print(b)

for i in range(98):  # ya tenemos los dos primeros
    c = a + b
    print(c)
    
    a = b
    b = c
