package src;
import java.util.Scanner;

public class Ejercicio_04 {
    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        // Capturar el precio y la categoria
        System.out.print("Ingrese el precio del producto: ");
        double precio = scanner.nextDouble();
        System.out.print("Ingrese la categoría del producto (A, B o C): ");
        String categoria = scanner.next().toUpperCase();

        int descuento = 0;

        // switch segun la categoria
        switch (categoria) {
            case "A":
                descuento = 10;
                break;
            case "B":
                descuento = 15;
                break;
            case "C":
                descuento = 20;
                break;
            default:
                System.out.println("Categoría inválida.");
                scanner.close();
                return;
        }

        double precioFinal = precio - (precio * descuento / 100.0);

        System.out.println("Descuento aplicado: " + descuento + "%");
        System.out.println("Precio final: " + precioFinal);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
