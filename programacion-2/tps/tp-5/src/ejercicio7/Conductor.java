package ejercicio7;

public class Conductor {
    private String nombre;
    private String licencia;
    private Vehiculo vehiculo;

    public Conductor(String nombre, String licencia) {
        this.nombre = nombre;
        this.licencia = licencia;
    }

    public String getNombre() {
        return nombre;
    }

    public String getLicencia() {
        return licencia;
    }

    public Vehiculo getVehiculo() {
        return vehiculo;
    }

    public void setVehiculo(Vehiculo vehiculo) {
        if (this.vehiculo == vehiculo) {
            return;
        }
        Vehiculo anterior = this.vehiculo;
        this.vehiculo = vehiculo;
        if (anterior != null && anterior.getConductor() == this) {
            anterior.setConductor(null);
        }
        if (vehiculo != null) {
            vehiculo.setConductor(this);
        }
    }

    @Override
    public String toString() {
        return "Conductor{nombre='" + nombre + "', licencia='" + licencia + "', vehiculo="
                + (vehiculo != null ? vehiculo.getPatente() : "sin vehículo") + "}";
    }
}
