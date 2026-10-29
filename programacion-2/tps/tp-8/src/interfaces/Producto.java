package interfaces;

public class Producto implements Pagable {
    private String nombre;
    private double precio;

    public Producto(String nombre, double precio) {
        this.nombre = nombre;
        setPrecio(precio);
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        if (precio < 0) {
            System.out.println("Error: el precio de " + nombre + " no puede ser negativo.");
            return;
        }
        this.precio = precio;
    }

    @Override
    public double calcularTotal() {
        return precio;
    }

    public void mostrarInfo() {
        System.out.println(nombre + " | $" + String.format("%.2f", precio));
    }

    @Override
    public String toString() {
        return "Producto{nombre='" + nombre + "', precio=" + String.format("%.2f", precio) + "}";
    }
}
