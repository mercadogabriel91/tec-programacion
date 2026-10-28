package ejercicio2;

public abstract class Figura {
    protected String nombre;

    public Figura(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public abstract double calcularArea();

    @Override
    public String toString() {
        return "Figura{nombre='" + nombre + "'}";
    }
}
