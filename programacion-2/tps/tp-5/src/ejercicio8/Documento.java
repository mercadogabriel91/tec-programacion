package ejercicio8;

import java.time.LocalDate;

public class Documento {
    private String titulo;
    private String contenido;
    private final FirmaDigital firma;

    // composición: la firma se crea adentro
    public Documento(String titulo, String contenido, String codigoHash, LocalDate fechaFirma, Usuario firmante) {
        this.titulo = titulo;
        this.contenido = contenido;
        this.firma = new FirmaDigital(codigoHash, fechaFirma, firmante);
    }

    public String getTitulo() {
        return titulo;
    }

    public String getContenido() {
        return contenido;
    }

    public FirmaDigital getFirma() {
        return firma;
    }

    @Override
    public String toString() {
        return "Documento{titulo='" + titulo + "', contenido='" + contenido + "', firma=" + firma + "}";
    }
}
