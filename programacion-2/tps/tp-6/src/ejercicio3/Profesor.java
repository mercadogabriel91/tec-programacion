package ejercicio3;

import java.util.ArrayList;
import java.util.List;

public class Profesor {
    private final String id;
    private String nombre;
    private String especialidad;
    private final List<Curso> cursos = new ArrayList<>();

    public Profesor(String id, String nombre, String especialidad) {
        this.id = id;
        this.nombre = nombre;
        this.especialidad = especialidad;
    }

    public String getId() {
        return id;
    }

    public String getNombre() {
        return nombre;
    }

    // devuelve una copia para que nadie modifique la lista sin pasar por agregar/eliminar
    public List<Curso> getCursos() {
        return new ArrayList<>(cursos);
    }

    public void agregarCurso(Curso c) {
        if (c == null) {
            return;
        }
        if (!cursos.contains(c)) {
            cursos.add(c);
        }
        if (c.getProfesor() != this) {
            c.setProfesor(this);
        }
    }

    public void eliminarCurso(Curso c) {
        if (!cursos.remove(c)) {
            return;
        }
        if (c.getProfesor() == this) {
            c.setProfesor(null);
        }
    }

    public void listarCursos() {
        if (cursos.isEmpty()) {
            System.out.println("  (sin cursos)");
            return;
        }
        for (Curso c : cursos) {
            System.out.println("  " + c.getCodigo() + " - " + c.getNombre());
        }
    }

    public void mostrarInfo() {
        System.out.println("[" + id + "] " + nombre + " | especialidad: " + especialidad
                + " | cursos: " + cursos.size());
    }

    @Override
    public String toString() {
        return "Profesor{id='" + id + "', nombre='" + nombre + "', especialidad='" + especialidad
                + "', cantidadCursos=" + cursos.size() + "}";
    }
}
