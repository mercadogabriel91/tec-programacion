package ejercicio3;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Asociación unidireccional (Libro -> Autor) y agregación (Libro -> Editorial) ---");
        Autor autor = new Autor("Jorge Luis Borges", "Argentina");
        Editorial sudamericana = new Editorial("Sudamericana", "algun lugar, CABA");
        Libro libro = new Libro("La fiesta del monstruo", "978-9500432443", autor, sudamericana);
        System.out.println(libro);

        System.out.println("\n--- El autor no sabe nada del libro ---");
        System.out.println(autor);

        System.out.println("\n--- Cambio de editorial: la anterior sigue existiendo ---");
        Editorial alfaguara = new Editorial("Alfaguara", "Av. Leandro N. Alem 720, CABA");
        libro.setEditorial(alfaguara);
        System.out.println(libro);
        System.out.println("Editorial anterior: " + sudamericana);
        libro.setAutor(null); // te tira  el error de validacion
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
