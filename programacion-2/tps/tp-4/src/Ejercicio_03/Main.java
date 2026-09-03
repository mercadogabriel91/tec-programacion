package Ejercicio_03;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creación con ambos constructores ---");
        Alumno a1 = new Alumno("Sofía", 8.5);
        Alumno a2 = new Alumno("Pedro"); // promedio 0
        Alumno a3 = new Alumno("Lucía", 5.5);

        System.out.println("\n--- Actualizar promedios ---");
        a2.actualizarPromedio(7.0);
        a3.actualizarPromedio(new double[] {6, 7, 8, 9});
        a1.actualizarPromedio(12); // se ajusta a 10
        a2.actualizarPromedio(new double[] {}); // inválido

        System.out.println("\n--- Estado inicial (nota de aprobación = " + Alumno.getNotaAprobacion() + ") ---");
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);

        System.out.println("\n--- Cambio de nota de aprobación global ---");
        Alumno.cambiarNotaAprobacion(8);
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-4/src
 */
