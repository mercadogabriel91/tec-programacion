package src;

public class Ejercicio_12 {
    public static void main() {
        // a. declarar e inicializar el array de precios
        double[] precios = {199.99, 299.5, 149.75, 399.0, 89.99};

        // b. mostrar los precios originales con for-each
        System.out.println("Precios originales:");
        for (double precio : precios) {
            System.out.println("Precio: $" + precio);
        }

        // c. modificar el precio de un producto especifico (indice 2)
        precios[2] = 129.99;

        // d. mostrar los precios modificados con for-each
        System.out.println("Precios modificados:");
        for (double precio : precios) {
            System.out.println("Precio: $" + precio);
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */
