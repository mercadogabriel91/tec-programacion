package Ejercicio_05;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Creación con ambos constructores ---");
        Cuenta c1 = new Cuenta("Gabriel Mercado", 2000);
        Cuenta c2 = new Cuenta("Ana Pérez"); // saldo 0
        Cuenta c3 = new Cuenta("Luis Gómez", 5000);

        System.out.println("Números que van asumentando automaticamente:");
        System.out.println(c1);
        System.out.println(c2);
        System.out.println(c3);

        System.out.println("\n--- Operaciones ---");
        c2.depositar(1500);
        c1.extraer(3000); // más de lo que hay
        c1.extraer(-50);
        c1.depositar(500);
        c1.extraer(1000);

        System.out.println("\n--- Saldo en dólares ---");
        System.out.println("Saldo de c1 en pesos: " + c1.consultarSaldo());
        System.out.println("Saldo de c1 en dólares (cotización 1582): " + c1.consultarSaldo(1582));

        System.out.println();
        Cuenta.mostrarTotalCuentas();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-4/src
 */
