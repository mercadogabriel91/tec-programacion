package Ejercicio_02;

public class Libro {
    private String titulo;
    private String autor;
    private static String editorial = "Independiente";

    // constructor basico
    public Libro(String titulo, String autor) {
        this.titulo = "Sin título";
        this.autor = "Sin autor";
        setTitulo(titulo);
        setAutor(autor);
    }

    // constructor con editorial: se lo manda al base y después le cambia la editorial global
    public Libro(String titulo, String autor, String editorial) {
        this(titulo, autor);
        cambiarEditorial(editorial);
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        if (titulo == null || titulo.trim().isEmpty()) {
            System.out.println("Error: el título no puede estar vacío.");
            return;
        }
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        if (autor == null || autor.trim().isEmpty()) {
            System.out.println("Error: el autor no puede estar vacío.");
            return;
        }
        this.autor = autor;
    }

    public String getEditorial() {
        return editorial;
    }

    public void actualizarTitulo(String nuevoTitulo) {
        setTitulo(nuevoTitulo);
    }

    public void actualizarTitulo(String prefijo, String nuevoTitulo) {
        if (prefijo == null || prefijo.trim().isEmpty() || nuevoTitulo == null || nuevoTitulo.trim().isEmpty()) {
            System.out.println("Error: el prefijo y el nuevo título no pueden estar vacíos.");
            return;
        }
        setTitulo(prefijo + " " + nuevoTitulo);
    }

    public static void cambiarEditorial(String nueva) {
        if (nueva == null || nueva.trim().isEmpty()) {
            System.out.println("Error: la editorial no puede estar vacía.");
            return;
        }
        editorial = nueva;
    }

    @Override
    public String toString() {
        return "Libro{titulo='" + titulo + "', autor='" + autor + "', editorial='" + editorial + "'}";
    }
}
