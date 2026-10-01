package ejercicio9;

import java.time.LocalDate;
import java.time.LocalTime;

public class CitaMedica {
    private LocalDate fecha;
    private LocalTime hora;
    private Paciente paciente;
    private Profesional profesional;

    public CitaMedica(LocalDate fecha, LocalTime hora, Paciente paciente, Profesional profesional) {
        this.fecha = fecha;
        this.hora = hora;
        setPaciente(paciente);
        setProfesional(profesional);
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public LocalTime getHora() {
        return hora;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        if (paciente == null) {
            System.out.println("Error: la cita necesita un paciente.");
            return;
        }
        this.paciente = paciente;
    }

    public Profesional getProfesional() {
        return profesional;
    }

    public void setProfesional(Profesional profesional) {
        if (profesional == null) {
            System.out.println("Error: la cita necesita un profesional.");
            return;
        }
        this.profesional = profesional;
    }

    @Override
    public String toString() {
        return "CitaMedica{fecha=" + fecha + ", hora=" + hora + ", paciente=" + paciente + ", profesional=" + profesional + "}";
    }
}
