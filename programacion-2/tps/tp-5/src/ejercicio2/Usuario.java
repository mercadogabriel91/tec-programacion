package ejercicio2;

public class Usuario {
    private String nombre;
    private String dni;
    private Celular celular;

    public Usuario(String nombre, String dni) {
        this.nombre = nombre;
        this.dni = dni;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDni() {
        return dni;
    }

    public Celular getCelular() {
        return celular;
    }

    public void setCelular(Celular celular) {
        if (this.celular == celular) {
            return;
        }
        Celular anterior = this.celular;
        this.celular = celular;
        if (anterior != null && anterior.getUsuario() == this) {
            anterior.setUsuario(null);
        }
        if (celular != null) {
            celular.setUsuario(this);
        }
    }

    @Override
    public String toString() {
        return "Usuario{nombre='" + nombre + "', dni='" + dni + "', celular="
                + (celular != null ? celular.getMarca() + " " + celular.getModelo() : "sin celular") + "}";
    }
}
