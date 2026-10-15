package ejercicio2;

import java.util.ArrayList;
import java.util.List;

public class Biblioteca {
    private String nombre;
    private final List<Libro> libros = new ArrayList<>();

    public Biblioteca(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    // composición, los libros se crean adentro y nacen y mueren con la biblioteca
    public void agregarLibro(String isbn, String titulo, int anioPublicacion, Autor autor) {
        if (autor == null) {
            System.out.println("Error: el libro \"" + titulo + "\" necesita un autor.");
            return;
        }
        if (buscarLibroPorIsbn(isbn) != null) {
            System.out.println("Error: ya existe un libro con ISBN " + isbn);
            return;
        }
        libros.add(new Libro(isbn, titulo, anioPublicacion, autor));
    }

    public void listarLibros() {
        if (libros.isEmpty()) {
            System.out.println("La biblioteca no tiene libros.");
            return;
        }
        for (Libro l : libros) {
            l.mostrarInfo();
        }
    }

    public Libro buscarLibroPorIsbn(String isbn) {
        for (Libro l : libros) {
            if (l.getIsbn().equals(isbn)) {
                return l;
            }
        }
        return null;
    }

    public void eliminarLibro(String isbn) {
        Libro l = buscarLibroPorIsbn(isbn);
        if (l == null) {
            System.out.println("Error: no existe un libro con ISBN " + isbn);
            return;
        }
        libros.remove(l);
        System.out.println("Libro eliminado: \"" + l.getTitulo() + "\"");
    }

    public int obtenerCantidadLibros() {
        return libros.size();
    }

    public List<Libro> filtrarLibrosPorAnio(int anio) {
        List<Libro> resultado = new ArrayList<>();
        for (Libro l : libros) {
            if (l.getAnioPublicacion() == anio) {
                resultado.add(l);
            }
        }
        return resultado;
    }

    public void mostrarAutoresDisponibles() {
        List<Autor> autores = new ArrayList<>();
        for (Libro l : libros) {
            if (!autores.contains(l.getAutor())) {
                autores.add(l.getAutor());
            }
        }
        for (Autor a : autores) {
            a.mostrarInfo();
        }
    }

    @Override
    public String toString() {
        return "Biblioteca{nombre='" + nombre + "', cantidadLibros=" + libros.size() + "}";
    }
}
