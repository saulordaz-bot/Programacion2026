#@ author: Marcos Martínez Herández.
#@ author: Saúl Ordaz González.
#Create 6 mayo 2026.

# Diccionario que convierte puntos de calificación a letras
# Ahora las equivalencias son: A=10, B=9, C=8, D=7, F=6
puntos_a_letra = {
    10.0: "A",
    9.0: "B",
    8.0: "C",
    7.0: "D",
    6.0: "F"
}

# Diccionario inverso que convierte letras a puntos
# Se construye automáticamente a partir del anterior
letra_a_puntos = {v: k for k, v in puntos_a_letra.items()}

def convertir_puntos_a_letra(valor: float) -> str:
    """
    Convierte puntos de calificación a letra.
    Si el valor no existe en el diccionario, lanza una excepción.
    """
    if valor in puntos_a_letra:
        return puntos_a_letra[valor]
    # Si no se encuentra el valor, se lanza un error
    raise ValueError("Puntos no válidos")

def convertir_letra_a_puntos(valor: str) -> float:
    """
    Convierte letra de calificación a puntos.
    Si la letra no existe en el diccionario, lanza una excepción.
    """
    valor = valor.upper()  # Se asegura que la letra esté en mayúsculas
    if valor in letra_a_puntos:
        return letra_a_puntos[valor]
    # Si no se encuentra la letra, se lanza un error
    raise ValueError("Letra no válida")

def manejar_conversion(entrada: str) -> str:
    """
    Intenta convertir la entrada primero como puntos (float).
    Si falla, intenta convertirla como letra.
    Si ambas conversiones fallan, devuelve un mensaje de error.
    """
    try:
        # Primer intento: convertir la entrada a número (float)
        puntos = float(entrada)
        return f"{puntos} → {convertir_puntos_a_letra(puntos)}"
    except ValueError:
        try:
            # Segundo intento: convertir la entrada como letra
            return f"{entrada.upper()} → {convertir_letra_a_puntos(entrada)}"
        except ValueError:
            # Si ambas conversiones fallan, se indica que la entrada es inválida
            return f"Entrada inválida: {entrada}"

def main():
    """
    Función principal del programa.
    Pide entradas al usuario en un ciclo hasta que se ingrese una línea en blanco.
    """
    print("Conversor de calificaciones (enter vacío para salir)")
    while True:
        # Se solicita la entrada al usuario
        entrada = input("Ingresa calificación: ").strip()
        if entrada == "":
            # Si la entrada está vacía, se termina el programa
            break
        # Se procesa la entrada y se muestra el resultado
        print(manejar_conversion(entrada))

# Punto de entrada del programa
if _name_ == "_main_":
    main()
