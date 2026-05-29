#Create 21 mayo 2025

#Saúl Ordaz González
#Martínez Hernández Marcos



# Librería para eliminar signos de puntuación.
import string

def palabras_repetidas(nombre_archivo=None):

    # Verificar si el usuario proporcionó el parámetro
    if nombre_archivo is None:
        print("Error: Debe proporcionar el nombre del archivo.")
        return

    try:
        # Abrir archivo en modo lectura.
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            # Variable para guardar la última palabra de la línea anterior.
            palabra_anterior = ""
            # Variable para saber si hubo repeticiones
            hay_repetidas = False

            # Recorrer archivo línea por línea
            for numero_linea, linea in enumerate(archivo, start=1):
                # Convertir a minúsculas
                linea = linea.lower()

                # Eliminar signos de puntuación
                for simbolo in string.punctuation:
                    linea = linea.replace(simbolo, "")

                # Separar línea en palabras
                palabras = linea.split()

                # Si la línea está vacía, continuar con la siguiente.
                if not palabras:
                    continue

                # Verificar repetición entre líneas:
                # última palabra de línea anterior
                # con primera palabra de línea actual
                if palabra_anterior == palabras[0]:

                    hay_repetidas = True

                    print(
                        f"Palabra repetida entre líneas "
                        f"en línea {numero_linea}: "
                        f"'{palabras[0]}'")

                # Verificar palabras repetidas consecutivas
                # dentro de la misma línea
                for i in range(len(palabras) - 1):

                    if palabras[i] == palabras[i + 1]:

                        hay_repetidas = True

                        print(
                            f"Palabra repetida en línea "
                            f"{numero_linea}: "
                            f"'{palabras[i]}'")


                # Guardar última palabra de la línea actual
                palabra_anterior = palabras[-1]

            # Si no hubo palabras repetidas
            if not hay_repetidas:
                print("No se encontraron palabras repetidas.")

    # Error si el archivo no existe
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no existe.")

    # Capturar cualquier otro error
    except Exception as error:
        print("Ocurrió un error durante el procesamiento.")
        print("Detalle del error:", error)


# Llamada principal del programa:
palabras_repetidas("poema_20.txt")
