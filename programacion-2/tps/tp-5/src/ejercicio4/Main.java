package ejercicio4;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Agregación: TarjetaDeCredito -> Banco ---");
        Banco banco = new Banco("Banco Nación", "20-55555555-3");
        TarjetaDeCredito tarjeta = new TarjetaDeCredito("4509 9535 6623 3704", LocalDate.of(2029, 11, 30), banco);
        System.out.println(tarjeta);

        System.out.println("\n--- Asociación bidireccional: TarjetaDeCredito <-> Cliente ---");
        Cliente cliente = new Cliente("Gabriel Mercado", "55555555");
        cliente.setTarjeta(tarjeta);
        System.out.println(tarjeta);
        System.out.println(cliente);
        System.out.println("La tarjeta apunta al mismo cliente? " + (tarjeta.getCliente() == cliente));

        System.out.println("\n--- Desvincular desde un lado deja limpio el otro ---");
        tarjeta.setCliente(null);
        System.out.println(tarjeta);
        System.out.println(cliente);
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
