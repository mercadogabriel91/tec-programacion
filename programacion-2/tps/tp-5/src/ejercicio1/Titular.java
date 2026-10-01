package ejercicio1;

public class Titular {
    private String nombre;
    private String dni;
    private Pasaporte pasaporte;

    public Titular(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public Pasaporte getPasaporte() {
        return pasaporte;
    }

    public void setPasaporte(Pasaporte pasaporte) {
        if (this.pasaporte == pasaporte) {
            return;
        }
        Pasaporte anterior = this.pasaporte;
        this.pasaporte = pasaporte;
        if (anterior != null && anterior.getTitular() == this) {
            anterior.setTitular(null);
        }
        if (pasaporte != null) {
            pasaporte.setTitular(this);
        }
    }

    @Override
    public String toString() {
        return "Titular{nombre='" + nombre + "', dni='" + dni + "', pasaporte="
                + (pasaporte != null ? pasaporte.getNumero() : "sin pasaporte") + "}";
    }
}
