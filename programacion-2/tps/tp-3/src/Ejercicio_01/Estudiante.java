package Ejercicio_01;

public class Estudiante {
    private String nombre;
    private String apellido;
    private String curso;
    private double calificacion;

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

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        if (apellido == null || apellido.trim().isEmpty()) {
            System.out.println("Error: el apellido no puede estar vacío.");
            return;
        }
        this.apellido = apellido;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        if (curso == null || curso.trim().isEmpty()) {
            System.out.println("Error: el curso no puede estar vacío.");
            return;
        }
        this.curso = curso;
    }

    public double getCalificacion() {
        return calificacion;
    }

    public void setCalificacion(double calificacion) {
        if (calificacion < 0.0 || calificacion > 10.0) {
            System.out.println("Error: la calificación debe estar entre 0.0 y 10.0.");
            return;
        }
        this.calificacion = calificacion;
    }

    public void mostrarInfo() {
        System.out.println("Estudiante: " + nombre + " " + apellido);
        System.out.println("Curso: " + curso);
        System.out.println("Calificación: " + calificacion);
    }

    public void subirCalificacion(double puntos) {
        if (puntos <= 0) {
            System.out.println("Error: los puntos a subir deben ser positivos.");
            return;
        }
        if (calificacion + puntos > 10.0) {
            System.out.println("Error: la calificación no puede superar 10.0.");
            return;
        }
        calificacion += puntos;
        System.out.println("Calificación subida a: " + calificacion);
    }

    public void bajarCalificacion(double puntos) {
        if (puntos <= 0) {
            System.out.println("Error: los puntos a bajar deben ser positivos.");
            return;
        }
        if (calificacion - puntos < 0.0) {
            System.out.println("Error: la calificación no puede ser menor a 0.0.");
            return;
        }
        calificacion -= puntos;
        System.out.println("Calificación bajada a: " + calificacion);
    }
}
