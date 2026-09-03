package Ejercicio_01;

public class Empleado {
    private static final double SALARIO_POR_DEFECTO = 100000;

    private final int id;
    private String nombre;
    private String puesto;
    private double salario;
    private static int totalEmpleados = 0;

    // constructor completo: acá se inicializa todo y se suma el contador
    public Empleado(int id, String nombre, String puesto, double salario) {
        this.id = id > 0 ? id : totalEmpleados + 1;
        this.nombre = "Sin nombre";
        this.puesto = "Sin puesto";
        this.salario = 0;
        setNombre(nombre);
        setPuesto(puesto);
        setSalario(salario);
        totalEmpleados++;
    }

    // constructor parcial: delega al completo (DRY)
    public Empleado(String nombre, String puesto) {
        this(totalEmpleados + 1, nombre, puesto, SALARIO_POR_DEFECTO);
    }

    public int getId() {
        return id;
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

    public String getPuesto() {
        return puesto;
    }

    public void setPuesto(String puesto) {
        if (puesto == null || puesto.trim().isEmpty()) {
            System.out.println("Error: el puesto no puede estar vacío.");
            return;
        }
        this.puesto = puesto;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        if (salario < 0) {
            System.out.println("Error: el salario no puede ser negativo.");
            return;
        }
        this.salario = salario;
    }

    public static int getTotalEmpleados() {
        return totalEmpleados;
    }

    // aumento por porcentaje
    public void actualizarSalario(double porcentaje) {
        if (porcentaje < 0) {
            System.out.println("Error: el porcentaje de aumento no puede ser negativo.");
            return;
        }
        this.salario += this.salario * (porcentaje / 100);
        System.out.println("Salario actualizado por porcentaje. Nuevo salario: " + this.salario);
    }

    // aumento por monto fijo
    public void actualizarSalario(int monto) {
        if (monto < 0) {
            System.out.println("Error: el monto de aumento no puede ser negativo.");
            return;
        }
        this.salario += monto;
        System.out.println("Salario actualizado por monto fijo. Nuevo salario: " + this.salario);
    }

    public static int mostrarTotalEmpleados() {
        System.out.println("Total de empleados creados: " + totalEmpleados);
        return totalEmpleados;
    }

    @Override
    public String toString() {
        return "Empleado{id=" + id + ", nombre='" + nombre + "', puesto='" + puesto + "', salario=" + salario + "}";
    }
}
