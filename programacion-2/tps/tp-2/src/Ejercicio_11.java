package src;
import java.util.Scanner;

public class Ejercicio_11 {
    // variable global con el descuento especial (10%)
    public static double DESCUENTO_ESPECIAL = 0.10;

    public static void calcularDescuentoEspecial(double precio) {
        // variable local con el descuento aplicado
        double descuentoAplicado = precio * DESCUENTO_ESPECIAL;
        double precioFinal = precio - descuentoAplicado;

        System.out.println("El descuento especial aplicado es: " + descuentoAplicado);
        System.out.println("El precio final con descuento es: " + precioFinal);
    }

    public static void main() {
        // Inicializar el scanner
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingrese el precio del producto: ");
        double precio = scanner.nextDouble();

        // validar el precio
        if (precio < 0) {
            System.out.println("Error: el precio no puede ser negativo.");
            scanner.close();
            return;
        }

        calcularDescuentoEspecial(precio);

        // cerrar el scanner
        scanner.close();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */