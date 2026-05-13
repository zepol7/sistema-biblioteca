"""Módulo de catálogo de libros - Sistema Biblioteca"""

class Libro:
    def __init__(self, isbn, titulo, autor, disponible=True):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({estado})"


class Catalogo:
    def __init__(self):
        self._libros = {}
    
    def agregar_libro(self, libro):
        """Agrega un libro al catálogo."""
        if libro.isbn in self._libros:
            raise ValueError(f"El libro con ISBN {libro.isbn} ya existe")
        self._libros[libro.isbn] = libro
        return True
    
    def buscar_por_isbn(self, isbn):
        """Busca un libro por su ISBN."""
        return self._libros.get(isbn)
    
    def buscar_por_titulo(self, termino):
        """Busca libros cuyo título contiene el término."""
        termino = termino.lower()
        return [libro for libro in self._libros.values()
                if termino in libro.titulo.lower()]
    
    def listar_disponibles(self):
        """Retorna lista de libros disponibles."""
        return [libro for libro in self._libros.values() if libro.disponible]
    
    def total_libros(self):
        """Retorna el total de libros en el catálogo."""
        return len(self._libros)