package ejercicio2;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- 1. Creación de la biblioteca ---");
        Biblioteca biblioteca = new Biblioteca("Gran Biblioteca de Alejandría");
        System.out.println(biblioteca);

        System.out.println("\n--- 2. Creación de autores ---");
        Autor borges = new Autor("A01", "Jorge Luis Borges", "Argentina");
        Autor shakespeare = new Autor("A02", "William Shakespeare", "Inglaterra");
        Autor dostoyevski = new Autor("A03", "Fiodor Dostoyevski", "Rusia");
        borges.mostrarInfo();
        shakespeare.mostrarInfo();
        dostoyevski.mostrarInfo();

        System.out.println("\n--- 3. Alta de libros (los crea la biblioteca) ---");
        biblioteca.agregarLibro("978-0001", "Ficciones", 1944, borges);
        biblioteca.agregarLibro("978-0002", "El Aleph", 1949, borges);
        biblioteca.agregarLibro("978-0003", "Hamlet", 1603, shakespeare);
        biblioteca.agregarLibro("978-0004", "Macbeth", 1606, shakespeare);
        biblioteca.agregarLibro("978-0005", "Crimen y castigo", 1866, dostoyevski);
        biblioteca.agregarLibro("978-0001", "Duplicado", 2000, borges); // ISBN repetido

        System.out.println("\n--- 4. Listado de libros ---");
        biblioteca.listarLibros();

        System.out.println("\n--- 5. Búsqueda por ISBN ---");
        Libro encontrado = biblioteca.buscarLibroPorIsbn("978-0003");
        if (encontrado != null) {
            encontrado.mostrarInfo();
        }

        System.out.println("\n--- 6. Libros publicados en 1949 ---");
        for (Libro l : biblioteca.filtrarLibrosPorAnio(1949)) {
            l.mostrarInfo();
        }

        System.out.println("\n--- 7. Eliminar 978-0004 y listar los restantes ---");
        biblioteca.eliminarLibro("978-0004");
        biblioteca.listarLibros();

        System.out.println("\n--- 8. Cantidad total de libros ---");
        System.out.println("Cantidad de libros: " + biblioteca.obtenerCantidadLibros());

        System.out.println("\n--- 9. Autores con libros disponibles ---");
        biblioteca.mostrarAutoresDisponibles();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-6/src
 */
