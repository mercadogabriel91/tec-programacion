package Ejercicio_02;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creación sin editorial (Independiente) ---");
        Libro libro1 = new Libro("Rayuela", "Julio Cortázar");
        System.out.println(libro1);

        System.out.println("\n--- Creación con editorial (cambia la editorial global) ---");
        Libro libro2 = new Libro("El Aleph", "Jorge Luis Borges", "Sudamericana");
        System.out.println(libro1);
        System.out.println(libro2);

        System.out.println("\n--- Actualizar títulos (válido e inválido) ---");
        libro1.actualizarTitulo("Rayuela (edición revisada)");
        libro2.actualizarTitulo("Clásicos", "El Aleph");
        libro1.actualizarTitulo(""); // se ignora por validación
        libro2.actualizarTitulo("Prefijo", "   ");

        System.out.println("\n--- Libros después de actualizar ---");
        System.out.println(libro1);
        System.out.println(libro2);

        System.out.println("\n--- Cambio de editorial global ---");
        Libro.cambiarEditorial("Planeta");
        System.out.println(libro1);
        System.out.println(libro2);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-4/src
 */
