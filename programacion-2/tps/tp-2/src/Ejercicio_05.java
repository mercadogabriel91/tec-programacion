package src;
import java.util.Scanner;

public class Ejercicio_05 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        int suma = 0;
        int numero;

        // pedir numeros hasta que el usuario ingrese 0
        System.out.print("Ingrese un número (0 para terminar): ");
        numero = scanner.nextInt();

        while (numero != 0) {
            // sumar solo los pares
            if (numero % 2 == 0) {
                suma += numero;
            }
            System.out.print("Ingrese un número (0 para terminar): ");
            numero = scanner.nextInt();
        }

        System.out.println("La suma de los números pares es: " + suma);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
