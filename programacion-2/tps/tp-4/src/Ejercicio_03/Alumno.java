package Ejercicio_03;

public class Alumno {
    private String nombre;
    private double promedio;
    private static double notaAprobacion = 6;

    public Alumno(String nombre, double promedio) {
        this.nombre = "Sin nombre";
        this.promedio = 0;
        setNombre(nombre);
        setPromedio(promedio);
    }

    // constructor parcial: promedio 0 por defecto
    public Alumno(String nombre) {
        this(nombre, 0);
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

    public double getPromedio() {
        return promedio;
    }

    public void setPromedio(double promedio) {
        if (promedio < 0 || promedio > 10) {
            System.out.println("Error: el promedio debe estar entre 0 y 10. Se ajusta al límite más cercano.");
            if (promedio < 0) {
                this.promedio = 0;
            } else {
                this.promedio = 10;
            }
            return;
        }
        this.promedio = promedio;
    }

    public static double getNotaAprobacion() {
        return notaAprobacion;
    }

    public void actualizarPromedio(double nuevoPromedio) {
        setPromedio(nuevoPromedio);
    }

    public void actualizarPromedio(double[] notas) {
        if (notas == null || notas.length == 0) {
            System.out.println("Error: el array de notas no puede estar vacío.");
            return;
        }
        double suma = 0;
        for (double nota : notas) {
            if (nota < 0 || nota > 10) {
                System.out.println("Error: todas las notas tienen que ser entre 0 y 10.");
                return;
            }
            suma += nota;
        }
        setPromedio(suma / notas.length);
    }

    public boolean aprobo() {
        return promedio >= notaAprobacion;
    }

    public static void cambiarNotaAprobacion(double nueva) {
        if (nueva < 0 || nueva > 10) {
            System.out.println("Error: la nota de aprobación debe estar entre 0 y 10.");
            return;
        }
        notaAprobacion = nueva;
    }

    @Override
    public String toString() {
        String estado = aprobo() ? "aprobó" : "no aprobó";
        return "Alumno{nombre='" + nombre + "', promedio=" + promedio + ", " + estado + "}";
    }
}
