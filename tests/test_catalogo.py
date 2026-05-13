"""Pruebas unitarias para el módulo catálogo."""
import sys
sys.path.insert(0, '../src')

from catalogo import Libro, Catalogo


def test_crear_libro():
    libro = Libro("978-1", "El Quijote", "Cervantes")
    assert libro.isbn == "978-1"
    assert libro.disponible == True
    print("✅ test_crear_libro: PASÓ")


def test_agregar_libro_al_catalogo():
    catalogo = Catalogo()
    libro = Libro("978-1", "El Quijote", "Cervantes")
    resultado = catalogo.agregar_libro(libro)
    assert resultado == True
    assert catalogo.total_libros() == 1
    print("✅ test_agregar_libro: PASÓ")


def test_buscar_por_isbn():
    catalogo = Catalogo()
    libro = Libro("978-2", "Cien Años de Soledad", "García Márquez")
    catalogo.agregar_libro(libro)
    encontrado = catalogo.buscar_por_isbn("978-2")
    assert encontrado is not None
    assert encontrado.autor == "García Márquez"
    print("✅ test_buscar_por_isbn: PASÓ")


def test_buscar_por_titulo():
    catalogo = Catalogo()
    catalogo.agregar_libro(Libro("978-3", "Python para todos", "Dr. Chuck"))
    catalogo.agregar_libro(Libro("978-4", "Python avanzado", "Luciano R."))
    resultados = catalogo.buscar_por_titulo("python")
    assert len(resultados) == 2
    print("✅ test_buscar_por_titulo: PASÓ")


def test_isbn_duplicado():
    catalogo = Catalogo()
    libro1 = Libro("978-1", "Libro A", "Autor A")
    libro2 = Libro("978-1", "Libro B", "Autor B")  # ISBN duplicado
    catalogo.agregar_libro(libro1)
    try:
        catalogo.agregar_libro(libro2)
        print("❌ test_isbn_duplicado: FALLÓ - debería lanzar ValueError")
    except ValueError:
        print("✅ test_isbn_duplicado: PASÓ")


if __name__ == "__main__":
    test_crear_libro()
    test_agregar_libro_al_catalogo()
    test_buscar_por_isbn()
    test_buscar_por_titulo()
    test_isbn_duplicado()
    print("\n🎉 Todas las pruebas completadas")