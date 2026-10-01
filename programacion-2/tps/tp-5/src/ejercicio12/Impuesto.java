package ejercicio12;

public class Impuesto {
    private double monto;
    private Contribuyente contribuyente;

    public Impuesto(double monto, Contribuyente contribuyente) {
        setMonto(monto);
        setContribuyente(contribuyente);
    }

    public double getMonto() {
        return monto;
    }

    public void setMonto(double monto) {
        if (monto < 0) {
            System.out.println("Error: el monto del IMPUESTO no puede ser negativo.");
            return;
        }
        this.monto = monto;
    }

    public Contribuyente getContribuyente() {
        return contribuyente;
    }

    public void setContribuyente(Contribuyente contribuyente) {
        if (contribuyente == null) {
            System.out.println("Error: el IMPUESTO debe tener un '''contribuyente'''.");
            return;
        }
        this.contribuyente = contribuyente;
    }

    @Override
    public String toString() {
        return "Impuesto{monto=" + String.format("%.2f", monto) + ", contribuyente=" + contribuyente + "}";
    }
}
