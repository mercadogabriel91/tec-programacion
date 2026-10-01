package ejercicio2;

public class Celular {
    private String imei;
    private String marca;
    private String modelo;
    private Bateria bateria;
    private Usuario usuario;

    // agregación: la batería se crea afuera y llega ya armado el coso
    public Celular(String imei, String marca, String modelo, Bateria bateria) {
        this.imei = imei;
        this.marca = marca;
        this.modelo = modelo;
        setBateria(bateria);
    }

    public String getImei() {
        return imei;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public Bateria getBateria() {
        return bateria;
    }

    public void setBateria(Bateria bateria) {
        if (bateria == null) {
            System.out.println("Error: el celu necesita una bateria.");
            return;
        }
        this.bateria = bateria;
    }

    public Usuario getUsuario() {
        return usuario;
    }

    // asociación bidireccional: se mantienen en sync
    public void setUsuario(Usuario usuario) {
        if (this.usuario == usuario) {
            return;
        }
        Usuario anterior = this.usuario;
        this.usuario = usuario;
        if (anterior != null && anterior.getCelular() == this) {
            anterior.setCelular(null);
        }
        if (usuario != null) {
            usuario.setCelular(this);
        }
    }

    @Override
    public String toString() {
        return "Celular{imei='" + imei + "', marca='" + marca + "', modelo='" + modelo + "', bateria=" + bateria
                + ", usuario=" + (usuario != null ? usuario.getNombre() : "sin usuario") + "}";
    }
}
