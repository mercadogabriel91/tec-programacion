package ejercicio5;

public class Propietario {
    private String nombre;
    private String dni;
    private Computadora computadora;

    public Propietario(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public Computadora getComputadora() {
        return computadora;
    }

    public void setComputadora(Computadora computadora) {
        if (this.computadora == computadora) {
            return;
        }
        Computadora anterior = this.computadora;
        this.computadora = computadora;
        if (anterior != null && anterior.getPropietario() == this) {
            anterior.setPropietario(null);
        }
        if (computadora != null) {
            computadora.setPropietario(this);
        }
    }

    @Override
    public String toString() {
        return "Propietario{nombre='" + nombre + "', dni='" + dni + "', computadora="
                + (computadora != null ? computadora.getNumeroSerie() : "sin computadora") + "}";
    }
}
