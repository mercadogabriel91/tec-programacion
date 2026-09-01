package Ejercicio_01;

public class Main {
    public static void main() {
        Estudiante estudiante = new Estudiante();

        // probar datos inválidos
        System.out.println("--- Prueba con datos inválidos ---");
        estudiante.setNombre("");
        estudiante.setApellido("   ");
        estudiante.setCurso("");
        estudiante.setCalificacion(11.5);

        // cargar datos correctos
        System.out.println("\n--- Carga de datos válidos ---");
        estudiante.setNombre("Gabriel");
        estudiante.setApellido("Mercado");
        estudiante.setCurso("Programación 2");
        estudiante.setCalificacion(7.5);
        estudiante.mostrarInfo();

        // probar límites de las notas
        System.out.println("\n--- Probar de subir y bajar las notas y ver que te tira ---");
        estudiante.subirCalificacion(3.0); // debería fallar (ya que es mas de 10)
        estudiante.subirCalificacion(2.0); // válido -> 9.5
        estudiante.bajarCalificacion(10.0); // debería fallar (baja de 0)
        estudiante.bajarCalificacion(1.5); // válido -> 8.0

        System.out.println("\n--- Información final ---");
        estudiante.mostrarInfo();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-3/src
 */
