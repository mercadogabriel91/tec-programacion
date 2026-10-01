package ejercicio1;

import java.time.LocalDate;

public class Pasaporte {
    private String numero;
    private LocalDate fechaEmision;
    private final Foto foto;
    private Titular titular;

    // composición: la foto se crea adentro y nace y se muere con el pasaporte
    public Pasaporte(String numero, LocalDate fechaEmision, String imagen, String formato) {
        this.numero = numero;
        this.fechaEmision = fechaEmision;
        this.foto = new Foto(imagen, formato);
    }

    public String getNumero() {
        return numero;
    }

    public LocalDate getFechaEmision() {
        return fechaEmision;
    }

    public Foto getFoto() {
        return foto;
    }

    public Titular getTitular() {
        return titular;
    }

    // asociación bidireccional: mantiene sincronizados a los dos lados
    public void setTitular(Titular titular) {
        if (this.titular == titular) {
            return;
        }
        Titular anterior = this.titular;
        this.titular = titular;
        if (anterior != null && anterior.getPasaporte() == this) {
            anterior.setPasaporte(null);
        }
        if (titular != null) {
            titular.setPasaporte(this);
        }
    }

    @Override
    public String toString() {
        return "Pasaporte{numero='" + numero + "', fechaEmision=" + fechaEmision + ", foto=" + foto
                + ", titular=" + (titular != null ? titular.getNombre() : "sin titular") + "}";
    }
}
