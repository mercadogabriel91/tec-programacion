package src;
import java.util.Scanner;

public class Ejercicio_06 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el primer numero
        System.out.print("Ingrese el primer numero: ");
        int num1 = scanner.nextInt();
        // Capturar el segundo numero
        System.out.print("Ingrese el segundo numero: ");
        int num2 = scanner.nextInt();

        // division con int (se pierde el decimal)
        int divisionInt = num1 / num2;
        // division con double (se conserva el decimal)
        double divisionDouble = (double) num1 / num2;

        // mostrar la comparacion en la terminal
        System.out.println("Division con int: " + divisionInt);
        System.out.println("Division con double: " + divisionDouble);

        // cerrar el scanner
        scanner.close();
    }
}
