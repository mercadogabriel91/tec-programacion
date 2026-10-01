package ejercicio1;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Composición: Pasaporte -> Foto ---");
        Pasaporte pasaporte = new Pasaporte("AAB123456", LocalDate.of(2024, 3, 15), "foto_gabriel.jpg", "JPG");
        System.out.println("La foto la crea el propio pasaporte: " + pasaporte.getFoto());

        System.out.println("\n--- Asociación bidireccional: Pasaporte <-> Titular ---");
        Titular titular = new Titular("Gabriel Mercado", "40545665");
        pasaporte.setTitular(titular); //lo vinculas de un solo lado
        System.out.println(pasaporte);
        System.out.println(titular);
        System.out.println("El titular apunta al mismo pasaporte? " + (titular.getPasaporte() == pasaporte));

        System.out.println("\n--- Reasignación: el titular anterior queda desvinculado ---");
        Titular nuevoTitular = new Titular("Ana Pérez", "38111222");
        nuevoTitular.setPasaporte(pasaporte);
        System.out.println(pasaporte);
        System.out.println(titular);
        System.out.println(nuevoTitular);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
