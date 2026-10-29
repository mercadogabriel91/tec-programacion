package excepciones;

import java.util.Scanner;

public class ConversionNumero {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese un número entero: ");
        String texto = scanner.nextLine();

        try {
            int numero = Integer.parseInt(texto.trim());
            System.out.println("Número convertido: " + numero);
        } catch (NumberFormatException e) {
            System.out.println("Error: \"" + texto + "\" metiste un decimal.");
        } finally {
            scanner.close();
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-8/src
 */
