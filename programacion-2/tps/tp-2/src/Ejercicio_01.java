package src;
import java.util.Scanner;

public class Ejercicio_01 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el año
        System.out.print("Ingrese un año: ");
        int anio = scanner.nextInt();

        // Un año es bisiesto si es divisible por 4,
        // pero no por 100, salvo que también sea divisible por 400
        boolean bisiesto = (anio % 4 == 0 && anio % 100 != 0) || (anio % 400 == 0);

        if (bisiesto) {
            System.out.println("El año " + anio + " es bisiesto.");
        } else {
            System.out.println("El año " + anio + " no es bisiesto.");
        }

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
