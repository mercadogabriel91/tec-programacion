package Ejercicio_03;

public class Main {
    public static void main() {
        Libro libro = new Libro();
        final int cyberpunk = 2077;

        libro.setTitulo("100 años de soledad");
        libro.setAutor("Gabriel García Márquez");
        libro.setAñoPublicacion(1967);

        // intentar modificar con un año inválido
        System.out.println("--- Prueba con año inválido ---");
        libro.setAñoPublicacion(cyberpunk);
        System.out.println("Año actual del libro: " + libro.getAñoPublicacion());

        // modificar con un año válido
        System.out.println("\n--- Modificación con año válido ---");
        libro.setAñoPublicacion(1970);

        System.out.println("\n--- Información final ---");
        libro.mostrarInfo();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-3/src
 */
