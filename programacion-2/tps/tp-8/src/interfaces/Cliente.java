package interfaces;

public class Cliente implements Notificable {
    private String nombre;
    private String email;

    public Cliente(String nombre, String email) {
        this.nombre = nombre;
        this.email = email;
    }

    public String getNombre() {
        return nombre;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public void notificarCambioDeEstado(EstadoPedido nuevoEstado) {
        System.out.println("Notificación a " + nombre + " (" + email + "): el pedido ahora está " + nuevoEstado + ".");
    }

    public void mostrarInfo() {
        System.out.println(nombre + " | " + email);
    }

    @Override
    public String toString() {
        return "Cliente{nombre='" + nombre + "', email='" + email + "'}";
    }
}
