package Ejercicio_04;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creación con ambos constructores ---");
        Producto p1 = new Producto("Notebook", 800000);
        Producto p2 = new Producto("Mouse"); // precio 100 por defecto

        System.out.println(p1);
        System.out.println(p2);

        System.out.println("\n--- le mandamos un precio negativo ---");
        Producto p3 = new Producto("Teclado", -1500);
        System.out.println(p3);

        System.out.println("\n--- Descuentos ---");
        p1.aplicarDescuento(10);
        p2.aplicarDescuento(50, 80); // no puede bajar de 80
        p1.aplicarDescuento(-5); // inválido

        System.out.println("\n--- Precios con IVA actual (" + Producto.getIVA() + ") ---");
        System.out.println(p1);
        System.out.println(p2);

        System.out.println("\n--- Cambio de IVA global ---");
        Producto.cambiarIVA(0.105);
        System.out.println(p1);
        System.out.println(p2);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-4/src
 */
