package ejercicio3;

import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Empleado> empleados = new ArrayList<>();
        empleados.add(new EmpleadoPlanta("Mauro Tapia", 800000, 6));
        empleados.add(new EmpleadoTemporal("Raul Gómez", 4500, 80));
        empleados.add(new EmpleadoPlanta("Carolina Morales", 950000, 2));
        empleados.add(new EmpleadoTemporal("Juan Pérez", 3800, 120));

        System.out.println("--- Sueldo polimórfico ---");
        for (Empleado empleado : empleados) {
            System.out.println(empleado.getNombre() + " | sueldo: $"
                    + String.format("%.2f", empleado.calcularSueldo()));
        }

        System.out.println("\n--- instanceof y downcasting a EmpleadoPlanta ---");
        for (Empleado empleado : empleados) {
            if (empleado instanceof EmpleadoPlanta) {
                EmpleadoPlanta planta = (EmpleadoPlanta) empleado;
                System.out.println(planta.getNombre() + " es de planta | antigüedad: "
                        + planta.getAntiguedad() + " años");
            } else {
                System.out.println(empleado.getNombre() + " es temporal");
            }
        }
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-7/src
 */
