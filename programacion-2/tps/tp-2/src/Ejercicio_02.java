package src;
import java.util.Scanner;

public class Ejercicio_02 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar los tres numeros
        System.out.print("Ingrese el primer número: ");
        int num1 = scanner.nextInt();
        System.out.print("Ingrese el segundo número: ");
        int num2 = scanner.nextInt();
        System.out.print("Ingrese el tercer número: ");
        int num3 = scanner.nextInt();

        // determinar el mayor
        int mayor = num1;
        if (num2 > mayor) {
            mayor = num2;
        }
        if (num3 > mayor) {
            mayor = num3;
        }

        System.out.println("El mayor es: " + mayor);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
