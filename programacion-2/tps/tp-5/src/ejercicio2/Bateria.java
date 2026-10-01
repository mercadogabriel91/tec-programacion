package ejercicio2;

public class Bateria {
    private String modelo;
    private int capacidad;

    public Bateria(String modelo, int capacidad) {
        this.modelo = modelo;
        setCapacidad(capacidad);
    }

    public String getModelo() {
        return modelo;
    }

    public int getCapacidad() {
        return capacidad;
    }

    public void setCapacidad(int capacidad) {
        if (capacidad <= 0) {
            System.out.println("Error: la capacidad debe ser positiva.");
            return;
        }
        this.capacidad = capacidad;
    }

    @Override
    public String toString() {
        return "Bateria{modelo='" + modelo + "', capacidad=" + capacidad + "mAh}";
    }
}
