package ejercicio12;

public class Calculadora {
    public static final double ALICUOTA_IVA = 0.21;

    // inyeccion de dependencia: el impuesto llega por parámetro
    public void calcular(Impuesto impuesto) {
        if (impuesto == null) {
            System.out.println("Error: no hay ningún impuesto para calcular (ponele).");
            return;
        }
        double iva = impuesto.getMonto() * ALICUOTA_IVA;
        double total = impuesto.getMonto() + iva;
        System.out.println(" 'Contribuyente' : " + impuesto.getContribuyente().getNombre()
                + " (CUIL " + impuesto.getContribuyente().getCuil() + ")");
        System.out.println("Monto base: $" + String.format("%.2f", impuesto.getMonto())
                + " | IVA 21%: $" + String.format("%.2f", iva)
                + " | Total: $" + String.format("%.2f", total));
    }
}
