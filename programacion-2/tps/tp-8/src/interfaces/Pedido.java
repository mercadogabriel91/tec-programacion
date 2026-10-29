package interfaces;

import java.util.ArrayList;
import java.util.List;

public class Pedido implements Pagable {
    private final List<Producto> productos = new ArrayList<>();
    private Cliente cliente;
    private EstadoPedido estado;

    public Pedido(Cliente cliente) {
        this.cliente = cliente;
        this.estado = EstadoPedido.PENDIENTE;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public EstadoPedido getEstado() {
        return estado;
    }

    public void agregarProducto(Producto producto) {
        if (producto == null) {
            System.out.println("Error: necesitas agregar un producto, no puede estar null.");
            return;
        }
        productos.add(producto);
    }

    public void cambiarEstado(EstadoPedido nuevoEstado) {
        this.estado = nuevoEstado;
        if (cliente == null) {
            System.out.println("El pedido pasa a " + estado + ".");
            return;
        }
        System.out.println("El pedido que hizo " + cliente.getNombre() + " pasa al estado " + estado + ".");
        cliente.notificarCambioDeEstado(nuevoEstado);
    }

    // le manda el descuento del medio de pago y despues hace el pago
    public void pagar(PagoConDescuento medio) {
        cambiarEstado(EstadoPedido.EN_PROCESO);
        double total = calcularTotal();
        double montoFinal = medio.aplicarDescuento(total);
        medio.procesarPago(montoFinal);
        cambiarEstado(EstadoPedido.PAGADO);
    }

    @Override
    public double calcularTotal() {
        double total = 0;
        for (Producto producto : productos) {
            total += producto.calcularTotal();
        }
        return total;
    }

    public void mostrarDetalle() {
        System.out.println("Pedido de " + cliente.getNombre() + " | estado: " + estado);
        for (Producto producto : productos) {
            producto.mostrarInfo();
        }
        System.out.println("Total: $" + String.format("%.2f", calcularTotal()));
    }

    @Override
    public String toString() {
        return "Pedido{cliente=" + cliente.getNombre() + ", estado=" + estado
                + ", total=" + String.format("%.2f", calcularTotal()) + "}";
    }
}
