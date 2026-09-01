package Ejercicio_02;

public class Main {
    public static void main() {
        Mascota mascota = new Mascota();

        // probar darle una edad negativa
        System.out.println("--- Prueba con edad inválida ---");
        mascota.setEdad(-3);
        System.out.println("Edad actual: " + mascota.getEdad());

        // asignar datos válidos
        System.out.println("\n--- Carga de datos válidos ---");
        mascota.setNombre("Waton");
        mascota.setEspecie("Perro");
        mascota.setEdad(3);
        mascota.mostrarInfo();

        // mandarle un cumple
        System.out.println("\n--- Cumpliendo años ---");
        mascota.cumplirAnios();
        mascota.cumplirAnios();
        mascota.cumplirAnios();

        System.out.println("\n--- Información final ---");
        mascota.mostrarInfo();
    }
}

/*
 * //REPO URL: https://github.com/mercadogabriel91/tec-programacion/tree/master/programacion-2/tps/tp-3/src
 */
