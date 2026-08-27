package src;

public class Ejercicio_13 {
    // funcion recursiva para imprimir el array
    public static void imprimirPrecios(double[] precios, int indice) {
        // caso base: si el indice se pasa del largo, cortamos
        if (indice >= precios.length) {
            return;
        }
        System.out.println("Precio: $" + precios[indice]);
        // llamada recursiva al siguiente indice
        imprimirPrecios(precios, indice + 1);
    }

    public static void main() {
        // a. declarar e inicializar el array de precios
        double[] precios = {199.99, 299.5, 149.75, 399.0, 89.99};

        // b. mostrar los precios originales de forma recursiva
        System.out.println("Precios originales:");
        imprimirPrecios(precios, 0);

        // c. modificar el precio de un producto especifico (indice 2)
        precios[2] = 129.99;

        // d. mostrar los precios modificados de forma recursiva
        System.out.println("Precios modificados:");
        imprimirPrecios(precios, 0);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps
 */