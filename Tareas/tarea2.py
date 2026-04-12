#Ordaz González Saúl 
#Martínez Hernández Marcos



class Numero:
    def __init__(self, valor):
        self.valor = valor

    def latex(self):
        return str(self.valor)

    def evaluar(self, variables=None):
        return self.valor

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"


class Variable:
    def __init__(self, nombre):
        self.nombre = nombre

    def latex(self):
        if len(self.nombre) > 1:
            return "\\" + self.nombre
        return self.nombre

    def evaluar(self, variables=None):
        return variables[self.nombre]

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"


class Suma:
    def __init__(self, izq, der):
        self.izq = Numero(izq) if isinstance(izq, (int, float)) else izq
        self.der = Numero(der) if isinstance(der, (int, float)) else der

    def latex(self):
        return f"{self.izq.latex()} + {self.der.latex()}"

    def evaluar(self, variables=None):
        return self.izq.evaluar(variables) + self.der.evaluar(variables)

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"


class Resta:
    def __init__(self, izq, der):
        self.izq = Numero(izq) if isinstance(izq, (int, float)) else izq
        self.der = Numero(der) if isinstance(der, (int, float)) else der

    def latex(self):
        return f"{self.izq.latex()} - {self.der.latex()}"

    def evaluar(self, variables=None):
        return self.izq.evaluar(variables) - self.der.evaluar(variables)

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"


class Producto:
    def __init__(self, izq, der):
        self.izq = Numero(izq) if isinstance(izq, (int, float)) else izq
        self.der = Numero(der) if isinstance(der, (int, float)) else der

    def latex(self):
        return f"{self.izq.latex()} \\cdot {self.der.latex()}"

    def evaluar(self, variables=None):
        return self.izq.evaluar(variables) * self.der.evaluar(variables)

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"


class Potencia:
    def __init__(self, base, exponente):
        self.base = Numero(base) if isinstance(base, (int, float)) else base
        self.exp = Numero(exponente) if isinstance(exponente, (int, float)) else exponente

    def latex(self):
        return f"{self.base.latex()}^{{{self.exp.latex()}}}"

    def evaluar(self, variables=None):
        return self.base.evaluar(variables) ** self.exp.evaluar(variables)

    def __add__(self, otro): return Suma(self, otro)
    def __sub__(self, otro): return Resta(self, otro)
    def __mul__(self, otro): return Producto(self, otro)
    def __pow__(self, otro): return Potencia(self, otro)

    def __radd__(self, otro): return Suma(otro, self)
    def __rsub__(self, otro): return Resta(otro, self)
    def __rmul__(self, otro): return Producto(otro, self)

    def _repr_latex_(self): return f"$${self.latex()}$$"
