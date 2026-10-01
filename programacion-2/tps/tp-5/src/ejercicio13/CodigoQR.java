package ejercicio13;

public class CodigoQR {
    private String valor;
    private Usuario usuario;

    public CodigoQR(String valor, Usuario usuario) {
        this.valor = valor;
        setUsuario(usuario);
    }

    public String getValor() {
        return valor;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        if (usuario == null) {
            System.out.println("Error: el código QR necesita un usuario.");
            return;
        }
        this.usuario = usuario;
    }

    @Override
    public String toString() {
        return "CodigoQR{valor='" + valor + "', usuario=" + usuario + "}";
    }
}
