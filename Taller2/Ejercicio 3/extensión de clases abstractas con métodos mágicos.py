from abc import ABC, abstractmethod


# Clase abstracta Publicacion
class Publicacion(ABC):
    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass

    # Método mágico __str__ en la clase base
    def __str__(self):
        return "Tipo de publicación: Publicacion"


# Clase derivada Libro
class Libro(Publicacion):
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def informacion(self):
        return f"Libro: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

    def resumen(self):
        return f"Este libro, '{self.titulo}', escrito por {self.autor}, tiene {self.paginas} páginas."

    # Sobrescribiendo el método __str__
    def __str__(self):
        return f"Tipo de publicación: Libro, Título: {self.titulo}"


# Clase derivada Revista
class Revista(Publicacion):
    def __init__(self, titulo, edicion, articulos):
        self.titulo = titulo
        self.edicion = edicion
        self.articulos = articulos

    def informacion(self):
        return f"Revista: {self.titulo}, Edición: {self.edicion}, Número de artículos: {self.articulos}"

    def resumen(self):
        return f"La revista '{self.titulo}', edición {self.edicion}, contiene {self.articulos} artículos."

    # Sobrescribiendo el método __str__
    def __str__(self):
        return f"Tipo de publicación: Revista, Título: {self.titulo}"

libro = Libro("El hobbit", "J.R.R. Tolkien", 310)
revista = Revista("Scientific American", "Octubre 2024", 10)

print(str(libro))
print(str(revista))
