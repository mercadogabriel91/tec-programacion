package ejercicio8;

import java.time.LocalDate;

public class FirmaDigital {
    private String codigoHash;
    private LocalDate fecha;
    private Usuario usuario;

    // agregación: el usuario que firma existe y se recibe de afuera
    public FirmaDigital(String codigoHash, LocalDate fecha, Usuario usuario) {
        this.codigoHash = codigoHash;
        this.fecha = fecha;
        setUsuario(usuario);
    }

    public String getCodigoHash() {
        return codigoHash;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    public void setUsuario(Usuario usuario) {
        if (usuario == null) {
            System.out.println("Error: la firma tiene que pertenecer a un usuario.");
            return;
        }
        this.usuario = usuario;
    }

    @Override
    public String toString() {
        return "FirmaDigital{codigoHash='" + codigoHash + "', fecha=" + fecha + ", usuario=" + usuario + "}";
    }
}
