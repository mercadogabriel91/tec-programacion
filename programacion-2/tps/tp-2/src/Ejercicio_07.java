package src;
import java.util.Scanner;

public class Ejercicio_07 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        double nota;

        // pedir la nota hasta que este entre 0 y 10
        do {
            System.out.print("Ingrese una nota (0-10): ");
            nota = scanner.nextDouble();

            if (nota < 0 || nota > 10) {
                System.out.println("Error: Nota inválida. Ingrese una nota entre 0 y 10.");
            }
        } while (nota < 0 || nota > 10);

        System.out.println("Nota válida ingresada: " + nota);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
