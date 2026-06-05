# Created on june 2026, by:
#@Ordaz González Saúl 
#@Martínez Hernández Marcos


class Expresion:

    def __add__(self, otro):
        return Suma(self, otro)

    def __sub__(self, otro):
        return Resta(self, otro)

    def __mul__(self, otro):
        return Producto(self, otro)

    def __pow__(self, otro):
        return Potencia(self, otro)

    def _repr_latex_(self):
        return f"$${self.latex()}$$"


class Numero(Expresion):

    def __init__(self, valor):
        self.valor = valor

    def latex(self):
        return str(self.valor)

    def evaluar(self, variables=None):
        return self.valor


class Variable(Expresion):

    def __init__(self, nombre):
        self.nombre = nombre

    def __radd__(self, otro):
        return Suma(otro, self)

    def __rsub__(self, otro):
        return Resta(otro, self)

    def __rmul__(self, otro):
        return Producto(otro, self)


class OperacionBinaria(Expresion):

    def __init__(self, izq, der):
        self.izq = Numero(izq) if isinstance(izq, (int, float)) else izq
        self.der = Numero(der) if isinstance(der, (int, float)) else der


class Suma(OperacionBinaria):
    pass


class Resta(OperacionBinaria):

    def __rsub__(self, otro):
        return Resta(otro, self)


class Producto(OperacionBinaria):

    def __rmul__(self, otro):
        return Producto(otro, self)


class Potencia(Expresion):

    def __init__(self, base, exponente):
        self.base = Numero(base) if isinstance(base, (int, float)) else base
        self.exp = Numero(exponente) if isinstance(exponente, (int, float)) else exponente

    def __rmul__(self, otro):
        return Producto(otro, self)
