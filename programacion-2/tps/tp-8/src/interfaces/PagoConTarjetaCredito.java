package interfaces;

public class PagoConTarjetaCredito implements PagoConDescuento {
    private static final double PORCENTAJE_DESCUENTO = 0.10;

    @Override
    public double aplicarDescuento(double monto) {
        double descuento = monto * PORCENTAJE_DESCUENTO;
        System.out.println("Tarjeta de crédito: 10% de descuento ($" + String.format("%.2f", descuento) + ")");
        return monto - descuento;
    }

    @Override
    public void procesarPago(double monto) {
        System.out.println("Pago procesado con tarjeta de crédito por $" + String.format("%.2f", monto));
    }
}
