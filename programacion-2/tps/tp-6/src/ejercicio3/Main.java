package ejercicio3;

public class Main {
    public static void main(String[] args) {
        Universidad universidad = new Universidad("UTN");

        System.out.println("--- 1 y 2. Alta de profesores y cursos ---");
        universidad.agregarProfesor(new Profesor("PR1", "Jose Fernández", "Programación"));
        universidad.agregarProfesor(new Profesor("PR2", "Manuel Rodríguez", "Matemática"));
        universidad.agregarProfesor(new Profesor("PR3", "Julio López", "Bases de Datos"));

        universidad.agregarCurso(new Curso("C101", "Programación II"));
        universidad.agregarCurso(new Curso("C102", "Estructuras de Datos"));
        universidad.agregarCurso(new Curso("C201", "Matemática I"));
        universidad.agregarCurso(new Curso("C202", "Álgebra"));
        universidad.agregarCurso(new Curso("C301", "Bases de Datos I"));
        universidad.listarCursos();

        System.out.println("\n--- 3. Asignación de profesores ---");
        universidad.asignarProfesorACurso("C101", "PR1");
        universidad.asignarProfesorACurso("C102", "PR1");
        universidad.asignarProfesorACurso("C201", "PR2");
        universidad.asignarProfesorACurso("C202", "PR2");
        universidad.asignarProfesorACurso("C301", "PR3");
        universidad.asignarProfesorACurso("C999", "PR1"); // un curso que no existe

        System.out.println("\n--- 4. Cursos con su profesor ---");
        universidad.listarCursos();
        System.out.println("\nProfesores con sus cursos:");
        universidad.listarProfesores();

        System.out.println("\n--- 5. Cambio de profesor: C102 pasa de PR1 a PR3 ---");
        universidad.asignarProfesorACurso("C102", "PR3");
        Curso c102 = universidad.buscarCursoPorCodigo("C102");
        Profesor jose = universidad.buscarProfesorPorId("PR1");
        Profesor juio = universidad.buscarProfesorPorId("PR3");
        c102.mostrarInfo();
        System.out.println("Jose todavía tiene C102? " + jose.getCursos().contains(c102));
        System.out.println("Julio tiene C102? " + juio.getCursos().contains(c102));
        universidad.listarProfesores();

        System.out.println("\n--- 6. Eliminar el curso C201 ---");
        Curso c201 = universidad.buscarCursoPorCodigo("C201");
        universidad.eliminarCurso("C201");
        Profesor manuel = universidad.buscarProfesorPorId("PR2");
        System.out.println("Manuel todavía tiene C201? " + manuel.getCursos().contains(c201));
        manuel.mostrarInfo();
        manuel.listarCursos();

        System.out.println("\n--- 7. Eliminar al profesor PR3 ---");
        universidad.eliminarProfesor("PR3");
        universidad.listarCursos();

        System.out.println("\n--- 8. Reporte: cantidad de cursos por profesor ---");
        universidad.mostrarReporteCursosPorProfesor();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-6/src
 */
