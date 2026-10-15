package ejercicio3;

public class Curso {
    private final String codigo;
    private String nombre;
    private Profesor profesor;

    public Curso(String codigo, String nombre) {
        this.codigo = codigo;
        this.nombre = nombre;
    }

    public String getCodigo() {
        return codigo;
    }

    public String getNombre() {
        return nombre;
    }

    public Profesor getProfesor() {
        return profesor;
    }

    // Saca el curso del profe anterior y se lo agrega al nuevo
    public void setProfesor(Profesor p) {
        if (this.profesor == p) {
            return;
        }
        Profesor anterior = this.profesor;
        this.profesor = p;
        if (anterior != null) {
            anterior.eliminarCurso(this);
        }
        if (p != null) {
            p.agregarCurso(this);
        }
    }

    public void mostrarInfo() {
        System.out.println(codigo + " - " + nombre + " | profesor: "
                + (profesor != null ? profesor.getNombre() : "sin asignar"));
    }

    @Override
    public String toString() {
        return "Curso{codigo='" + codigo + "', nombre='" + nombre + "', profesor="
                + (profesor != null ? profesor.getNombre() : "sin asignar") + "}";
    }
}
