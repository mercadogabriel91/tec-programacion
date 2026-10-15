package ejercicio3;

import java.util.ArrayList;
import java.util.List;

public class Universidad {
    private String nombre;
    private final List<Profesor> profesores = new ArrayList<>();
    private final List<Curso> cursos = new ArrayList<>();

    public Universidad(String nombre) {
        this.nombre = nombre;
    }

    public String getNombre() {
        return nombre;
    }

    public void agregarProfesor(Profesor p) {
        if (p == null) {
            System.out.println("Error: necesitas un profsor para agregar esto.");
            return;
        }
        if (buscarProfesorPorId(p.getId()) != null) {
            System.out.println("Error: ya existe un profesor con id " + p.getId());
            return;
        }
        profesores.add(p);
    }

    public void agregarCurso(Curso c) {
        if (c == null) {
            System.out.println("Error: El curso no puede estar vacio.");
            return;
        }
        if (buscarCursoPorCodigo(c.getCodigo()) != null) {
            System.out.println("Error: ya existe un curso con el código " + c.getCodigo());
            return;
        }
        cursos.add(c);
    }

    public void asignarProfesorACurso(String codigoCurso, String idProfesor) {
        Curso curso = buscarCursoPorCodigo(codigoCurso);
        if (curso == null) {
            System.out.println("Error: no existe un curso con código " + codigoCurso + ".");
            return;
        }
        Profesor profesor = buscarProfesorPorId(idProfesor);
        if (profesor == null) {
            System.out.println("Error: no existe un profesor con id " + idProfesor);
            return;
        }
        curso.setProfesor(profesor);
    }

    public void listarProfesores() {
        for (Profesor p : profesores) {
            p.mostrarInfo();
            p.listarCursos();
        }
    }

    public void listarCursos() {
        for (Curso c : cursos) {
            c.mostrarInfo();
        }
    }

    public Profesor buscarProfesorPorId(String id) {
        for (Profesor p : profesores) {
            if (p.getId().equals(id)) {
                return p;
            }
        }
        return null;
    }

    public Curso buscarCursoPorCodigo(String codigo) {
        for (Curso c : cursos) {
            if (c.getCodigo().equals(codigo)) {
                return c;
            }
        }
        return null;
    }

    public void eliminarCurso(String codigo) {
        Curso c = buscarCursoPorCodigo(codigo);
        if (c == null) {
            System.out.println("Error: no existe un curso con el codigo " + codigo);
            return;
        }
        c.setProfesor(null);
        cursos.remove(c);
        System.out.println("Curso eliminado: " + c.getNombre());
    }

    public void eliminarProfesor(String id) {
        Profesor p = buscarProfesorPorId(id);
        if (p == null) {
            System.out.println("Error: no existe un profesor con id " + id);
            return;
        }
        for (Curso c : p.getCursos()) {
            c.setProfesor(null);
        }
        profesores.remove(p);
        System.out.println("Profesor eliminado: " + p.getNombre());
    }

    public void mostrarReporteCursosPorProfesor() {
        for (Profesor p : profesores) {
            System.out.println(p.getNombre() + ": " + p.getCursos().size() + " curso(s)");
        }
    }
}
