package Ejercicio_03;

import java.time.Year;

public class Libro {
    private String titulo;
    private String autor;
    private int añoPublicacion;

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

    public int getAñoPublicacion() {
        return añoPublicacion;
    }

    public void setAñoPublicacion(int añoPublicacion) {
        int añoActual = Year.now().getValue();
        if (añoPublicacion <= 0) {
            System.out.println("Error: el año de publicación debe ser mayor a 0.");
            return;
        }
        if (añoPublicacion > añoActual) {
            System.out.println("Error: el año de publicación no puede ser futuro.");
            return;
        }
        this.añoPublicacion = añoPublicacion;
    }

    public void mostrarInfo() {
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Año de publicación: " + añoPublicacion);
    }
}
