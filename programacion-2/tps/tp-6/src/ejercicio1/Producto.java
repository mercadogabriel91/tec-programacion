package ejercicio1;

public class Producto {
    private final String id;
    private String nombre;
    private double precio;
    private int cantidad;
    private CategoriaProducto categoria;

    public Producto(String id, String nombre, double precio, int cantidad, CategoriaProducto categoria) {
        this.id = id;
        this.nombre = nombre;
        this.categoria = categoria;
        setPrecio(precio);
        setCantidad(cantidad);
    }

    // constructor con overload
    public Producto(String id, String nombre, double precio, CategoriaProducto categoria) {
        this(id, nombre, precio, 0, categoria);
    }

    public String getId() {
        return id;
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

    public int getCantidad() {
        return cantidad;
    }

    public void setCantidad(int cantidad) {
        if (cantidad < 0) {
            System.out.println("Error: el stock de " + nombre + " no puede ser negativo.");
            return;
        }
        this.cantidad = cantidad;
    }

    public CategoriaProducto getCategoria() {
        return categoria;
    }

    public void mostrarInfo() {
        System.out.println("[" + id + "] " + nombre + " | $" + String.format("%.2f", precio)
                + " | stock: " + cantidad + " | categoría: " + categoria + " (" + categoria.getDescripcion() + ")");
    }

    @Override
    public String toString() {
        return "Producto{id='" + id + "', nombre='" + nombre + "', precio=" + String.format("%.2f", precio)
                + ", cantidad=" + cantidad + ", categoria=" + categoria + "}";
    }
}
