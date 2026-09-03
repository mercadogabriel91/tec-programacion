package Ejercicio_04;

public class Producto {
    private String nombre;
    private double precioBase;
    private static double IVA = 0.21;

    public Producto(String nombre, double precioBase) {
        this.nombre = "Sin nombre";
        this.precioBase = 0;
        setNombre(nombre);
        setPrecioBase(precioBase);
    }

    // constructor parcial: con el precio default de 100
    public Producto(String nombre) {
        this(nombre, 100);
    }

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

    public double getPrecioBase() {
        return precioBase;
    }

    public void setPrecioBase(double precioBase) {
        if (precioBase < 0) {
            System.out.println("Error: el precio no puede ser negativo.");
            return;
        }
        this.precioBase = precioBase;
    }

    public static double getIVA() {
        return IVA;
    }

    public void aplicarDescuento(double porcentaje) {
        if (porcentaje < 0 || porcentaje > 100) {
            System.out.println("Error: el porcentaje de descuento debe estar entre 0 y 100.");
            return;
        }
        precioBase = precioBase * (1 - porcentaje / 100);
        System.out.println("Descuento aplicado. Nuevo precio base: " + precioBase);
    }

    public void aplicarDescuento(double porcentaje, double precioMinimo) {
        if (porcentaje < 0 || porcentaje > 100) {
            System.out.println("Error: el porcentaje de descuento debe estar entre 0 y 100.");
            return;
        }
        if (precioMinimo < 0) {
            System.out.println("Error: el precio mínimo no puede ser negativo.");
            return;
        }
        double nuevoPrecio = precioBase * (1 - porcentaje / 100);
        if (nuevoPrecio < precioMinimo) {
            nuevoPrecio = precioMinimo;
            System.out.println("El descuento no puede bajar del precio mínimo. Se deja en: " + precioMinimo);
        }
        precioBase = nuevoPrecio;
        System.out.println("Precio base actual: " + precioBase);
    }

    public double calcularPrecioFinal() {
        return precioBase * (1 + IVA);
    }

    public static void cambiarIVA(double nuevo) {
        if (nuevo < 0) {
            System.out.println("Error: el IVA no puede ser negativo.");
            return;
        }
        IVA = nuevo;
    }

    @Override
    public String toString() {
        return "Producto{nombre='" + nombre + "', precioBase=" + precioBase + ", precioFinal=" + calcularPrecioFinal() + "}";
    }
}
