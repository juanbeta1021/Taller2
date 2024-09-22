class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"'{self.titulo}' de {self.autor} ({self.paginas} páginas)"

    def __repr__(self):
        # Representación formal con el nombre de la clase y los atributos
        return f"Libro(titulo='{self.titulo}', autor='{self.autor}', paginas={self.paginas})"

libro1 = Libro("El principito", "Antoine de Saint-Exupéry", 96)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)

print(str(libro1))  # Ver título, autor y páginas
print(str(libro2))

print(repr(libro1))  # ver la representación con estructura de clase
print(repr(libro2))
