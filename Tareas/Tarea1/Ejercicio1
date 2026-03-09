#ejercicio 1:Modifica el programa que resuelve la ecuación cuadratica (vista en la ayudantía), de tal forma que tenga solución cuando el discriminante sea menor a cero.
import cmath  # cmath permite trabajar con raíces cuadradas de números negativos.

# Pedimos los coeficientes al usuario
a = float(input("Da tu coeficiente a: "))
b = float(input("Da tu coeficiente b: "))
c = float(input("Da tu coeficiente c: "))

dis = b**2 - 4*a*c  # discriminante

if a != 0:
    # Usamos cmath.sqrt para que funcione incluso si dis < 0.
    x1 = (-b + cmath.sqrt(dis)) / (2*a)
    x2 = (-b - cmath.sqrt(dis)) / (2*a)
    print("Las soluciones son:")
    print("x1 =", x1)
    print("x2 =", x2)
else:
    # Caso lineal: bx + c = 0.
    if b != 0:
        x = -c/b
        print("La ecuación es lineal, solución:", x)
    else:
        if c == 0:
            print("Soluciones infinitas")
        else:
            print("Contradicción")
