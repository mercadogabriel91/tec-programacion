package ejercicio10;

import java.time.LocalDate;

public class ClaveSeguridad {
    private String codigo;
    private LocalDate ultimaModificacion;

    public ClaveSeguridad(String codigo) {
        this.codigo = codigo;
        this.ultimaModificacion = LocalDate.now();
    }

    public LocalDate getUltimaModificacion() {
        return ultimaModificacion;
    }

    public boolean coincide(String codigo) {
        return this.codigo.equals(codigo);
    }

    public void actualizar(String nuevoCodigo) {
        if (nuevoCodigo == null || nuevoCodigo.length() < 4) {
            System.out.println("Error: la clave debe tener al menos 4 caracteres.");
            return;
        }
        this.codigo = nuevoCodigo;
        this.ultimaModificacion = LocalDate.now();
        System.out.println("Clave actualizada correctamente.");
    }

    @Override
    public String toString() {
        return "ClaveSeguridad{codigo='****', ultimaModificacion=" + ultimaModificacion + "}";
    }
}
