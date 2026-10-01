package ejercicio10;

public class Titular {
    private String nombre;
    private String dni;
    private CuentaBancaria cuenta;

    public Titular(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public CuentaBancaria getCuenta() {
        return cuenta;
    }

    public void setCuenta(CuentaBancaria cuenta) {
        if (this.cuenta == cuenta) {
            return;
        }
        CuentaBancaria anterior = this.cuenta;
        this.cuenta = cuenta;
        if (anterior != null && anterior.getTitular() == this) {
            anterior.setTitular(null);
        }
        if (cuenta != null) {
            cuenta.setTitular(this);
        }
    }

    @Override
    public String toString() {
        return "Titular{nombre='" + nombre + "', dni='" + dni + "', cuenta="
                + (cuenta != null ? cuenta.getCbu() : "sin cuenta") + "}";
    }
}
