package ejercicio3;

public class Libro {
    private String titulo;
    private String isbn;
    private Autor autor;
    private Editorial editorial;

    // el libro conoce a su autor y a su editorial, pero ninguno de ellos conoce al libro
    public Libro(String titulo, String isbn, Autor autor, Editorial editorial) {
        this.titulo = titulo;
        this.isbn = isbn;
        setAutor(autor);
        setEditorial(editorial);
    }

    public String getTitulo() {
        return titulo;
    }

    public String getIsbn() {
        return isbn;
    }

    public Autor getAutor() {
        return autor;
    }

    public void setAutor(Autor autor) {
        if (autor == null) {
            System.out.println("Error: el libro necesita un autor si o si.");
            return;
        }
        this.autor = autor;
    }

    public Editorial getEditorial() {
        return editorial;
    }

    public void setEditorial(Editorial editorial) {
        if (editorial == null) {
            System.out.println("Error: el libro necita una editorial.");
            return;
        }
        this.editorial = editorial;
    }

    @Override
    public String toString() {
        return "Libro{titulo='" + titulo + "', isbn='" + isbn + "', autor=" + autor + ", editorial=" + editorial + "}";
    }
}
