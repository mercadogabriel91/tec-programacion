package ejercicio2;

public class Libro {
    private final String isbn;
    private String titulo;
    private int anioPublicacion;
    private Autor autor;

    Libro(String isbn, String titulo, int anioPublicacion, Autor autor) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.anioPublicacion = anioPublicacion;
        this.autor = autor;
    }

    public String getIsbn() {
        return isbn;
    }

    public String getTitulo() {
        return titulo;
    }

    public int getAnioPublicacion() {
        return anioPublicacion;
    }

    public Autor getAutor() {
        return autor;
    }

    public void mostrarInfo() {
        System.out.println("\"" + titulo + "\" | ISBN: " + isbn + " | año: " + anioPublicacion
                + " | autor: " + autor.getNombre() + " (" + autor.getNacionalidad() + ")");
    }

    @Override
    public String toString() {
        return "Libro{isbn='" + isbn + "', titulo='" + titulo + "', anioPublicacion=" + anioPublicacion
                + ", autor=" + autor.getNombre() + "}";
    }
}
