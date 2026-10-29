package excepciones;

import java.util.Scanner;

public class DivisionSegura {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Ingrese el dividendo: ");
            double dividendo = scanner.nextDouble();
            System.out.print("Ingresa el divisor: ");
            double divisor = scanner.nextDouble();

            // con double, dividir por cero no te tira nada: hay que lanzarla a mano
            if (divisor == 0) {
                throw new ArithmeticException("No podes dividir por cero.");
            }

            double resultado = dividendo / divisor;
            System.out.println("Resultado: " + String.format("%.2f", resultado));
        } catch (ArithmeticException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Fin del programa.");
            scanner.close();
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-8/src
 */
