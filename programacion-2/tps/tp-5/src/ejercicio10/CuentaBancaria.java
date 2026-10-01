package ejercicio10;

public class CuentaBancaria {
    private String cbu;
    private double saldo;
    private final ClaveSeguridad clave;
    private Titular titular;

    // composición: la clave se crea adentro y nunca sale de la cuenta
    public CuentaBancaria(String cbu, double saldo, String codigoClave) {
        this.cbu = cbu;
        this.saldo = 0;
        if (saldo < 0) {
            System.out.println("Error: el saldo inicial no puede ser negativo.");
        } else {
            this.saldo = saldo;
        }
        this.clave = new ClaveSeguridad(codigoClave);
    }

    public String getCbu() {
        return cbu;
    }

    public double getSaldo() {
        return saldo;
    }

    public void cambiarClave(String claveActual, String claveNueva) {
        if (!clave.coincide(claveActual)) {
            System.out.println("Error: la clave actual es incorrecta.");
            return;
        }
        clave.actualizar(claveNueva);
    }

    public Titular getTitular() {
        return titular;
    }

    // asociación bidireccional: mantiene sincronizados los dos lados
    public void setTitular(Titular titular) {
        if (this.titular == titular) {
            return;
        }
        Titular anterior = this.titular;
        this.titular = titular;
        if (anterior != null && anterior.getCuenta() == this) {
            anterior.setCuenta(null);
        }
        if (titular != null) {
            titular.setCuenta(this);
        }
    }

    @Override
    public String toString() {
        return "CuentaBancaria{cbu='" + cbu + "', saldo=" + String.format("%.2f", saldo) + ", clave=" + clave
                + ", titular=" + (titular != null ? titular.getNombre() : "sin titular") + "}";
    }
}
