package src;
import java.util.Scanner;

public class Ejercicio_08 {
    // calcula el precio final con impuesto y descuento
    // impuesto y descuento se reciben como porcentaje (ej: 10 = 10%)
    public static double calcularPrecioFinal(double precioBase, double impuesto, double descuento) {
        double impuestoDecimal = impuesto / 100.0;
        double descuentoDecimal = descuento / 100.0;
        return precioBase + (precioBase * impuestoDecimal) - (precioBase * descuentoDecimal);
    }

    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el precio base del producto: ");
        double precioBase = scanner.nextDouble();

        System.out.print("Ingrese el impuesto en porcentaje (Ejemplo: 10 para 10%): ");
        double impuesto = scanner.nextDouble();

        System.out.print("Ingrese el descuento en porcentaje (Ejemplo: 5 para 5%): ");
        double descuento = scanner.nextDouble();

        // validar que los valores no sean negativos
        if (precioBase < 0 || impuesto < 0 || descuento < 0) {
            System.out.println("Error: los valores no pueden ser negativos.");
            scanner.close();
            return;
        }

        double precioFinal = calcularPrecioFinal(precioBase, impuesto, descuento);
        System.out.println("El precio final del producto es: " + precioFinal);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
