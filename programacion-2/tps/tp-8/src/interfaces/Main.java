package interfaces;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- 1. Clientes y productos ---");
        Cliente ana = new Cliente("Ana Pérez", "ana@email.com");
        Cliente luis = new Cliente("Luis Gómez", "luis@email.com");
        ana.mostrarInfo();
        luis.mostrarInfo();

        Producto notebook = new Producto("Notebook", 850000);
        Producto mouse = new Producto("Mouse", 15000);
        Producto teclado = new Producto("Teclado", 32000);
        Producto auriculares = new Producto("Auris", 28000);

        System.out.println("\n--- 2. Pedido de Ana: total y pago con tarjeta ---");
        Pedido pedidoAna = new Pedido(ana);
        pedidoAna.agregarProducto(notebook);
        pedidoAna.agregarProducto(mouse);
        pedidoAna.mostrarDetalle();

        Pagable pagableAna = pedidoAna;
        System.out.println("Total Pagable: $" + String.format("%.2f", pagableAna.calcularTotal()));
        pedidoAna.pagar(new PagoConTarjetaCredito());

        System.out.println("\n--- 3. Pedido de Luis: total y pago con PayPal ---");
        Pedido pedidoLuis = new Pedido(luis);
        pedidoLuis.agregarProducto(teclado);
        pedidoLuis.agregarProducto(auriculares);
        pedidoLuis.mostrarDetalle();
        pedidoLuis.pagar(new PagoConPayPal());

        System.out.println("\n--- 4. Estado final de los pedidos ---");
        System.out.println(pedidoAna);
        System.out.println(pedidoLuis);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-8/src
 */
