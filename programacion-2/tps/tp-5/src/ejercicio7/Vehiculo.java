package ejercicio7;

public class Vehiculo {
    private String patente;
    private String modelo;
    private Motor motor;
    private Conductor conductor;

    // agregación: el motor se fabrica afuera
    public Vehiculo(String patente, String modelo, Motor motor) {
        this.patente = patente;
        this.modelo = modelo;
        setMotor(motor);
    }

    public String getPatente() {
        return patente;
    }

    public String getModelo() {
        return modelo;
    }

    public Motor getMotor() {
        return motor;
    }

    public void setMotor(Motor motor) {
        if (motor == null) {
            System.out.println("Error: el vehículo necesita un motor.");
            return;
        }
        this.motor = motor;
    }

    public Conductor getConductor() {
        return conductor;
    }

    // asociación bidireccional: mantiene sincronizados los dos lados
    public void setConductor(Conductor conductor) {
        if (this.conductor == conductor) {
            return;
        }
        Conductor anterior = this.conductor;
        this.conductor = conductor;
        if (anterior != null && anterior.getVehiculo() == this) {
            anterior.setVehiculo(null);
        }
        if (conductor != null) {
            conductor.setVehiculo(this);
        }
    }

    @Override
    public String toString() {
        return "Vehiculo{patente='" + patente + "', modelo='" + modelo + "', motor=" + motor
                + ", conductor=" + (conductor != null ? conductor.getNombre() : "sin conductor") + "}";
    }
}
