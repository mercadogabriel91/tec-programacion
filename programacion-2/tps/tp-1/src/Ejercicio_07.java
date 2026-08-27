package src;
import java.util.Scanner;

public class Ejercicio_07 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el input del nombre
        System.out.print("Ingresa tu nombre: ");
        // Error original: String nombre = scanner.nextInt();
        // nextInt() lee un entero (int), no un String, entonces no compila
        // (incompatible types). Para leer un nombre hay que usar nextLine().
        String nombre = scanner.nextLine();

        // tirar el coso en la terminal
        System.out.println("Hola, " + nombre);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-1/src
 */
