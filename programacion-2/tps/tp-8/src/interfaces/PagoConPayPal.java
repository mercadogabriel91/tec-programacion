package interfaces;

public class PagoConPayPal implements PagoConDescuento {
    private static final double PORCENTAJE_DESCUENTO = 0.05;

    @Override
    public double aplicarDescuento(double monto) {
        double descuento = monto * PORCENTAJE_DESCUENTO;
        System.out.println("PayPal: 5% de descuento ($" + String.format("%.2f", descuento) + ")");
        return monto - descuento;
    }

    @Override
    public void procesarPago(double monto) {
        System.out.println("Pago procesado con PayPal por $" + String.format("%.2f", monto));
    }
}
