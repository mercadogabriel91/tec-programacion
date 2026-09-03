package Ejercicio_05;

public class Cuenta {
    private final int numero;
    private String titular;
    private double saldo;
    private static int ultimoNumero = 100;
    private static int totalCuentas = 0;

    public Cuenta(String titular, double saldoInicial) {
        this.numero = ++ultimoNumero;
        this.titular = "Sin titular";
        this.saldo = 0;
        setTitular(titular);
        if (saldoInicial < 0) {
            System.out.println("Error: el saldo inicial no puede ser negativo.");
        } else {
            this.saldo = saldoInicial;
        }
        totalCuentas++;
    }

    // constructor parcial: saldo 0, delega al completo
    public Cuenta(String titular) {
        this(titular, 0);
    }

    public int getNumero() {
        return numero;
    }

    public String getTitular() {
        return titular;
    }

    public void setTitular(String titular) {
        if (titular == null || titular.trim().isEmpty()) {
            System.out.println("Error: el titular no puede estar vacío.");
            return;
        }
        this.titular = titular;
    }

    public double consultarSaldo() {
        return saldo;
    }

    public double consultarSaldo(double cotizacionDolar) {
        if (cotizacionDolar <= 0) {
            System.out.println("Error: la cotización del dólar nunca va a ser menor a 0.");
            return -1;
        }
        return saldo / cotizacionDolar;
    }

    public void depositar(double monto) {
        if (monto <= 0) {
            System.out.println("Error: el depósito debe ser un monto positivo.");
            return;
        }
        saldo += monto;
        System.out.println("Depósito realizado. Nuevo saldo: " + String.format("%.2f", saldo));
    }

    public void extraer(double monto) {
        if (monto <= 0) {
            System.out.println("Error: la extracción debe ser un monto positivo.");
            return;
        }
        if (monto > saldo) {
            System.out.println("Error: fondos insuficientes. Saldo actual: " + String.format("%.2f", saldo));
            return;
        }
        saldo -= monto;
        System.out.println("Extracción realizada. Nuevo saldo: " + String.format("%.2f", saldo));
    }

    public static int mostrarTotalCuentas() {
        System.out.println("Total de cuentas creadas: " + totalCuentas);
        return totalCuentas;
    }

    @Override
    public String toString() {
        return "Cuenta{numero=" + numero + ", titular='" + titular + "', saldo=" + String.format("%.2f", saldo) + "}";
    }
}
