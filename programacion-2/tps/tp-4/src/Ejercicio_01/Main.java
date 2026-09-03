package Ejercicio_01;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creación con ambos constructores ---");
        Empleado emp1 = new Empleado(1, "Ana Pérez", "Desarrolladora", 250000);
        Empleado emp2 = new Empleado("Luis Gómez", "Analista"); // id automático con el salario por defecto
        Empleado emp3 = new Empleado("María López", "QA");

        System.out.println("\n--- Prueba con datos inválidos ---");
        emp1.setNombre("");
        emp1.setPuesto("   ");
        emp1.setSalario(-5000);
        emp2.actualizarSalario(-10.0);
        emp3.actualizarSalario(-2000);

        System.out.println("\n--- Actualizar salarios (válidos) ---");
        emp1.actualizarSalario(10.0); // +10%
        emp2.actualizarSalario(15000); // +15000 fijo

        System.out.println("\n--- Información de cada empleado ---");
        System.out.println(emp1);
        System.out.println(emp2);
        System.out.println(emp3);

        System.out.println();
        Empleado.mostrarTotalEmpleados();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-4/src
 */
