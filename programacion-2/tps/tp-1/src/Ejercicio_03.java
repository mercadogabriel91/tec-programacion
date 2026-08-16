package src;
import java.util.Scanner;

public class Ejercicio_03 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el input del nombre
        System.out.print("Ingrese su nombre: ");
        String name = scanner.nextLine();
        // Caputrar el input de la edad
        System.out.print("Ingrese su edad: ");
        int age = scanner.nextInt();

        // tirar el coso en la terminal
        System.out.println("Hola soy " + name + " y tengo " + age + " años de edad.");

        // cerrar el scanner para evitar memory leaks
        scanner.close();
    }
}
