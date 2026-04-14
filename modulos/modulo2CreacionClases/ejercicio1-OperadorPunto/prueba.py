from cuenta import Cuenta

# Primer objeto
cuenta1 = Cuenta(5000, 'D', "Maria Hernandez")

# Segundo objeto
cuenta2 = Cuenta(12000, 'C', "Juan Perez")

# Mostrar datos
print(cuenta1.titular, cuenta1.saldo, cuenta1.tipo)
print(cuenta2.titular, cuenta2.saldo, cuenta2.tipo)
