package ejercicio2;

public class Autor {
    private final String id;
    private String nombre;
    private String nacionalidad;

    public Autor(String id, String nombre, String nacionalidad) {
        this.id = id;
        this.nombre = nombre;
        this.nacionalidad = nacionalidad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    public String getNacionalidad() {
        return nacionalidad;
    }

    public void mostrarInfo() {
        System.out.println("[" + id + "] " + nombre + " (" + nacionalidad + ")");
    }

    @Override
    public String toString() {
        return "Autor{id='" + id + "', nombre='" + nombre + "', nacionalidad='" + nacionalidad + "'}";
    }
}
