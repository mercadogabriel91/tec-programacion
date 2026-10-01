package ejercicio10;

public class Main {
    public static void main(String[] args) {
        System.out.println("--- Composición: CuentaBancaria -> ClaveSeguridad ---");
        CuentaBancaria cuenta = new CuentaBancaria("0110599520000012345678", 150000, "4821");
        System.out.println(cuenta);

        System.out.println("\n--- La clave solo se maneja desde de la cuenta ---");
        cuenta.cambiarClave("0000", "9173"); // clave incorrecta
        cuenta.cambiarClave("4821", "12"); // clave muy corta
        cuenta.cambiarClave("4821", "9173");

        System.out.println("\n--- Asociación bidireccional: CuentaBancaria <-> Titular ---");
        Titular titular = new Titular("Gabriel Mercado", "55555555");
        titular.setCuenta(cuenta);
        System.out.println(cuenta);
        System.out.println(titular);
        System.out.println("La cuenta apunta al mismo titular? " + (cuenta.getTitular() == titular));
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-5/src
 */
