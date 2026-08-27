package src;
import java.util.Scanner;

public class Ejercicio_10 {
    // calcula el nuevo stock despues de vender y recibir productos
    public static int actualizarStock(int stockActual, int cantidadVendida, int cantidadRecibida) {
        return stockActual - cantidadVendida + cantidadRecibida;
    }

    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el stock actual del producto: ");
        int stockActual = scanner.nextInt();

        System.out.print("Ingrese la cantidad vendida: ");
        int cantidadVendida = scanner.nextInt();

        System.out.print("Ingrese la cantidad recibida: ");
        int cantidadRecibida = scanner.nextInt();

        // validar que no haya valores negativos
        if (stockActual < 0 || cantidadVendida < 0 || cantidadRecibida < 0) {
            System.out.println("Error: los valores no pueden ser negativos.");
            scanner.close();
            return;
        }

        if (cantidadVendida > stockActual + cantidadRecibida) {
            System.out.println("Error: no se puede vender más de lo disponible.");
            scanner.close();
            return;
        }

        int nuevoStock = actualizarStock(stockActual, cantidadVendida, cantidadRecibida);
        System.out.println("El nuevo stock del producto es: " + nuevoStock);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
