#Ordaz González Saúl
#Martínez Hernández Marcos

class Playlist:
  def __init__(self, nombre):
    self.nombre = nombre
    self.canciones = []

  def añadir_cancion(self, titulo):
    if len(self.canciones) >= 5:
      print("Alcanzaste el límite máximo de canciones por playlist")
    else:
      if titulo in self.canciones:
        print("La canción ya se encuentra en la playlist")
      else:
        self.canciones.append(titulo)
        print(f"{titulo} añadida a {self.nombre}.")

  def eliminar_cancion(self, titulo):
    if titulo in self.canciones:
      self.canciones.remove(titulo)
      print(f"{titulo} ha sido eliminado de {self.nombre}")
    else:
      print(f"{titulo} no está en {self.nombre}")

  def total_canciones(self):
    return len(self.canciones)

  def mostrar_playlist(self):
    print(f"========== Playlist: {self.nombre} ==========")
    if len(self.canciones) == 0:
      print("La Playlist está vacía actualmente")
    else:
      for i, titulo in enumerate(self.canciones, 1):
        print(i, titulo)

  def limpiar_playlist(self):
    self.canciones.clear()
    print("La playlist está vacía")

  
  def buscador(self, texto):
    encontrados = []

    for cancion in self.canciones:
      if cancion.lower().startswith(texto.lower()):
        encontrados.append(cancion)

    if encontrados:
      print("Coincidencias encontradas:")
      for c in encontrados:
        print(c)
    else:
      print(f"No hay canciones que comiencen con '{texto}' en {self.nombre}")


