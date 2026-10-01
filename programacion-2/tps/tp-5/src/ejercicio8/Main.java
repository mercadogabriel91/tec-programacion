package ejercicio8;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Composición (Documento -> FirmaDigital) y agregación (FirmaDigital -> Usuario) ---");
        Usuario usuario = new Usuario("Gabriel Mercado", "gabriel@algunmail.com");
        Documento contrato = new Documento("Contrato de alquiler", "que se yo un contrato de alquier acá",
                "a3f5c9e1b7d24f68", LocalDate.of(2026, 9, 29), usuario);
        System.out.println(contrato);

        System.out.println("\n--- Cada documento tiene su propia firma, el usuario es el mismo ---");
        Documento anexo = new Documento("Anexo I", "Inventario del departamento...",
                "9b1e77d0c4a2e5f3", LocalDate.of(2026, 9, 30), usuario);
        System.out.println("Las firmas son el mismo objeto? " + (contrato.getFirma() == anexo.getFirma()));
        System.out.println("El que firma es el mismo? " + (contrato.getFirma().getUsuario() == anexo.getFirma().getUsuario()));
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
