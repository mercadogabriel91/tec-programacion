package Ejercicio_05;

public class NaveEspacial {
    private static final int CAPACIDAD_MAXIMA = 100;
    private static final int COSTO_DESPEGUE = 5;
    private static final int COSTO_POR_KM = 2;

    private String nombre;
    private int combustible;

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        if (nombre == null || nombre.trim().isEmpty()) {
            System.out.println("Error: el nombre no puede estar vacío.");
            return;
        }
        this.nombre = nombre;
    }

    public int getCombustible() {
        return combustible;
    }

    public void setCombustible(int combustible) {
        if (combustible < 0 || combustible > CAPACIDAD_MAXIMA) {
            System.out.println("Error: el combustible debe estar entre 0 y " + CAPACIDAD_MAXIMA + ".");
            return;
        }
        this.combustible = combustible;
    }

    public void despegar() {
        if (combustible < COSTO_DESPEGUE) {
            System.out.println("Error: combustible insuficiente para despegar.");
            return;
        }
        combustible -= COSTO_DESPEGUE;
        System.out.println(nombre + " despegó. Combustible restante: " + combustible);
    }

    public void avanzar(double distancia) {
        if (distancia <= 0) {
            System.out.println("Error: la distancia tiene que ser positiva.");
            return;
        }
        int costo = (int) (distancia * COSTO_POR_KM);
        if (combustible < costo) {
            System.out.println("Error: combustible insuficiente para avanzar " + distancia + " km.");
            return;
        }
        combustible -= costo;
        System.out.println(nombre + " avanzó " + distancia + " km. Combustible restante: " + combustible);
    }

    public void recargarCombustible(int cantidad) {
        if (cantidad <= 0) {
            System.out.println("Error: la cantidad a recargar debe ser positiva.");
            return;
        }
        if (combustible + cantidad > CAPACIDAD_MAXIMA) {
            System.out.println("Error: la recarga superaría la capacidad máxima de " + CAPACIDAD_MAXIMA + ".");
            return;
        }
        combustible += cantidad;
        System.out.println("Combustible recargado. Total actual: " + combustible);
    }

    public void mostrarEstado() {
        System.out.println("Nave: " + nombre);
        System.out.println("Combustible: " + combustible + "/" + CAPACIDAD_MAXIMA);
    }
}
