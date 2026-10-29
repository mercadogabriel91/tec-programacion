package interfaces;

public enum EstadoPedido {
    PENDIENTE("Pendiente"),
    EN_PROCESO("En proceso"),
    PAGADO("Pagado");

    private final String descripcion;

    EstadoPedido(String descripcion) {
        this.descripcion = descripcion;
    }

    public String getDescripcion() {
        return descripcion;
    }

    @Override
    public String toString() {
        return descripcion;
    }
}
