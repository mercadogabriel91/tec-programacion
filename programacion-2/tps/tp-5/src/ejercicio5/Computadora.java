package ejercicio5;

public class Computadora {
    private String marca;
    private String numeroSerie;
    private final PlacaMadre placaMadre;
    private Propietario propietario;

    // composición: la placa madre se crea adentro espawnea y despawnea acá
    public Computadora(String marca, String numeroSerie, String modeloPlaca, String chipsetPlaca) {
        this.marca = marca;
        this.numeroSerie = numeroSerie;
        this.placaMadre = new PlacaMadre(modeloPlaca, chipsetPlaca);
    }

    public String getMarca() {
        return marca;
    }

    public String getNumeroSerie() {
        return numeroSerie;
    }

    public PlacaMadre getPlacaMadre() {
        return placaMadre;
    }

    public Propietario getPropietario() {
        return propietario;
    }

    // asociación bidireccional: mantiene sincronizados los dos lados
    public void setPropietario(Propietario propietario) {
        if (this.propietario == propietario) {
            return;
        }
        Propietario anterior = this.propietario;
        this.propietario = propietario;
        if (anterior != null && anterior.getComputadora() == this) {
            anterior.setComputadora(null);
        }
        if (propietario != null) {
            propietario.setComputadora(this);
        }
    }

    @Override
    public String toString() {
        return "Computadora{marca='" + marca + "', numeroSerie='" + numeroSerie + "', placaMadre=" + placaMadre
                + ", propietario=" + (propietario != null ? propietario.getNombre() : "sin propietario") + "}";
    }
}
