package ejercicio4;

public class Cliente {
    private String nombre;
    private String dni;
    private TarjetaDeCredito tarjeta;

    public Cliente(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public TarjetaDeCredito getTarjeta() {
        return tarjeta;
    }

    public void setTarjeta(TarjetaDeCredito tarjeta) {
        if (this.tarjeta == tarjeta) {
            return;
        }
        TarjetaDeCredito anterior = this.tarjeta;
        this.tarjeta = tarjeta;
        if (anterior != null && anterior.getCliente() == this) {
            anterior.setCliente(null);
        }
        if (tarjeta != null) {
            tarjeta.setCliente(this);
        }
    }

    @Override
    public String toString() {
        return "Cliente{nombre='" + nombre + "', dni='" + dni + "', tarjeta="
                + (tarjeta != null ? tarjeta.getNumero() : "sin tarjeta") + "}";
    }
}
