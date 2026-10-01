package ejercicio6;

import java.time.LocalDate;
import java.time.LocalTime;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Asociación unidireccional (Reserva -> Cliente) y agregación (Reserva -> Mesa) ---");
        Cliente cliente = new Cliente("Gabriel Mercado", "+545555555555");
        Mesa mesa4 = new Mesa(4, 2);
        Reserva reserva = new Reserva(LocalDate.of(2026, 10, 3), LocalTime.of(21, 30), cliente, mesa4);
        System.out.println(reserva);

        System.out.println("\n--- Cambio de mesa: la mesa anterior sigue existiendo en el local ---");
        Mesa mesa7 = new Mesa(7, 16); // Tenia mas gente que Mirtha en la mesa
        reserva.setMesa(mesa7);
        System.out.println(reserva);
        System.out.println("Mesa anterior: " + mesa4);
        reserva.setCliente(null); // te tira el error que no puede haber una reserva fantasma
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
