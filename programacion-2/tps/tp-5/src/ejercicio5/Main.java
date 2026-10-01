package ejercicio5;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Composición: Computadora -> PlacaMadre ---");
        Computadora computadora = new Computadora("Lenovo", "PF3K9X2A", "B550M Pro", "AMD B550");
        System.out.println("La placa madre la crea la compu: " + computadora.getPlacaMadre());

        System.out.println("\n--- Asociación bidireccional: Computadora <-> Propietario ---");
        Propietario propietario = new Propietario("Gabriel Mercado", "55555555");
        computadora.setPropietario(propietario);
        System.out.println(computadora);
        System.out.println(propietario);
        System.out.println("El propietario apunta a la misma computadora? " + (propietario.getComputadora() == computadora));

        System.out.println("\n--- Venta: la computadora cambia de propietario ---");
        Propietario comprador = new Propietario("Raul", "55666655");
        comprador.setComputadora(computadora);
        System.out.println(computadora);
        System.out.println(propietario);
        System.out.println(comprador);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
