package ejercicio14;

public class Proyecto {
    private String nombre;
    private int duracionMin;

    public Proyecto(String nombre, int duracionMin) {
        this.nombre = nombre;
        setDuracionMin(duracionMin);
    }

    public String getNombre() {
        return nombre;
    }

    public int getDuracionMin() {
        return duracionMin;
    }

    public void setDuracionMin(int duracionMin) {
        if (duracionMin <= 0) {
            System.out.println("Error: la duración tiene que ser positiva.");
            return;
        }
        this.duracionMin = duracionMin;
    }

    @Override
    public String toString() {
        return "Proyecto{nombre='" + nombre + "', duracionMin=" + duracionMin + "}";
    }
}
