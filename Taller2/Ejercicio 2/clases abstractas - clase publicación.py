from abc import ABC, abstractmethod


# Clase abstracta Publicacion
class Publicacion(ABC):
    @abstractmethod
    def informacion(self):
        pass

    @abstractmethod
    def resumen(self):
        pass


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


#instancias de Libro y Revista
libro = Libro("El señor de los anillos", "J.R.R. Tolkien", 1178)
revista = Revista("National Geographic", "Septiembre 2024", 15)

print(libro.informacion())
print(libro.resumen())
print(revista.informacion())
print(revista.resumen())
