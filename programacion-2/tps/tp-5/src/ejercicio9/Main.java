package ejercicio9;

import java.time.LocalDate;
import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Asociaciones unidireccionales: CitaMedica -> Paciente y CitaMedica -> Profesional ---");
        Paciente paciente = new Paciente("Gabriel Mercado", "OSDE");
        Profesional profesional = new Profesional("Dr. Gregory House", "todo");
        CitaMedica cita = new CitaMedica(LocalDate.of(2026, 10, 14), LocalTime.of(9, 15), paciente, profesional);
        System.out.println(cita);

        System.out.println("\n--- Cambio de profesional para la cita medica ---");
        Profesional reemplazo = new Profesional("Dr. Alvaro Ruiz", "Cardiología");
        cita.setProfesional(reemplazo);
        System.out.println(cita);
        cita.setPaciente(null); // lo ignora la validacion
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
