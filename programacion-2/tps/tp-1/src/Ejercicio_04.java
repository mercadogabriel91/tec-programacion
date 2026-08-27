package src;
import java.util.Scanner;

public class Ejercicio_04 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el primer numero
        System.out.print("Ingrese el primer numero: ");
        int num1 = scanner.nextInt();
        // Capturar el segundo numero
        System.out.print("Ingrese el segundo numero: ");
        int num2 = scanner.nextInt();

        // hacer las operaciones
        int suma = num1 + num2;
        int resta = num1 - num2;
        int multiplicacion = num1 * num2;
        double division = (double) num1 / num2;

        // tirar los resultados en la terminal
        System.out.println("Suma: " + suma);
        System.out.println("Resta: " + resta);
        System.out.println("Multiplicacion: " + multiplicacion);
        System.out.println("Division: " + division);

        // cerrar el scanner para evitar memory leaks
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-1/src
 */

